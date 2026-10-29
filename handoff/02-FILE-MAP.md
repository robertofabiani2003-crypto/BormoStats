# Карта всех локальных доработок

База: `282a1e0ef9ab5a39c69276e64d6fadfc3c30d5e8`. 41 изменённых и 60 новых файлов.

| Файл | Статус | Что изменено / назначение |
| --- | --- | --- |
| [.dockerignore](changed-files/.dockerignore) | Изменён | Исключает локальные резервные копии и результаты из Docker-контекста. |
| [.gitignore](changed-files/.gitignore) | Изменён | Исключает локальный файл входа LOGIN.local.txt из Git. |
| [ARTICLE-ECONOMICS.md](changed-files/ARTICLE-ECONOMICS.md) | Добавлен | Предыдущие пояснения экономики артикулов и ручных сверок; часть описаний устарела. |
| [LOCAL-SETUP.md](changed-files/LOCAL-SETUP.md) | Добавлен | Инструкция локального запуска SVOYO; состояние миграций требует актуализации. |
| [PNL-TAX-ROLLBACK.md](changed-files/PNL-TAX-ROLLBACK.md) | Добавлен | Предыдущие налоговые правила и переключение флага; часть описаний устарела. |
| [REPORT-SYNC.md](changed-files/REPORT-SYNC.md) | Добавлен | Подробное описание ежедневного цикла и согласованности отчётов. |
| [Set-PnlTax.ps1](changed-files/Set-PnlTax.ps1) | Добавлен | Меняет налоговый флаг в локальном .env и применяет настройку backend. |
| [Start-BormoStats.ps1](changed-files/Start-BormoStats.ps1) | Добавлен | Запускает локальный Docker Compose с дополнительной конфигурацией. |
| [Stop-BormoStats.ps1](changed-files/Stop-BormoStats.ps1) | Добавлен | Останавливает локальные контейнеры с сохранением томов. |
| [backend/app/api/v1/economics.py](changed-files/backend/app/api/v1/economics.py) | Добавлен | Добавляет API экономики артикулов Ozon за выбранный период. |
| [backend/app/api/v1/finance.py](changed-files/backend/app/api/v1/finance.py) | Изменён | Добавляет выбор даты снимка финансового баланса. |
| [backend/app/api/v1/funnel.py](changed-files/backend/app/api/v1/funnel.py) | Изменён | Добавляет импорт воронки Ozon и API для заказов, финансов, рекламы и остатков. |
| [backend/app/api/v1/pnl.py](changed-files/backend/app/api/v1/pnl.py) | Изменён | Расширяет модели или API P&L: налог, дневной отчёт, периоды и дата внешнего расхода. |
| [backend/app/api/v1/stocks.py](changed-files/backend/app/api/v1/stocks.py) | Изменён | Добавляет параметр даты для исторического снимка остатков. |
| [backend/app/db/queries/finance_balance.sql](changed-files/backend/app/db/queries/finance_balance.sql) | Изменён | Ограничивает баланс и последнюю выплату выбранной датой. |
| [backend/app/db/queries/stocks.sql](changed-files/backend/app/db/queries/stocks.sql) | Изменён | Добавляет остатки на дату и их стоимость по себестоимости. |
| [backend/app/main.py](changed-files/backend/app/main.py) | Изменён | Подключает API экономики артикулов. |
| [backend/app/models/admin.py](changed-files/backend/app/models/admin.py) | Изменён | Расширяет допустимые наборы данных ручной дозагрузки. |
| [backend/app/models/pnl.py](changed-files/backend/app/models/pnl.py) | Изменён | Расширяет модели или API P&L: налог, дневной отчёт, периоды и дата внешнего расхода. |
| [backend/app/services/admin_service.py](changed-files/backend/app/services/admin_service.py) | Изменён | Маршрутизирует новые наборы данных ручной дозагрузки Ozon. |
| [backend/app/services/article_economics_service.py](changed-files/backend/app/services/article_economics_service.py) | Добавлен | Собирает экономику SKU из начислений, рекламы, выкупов, себестоимости и налога. |
| [backend/app/services/daily_pnl_service.py](changed-files/backend/app/services/daily_pnl_service.py) | Добавлен | Считает дневную прибыль, распределяет месячные суммы по дням и возвращает остатки. |
| [backend/app/services/metrics_service.py](changed-files/backend/app/services/metrics_service.py) | Изменён | Передаёт дату снимка и меняет ключ кеша остатков для новых полей стоимости. |
| [backend/app/services/ozon_cis_service.py](changed-files/backend/app/services/ozon_cis_service.py) | Добавлен | Добавляет выкупы СНГ без пересечения с обычными продажами. |
| [backend/app/services/pnl_service.py](changed-files/backend/app/services/pnl_service.py) | Изменён | Корректирует финансирование, СНГ, налог и сохранение расходов с датой. |
| [collectors/ozon/client.py](changed-files/collectors/ozon/client.py) | Изменён | Расширяет клиент Ozon: реализация, выкупы, SKU-реклама и метаданные кампаний. |
| [collectors/ozon/endpoints.py](changed-files/collectors/ozon/endpoints.py) | Изменён | Добавляет пути запросов реализации и выкупов Ozon. |
| [collectors/ozon/sku_ad_reports.py](changed-files/collectors/ozon/sku_ad_reports.py) | Добавлен | Разбирает SKU-рекламу, проверяет свежесть и подготавливает метаданные кампаний. |
| [common/article_economics.py](changed-files/common/article_economics.py) | Добавлен | Содержит денежные формулы экономики, классификацию удержаний и привязку рекламы. |
| [common/celery_config.py](changed-files/common/celery_config.py) | Изменён | Регистрирует модуль единого ежедневного цикла. |
| [common/economics_reference_images.json](changed-files/common/economics_reference_images.json) | Добавлен | Хранит резервные ссылки на фотографии конкретных артикулов магазина. |
| [common/env_validation.py](changed-files/common/env_validation.py) | Изменён | Разрешает запуск с одной настроенной площадкой; проверяет полную пару её ключей. |
| [common/funnel_economics.py](changed-files/common/funnel_economics.py) | Добавлен | Считает финансовые события воронки, типы рекламы и показатели остатков. |
| [common/ozon_buyouts.py](changed-files/common/ozon_buyouts.py) | Добавлен | Разбирает отчёт отдельных выкупов СНГ. |
| [common/pnl_tax.py](changed-files/common/pnl_tax.py) | Добавлен | Проверяет реализацию и считает налог по заданной ставке с округлением. |
| [compose.local.yaml](changed-files/compose.local.yaml) | Добавлен | Добавляет локальные bind-mount файлов и доступ к интерфейсу через loopback. |
| [docs/architecture.md](changed-files/docs/architecture.md) | Изменён | Описывает ежедневную последовательную загрузку вместо независимых таймеров. |
| [docs/data_catalog.md](changed-files/docs/data_catalog.md) | Изменён | Обновляет описание источников и периодичности данных. |
| [frontend/e2e/date-range.spec.js](changed-files/frontend/e2e/date-range.spec.js) | Добавлен | Проверяет выбор периода через браузер. |
| [frontend/e2e/pnl-expenses.spec.js](changed-files/frontend/e2e/pnl-expenses.spec.js) | Добавлен | Проверяет ввод внешних расходов через браузер. |
| [frontend/src/App.jsx](changed-files/frontend/src/App.jsx) | Изменён | Добавляет маршрут раздела экономики. |
| [frontend/src/components/DateRangePicker.css](changed-files/frontend/src/components/DateRangePicker.css) | Добавлен | Стили календаря выбора периода. |
| [frontend/src/components/DateRangePicker.jsx](changed-files/frontend/src/components/DateRangePicker.jsx) | Добавлен | Календарь и готовые периоды выбора дат. |
| [frontend/src/components/ExpenseForm.jsx](changed-files/frontend/src/components/ExpenseForm.jsx) | Добавлен | Форма добавления внешнего расхода с датой. |
| [frontend/src/components/FiltersBar.jsx](changed-files/frontend/src/components/FiltersBar.jsx) | Изменён | Подключает новый выбор периода вместо прежних полей дат. |
| [frontend/src/components/FreshnessBanner.jsx](changed-files/frontend/src/components/FreshnessBanner.jsx) | Изменён | Приводит порог устаревания к ежедневной загрузке. |
| [frontend/src/components/Layout.jsx](changed-files/frontend/src/components/Layout.jsx) | Изменён | Добавляет экономику в навигацию. |
| [frontend/src/pages/Dashboard.jsx](changed-files/frontend/src/pages/Dashboard.jsx) | Изменён | Читает дневной P&L, показывает прибыль, налог, внешние расходы и стоимость остатков. |
| [frontend/src/pages/Economics.jsx](changed-files/frontend/src/pages/Economics.jsx) | Добавлен | Таблица экономики артикулов, группы столбцов, итоги и экспорт. |
| [frontend/src/pages/Funnel.jsx](changed-files/frontend/src/pages/Funnel.jsx) | Изменён | Подключает отдельное представление воронки Ozon. |
| [frontend/src/pages/OzonFunnel.jsx](changed-files/frontend/src/pages/OzonFunnel.jsx) | Добавлен | Импорт Excel и отображение расширенной воронки Ozon. |
| [frontend/src/pages/PnL.jsx](changed-files/frontend/src/pages/PnL.jsx) | Изменён | Добавляет дневные итоги, статусы налога и форму внешнего расхода. |
| [frontend/src/utils/dashboardProfit.js](changed-files/frontend/src/utils/dashboardProfit.js) | Добавлен | Прежний вспомогательный расчёт месячной прибыли; текущий Dashboard читает дневной API. |
| [frontend/src/utils/dashboardProfit.test.mjs](changed-files/frontend/src/utils/dashboardProfit.test.mjs) | Добавлен | Проверяет прежний вспомогательный расчёт месячной прибыли. |
| [frontend/src/utils/dateRange.js](changed-files/frontend/src/utils/dateRange.js) | Добавлен | Функции календаря и готовых периодов. |
| [frontend/src/utils/dateRange.test.mjs](changed-files/frontend/src/utils/dateRange.test.mjs) | Добавлен | Проверяет периоды, переходы года и високосный февраль. |
| [frontend/src/utils/economicsColumns.js](changed-files/frontend/src/utils/economicsColumns.js) | Добавлен | Определяет столбцы и группы экономики артикулов. |
| [frontend/src/utils/i18n.jsx](changed-files/frontend/src/utils/i18n.jsx) | Изменён | Добавляет подписи стоимости остатков и отсутствующей себестоимости. |
| [frontend/src/utils/ozonFunnel.js](changed-files/frontend/src/utils/ozonFunnel.js) | Добавлен | Разбирает импортируемый Excel и объединяет данные воронки. |
| [frontend/src/utils/ozonFunnelDefinitions.js](changed-files/frontend/src/utils/ozonFunnelDefinitions.js) | Добавлен | Определяет столбцы и пояснения показателей воронки. |
| [frontend/src/utils/ozonFunnelMetrics.js](changed-files/frontend/src/utils/ozonFunnelMetrics.js) | Добавлен | Вычисляет показатели и прогнозы воронки Ozon. |
| [frontend/src/utils/ozonFunnelMetrics.test.mjs](changed-files/frontend/src/utils/ozonFunnelMetrics.test.mjs) | Добавлен | Проверяет даты событий, прогнозы, остатки и классификацию рекламы. |
| [frontend/src/utils/xlsx.js](changed-files/frontend/src/utils/xlsx.js) | Изменён | Расширяет экспорт таблиц для новых полей. |
| [infra/monitoring/prometheus/alerts.test.yml](changed-files/infra/monitoring/prometheus/alerts.test.yml) | Изменён | Обновляет ожидаемые результаты тестов порогов устаревания. |
| [infra/monitoring/prometheus/alerts.yml](changed-files/infra/monitoring/prometheus/alerts.yml) | Изменён | Настраивает оповещения под ежедневную загрузку. |
| [scripts/load_buyouts_week.py](changed-files/scripts/load_buyouts_week.py) | Добавлен | Скрипт ручной загрузки выкупов за выбранную неделю. |
| [tests/integration/test_pipeline_smoke.py](changed-files/tests/integration/test_pipeline_smoke.py) | Изменён | Адаптирует интеграционный smoke-тест к обновлённой сборке данных. |
| [tests/unit/test_article_economics.py](changed-files/tests/unit/test_article_economics.py) | Добавлен | Проверяет формулы экономики, удержания и привязку рекламы. |
| [tests/unit/test_buyout_economics.py](changed-files/tests/unit/test_buyout_economics.py) | Добавлен | Проверяет экономику СНГ и исключение повторных продаж. |
| [tests/unit/test_celery_config.py](changed-files/tests/unit/test_celery_config.py) | Изменён | Проверяет регистрацию новых задач. |
| [tests/unit/test_daily_pnl.py](changed-files/tests/unit/test_daily_pnl.py) | Добавлен | Проверяет дневной расчёт и распределение месячных сумм. |
| [tests/unit/test_expense_dates.py](changed-files/tests/unit/test_expense_dates.py) | Добавлен | Проверяет дату расхода и перенос между месяцами. |
| [tests/unit/test_funnel_economics.py](changed-files/tests/unit/test_funnel_economics.py) | Добавлен | Проверяет финансовые дни, типы кампаний и остатки воронки. |
| [tests/unit/test_pnl_financing.py](changed-files/tests/unit/test_pnl_financing.py) | Добавлен | Проверяет исключение потоков долга из расходов. |
| [tests/unit/test_pnl_tax.py](changed-files/tests/unit/test_pnl_tax.py) | Добавлен | Проверяет базу налога, структуру реализации и округление. |
| [tests/unit/test_pnl_tax_service.py](changed-files/tests/unit/test_pnl_tax_service.py) | Добавлен | Проверяет применение налога к месячному P&L. |
| [tests/unit/test_rebuild_serialization.py](changed-files/tests/unit/test_rebuild_serialization.py) | Изменён | Проверяет окна пересчёта рекламы и сохранение истории планирования поставок. |
| [tests/unit/test_sku_ad_reports.py](changed-files/tests/unit/test_sku_ad_reports.py) | Добавлен | Проверяет разбор и свежесть рекламных отчётов. |
| [tests/worker_suite/test_daily_reports.py](changed-files/tests/worker_suite/test_daily_reports.py) | Добавлен | Проверяет последовательность ежедневного цикла, блокировки и повторные запуски. |
| [tests/worker_suite/test_sku_report_collection.py](changed-files/tests/worker_suite/test_sku_report_collection.py) | Добавлен | Проверяет загрузку, кеширование и исправленные версии SKU-отчётов. |
| [warehouse/migrations/0039_ozon_realization_tax.sql](changed-files/warehouse/migrations/0039_ozon_realization_tax.sql) | Добавлен | Миграция: месячная реализация Ozon для налога. |
| [warehouse/migrations/0040_ozon_ads_sku.sql](changed-files/warehouse/migrations/0040_ozon_ads_sku.sql) | Добавлен | Миграция: расходы рекламы по SKU. |
| [warehouse/migrations/0041_ozon_sku_report_jobs.sql](changed-files/warehouse/migrations/0041_ozon_sku_report_jobs.sql) | Добавлен | Миграция: UUID и состояние заданий рекламных отчётов. |
| [warehouse/migrations/0042_ozon_buyouts_daily.sql](changed-files/warehouse/migrations/0042_ozon_buyouts_daily.sql) | Добавлен | Миграция: дневные снимки выкупов СНГ. |
| [warehouse/migrations/0043_ozon_funnel_import.sql](changed-files/warehouse/migrations/0043_ozon_funnel_import.sql) | Добавлен | Миграция: импорт Excel-воронки Ozon. |
| [warehouse/migrations/0044_ozon_campaign_metadata.sql](changed-files/warehouse/migrations/0044_ozon_campaign_metadata.sql) | Добавлен | Миграция: история метаданных рекламных кампаний. |
| [warehouse/migrations/0045_expense_date.sql](changed-files/warehouse/migrations/0045_expense_date.sql) | Добавлен | Миграция: дата внешнего расхода. |
| [warehouse/migrations/rollbacks/0039_ozon_realization_tax.sql](changed-files/warehouse/migrations/rollbacks/0039_ozon_realization_tax.sql) | Добавлен | Откат: месячная реализация Ozon для налога. |
| [warehouse/migrations/rollbacks/0040_ozon_ads_sku.sql](changed-files/warehouse/migrations/rollbacks/0040_ozon_ads_sku.sql) | Добавлен | Откат: расходы рекламы по SKU. |
| [warehouse/migrations/rollbacks/0041_ozon_sku_report_jobs.sql](changed-files/warehouse/migrations/rollbacks/0041_ozon_sku_report_jobs.sql) | Добавлен | Откат: UUID и состояние заданий рекламных отчётов. |
| [warehouse/migrations/rollbacks/0042_ozon_buyouts_daily.sql](changed-files/warehouse/migrations/rollbacks/0042_ozon_buyouts_daily.sql) | Добавлен | Откат: дневные снимки выкупов СНГ. |
| [warehouse/migrations/rollbacks/0043_ozon_funnel_import.sql](changed-files/warehouse/migrations/rollbacks/0043_ozon_funnel_import.sql) | Добавлен | Откат: импорт Excel-воронки Ozon. |
| [warehouse/migrations/rollbacks/0045_expense_date.sql](changed-files/warehouse/migrations/rollbacks/0045_expense_date.sql) | Добавлен | Откат: дата внешнего расхода. |
| [workers/app/beat_schedule.py](changed-files/workers/app/beat_schedule.py) | Изменён | Заменяет регулярные таймеры аналитики единым запуском в 06:00. |
| [workers/app/celery_app.py](changed-files/workers/app/celery_app.py) | Изменён | Подключает новый модуль задач reports. |
| [workers/app/sql/marts/mrt_pnl_monthly.sql](changed-files/workers/app/sql/marts/mrt_pnl_monthly.sql) | Изменён | Берёт рекламу из финансовых удержаний и устраняет её повторный вычет. |
| [workers/app/tasks/marts.py](changed-files/workers/app/tasks/marts.py) | Изменён | Согласует удаление и вставку рекламных окон; сохраняет прошлые снимки планирования. |
| [workers/app/tasks/ozon_collect.py](changed-files/workers/app/tasks/ozon_collect.py) | Изменён | Расширяет сбор реализации, выкупов и рекламы; обновляет статусы отправлений и баланс. |
| [workers/app/tasks/reports.py](changed-files/workers/app/tasks/reports.py) | Добавлен | Последовательно запускает сбор, преобразования, витрины и проверки с контрольными точками Redis. |
| [workers/app/utils/data_quality.py](changed-files/workers/app/utils/data_quality.py) | Изменён | Обновляет контроль свежести под ежедневный цикл. |
| [workers/app/utils/watermarks.py](changed-files/workers/app/utils/watermarks.py) | Изменён | Передаёт временные отметки с часовым поясом. |
