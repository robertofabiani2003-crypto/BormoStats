# Выполненные проверки и ограничения

Проверено 29.10.2026 на исходной рабочей папке C:/dev/BormoStats. Данные маркетплейсов не загружались, рабочие сервисы не перезапускались.

| Проверка | Результат |
| --- | --- |
| Git status, HEAD, main, origin/main, diff | Определена база 282a1e0; 41 изменённый + 60 новых исходных файлов |
| git diff --check | Успех; предупреждения Git о нормализации CRLF/LF |
| node --test src/utils/dashboardProfit.test.mjs src/utils/dateRange.test.mjs src/utils/ozonFunnelMetrics.test.mjs | 10/10 успешно |
| npm run build с --outDir вне рабочей установки | Успех; предупреждение о крупном JS chunk >500 kB |
| Python AST для 45 изменённых/новых .py | 44 разобраны Python 3.13; client.py использует синтаксис except Python 3.14, присутствующий и в исходном HEAD; это не найденная новая синтаксическая ошибка |
| python -m unittest tests.unit.test_article_economics tests.unit.test_buyout_economics tests.unit.test_funnel_economics tests.unit.test_pnl_tax tests.unit.test_sku_ad_reports | Запущено 22 unittest: 21 успешно, 1 ошибка окружения — нет tzdata/Europe/Moscow. Функциональные pytest-тесты test_funnel_economics этим запуском не выполняются |
| pytest выбранных backend unit-тестов | Не запущен: No module named pytest |
| python warehouse/apply_migrations.py verify | Не запущен: No module named clickhouse_connect |
| Наличие rollback по правилу verify_manifest, отдельная файловая проверка | Нет rollback для 0044_ozon_campaign_metadata.sql; конкретный дефект комплекта |

Окружение: системный Python 3.13; проект и CI требуют Python >=3.14. Системное окружение и зависимости не менялись. Вложения старых документов о ручных сверках с Ozon/Excel не считаются повторно выполненными проверками этого аудита.

Не выполнены: полный pytest, worker-suite, mypy, Ruff, Playwright, promtool, интеграции ClickHouse/Redis, чистые Docker builds, фактическое применение/откат миграций и сверка денег по рабочему магазину. Поэтому пакет не является подтверждением готовности к эксплуатации.

После подготовки пакета дополнительно проверяется: git apply --check на чистой базе, отсутствие потерянных исходных файлов и совпадение SHA-256 всех changed-files с inventory.json. Итог этих проверок записан в PACKAGE-CHECK.txt.
