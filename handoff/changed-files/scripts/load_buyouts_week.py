"""Read only the explicitly requested week; keep source responses for verification."""
import argparse
import json
import time
import urllib.request
import urllib.error
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('--start',type=date.fromisoformat,required=True)
parser.add_argument('--stop',type=date.fromisoformat,required=True)
args=parser.parse_args()
if not 0 <= (args.stop-args.start).days <= 6:
    raise SystemExit('This import is restricted to at most seven calendar days.')
env={}
for line in Path('C:/dev/SVOYO/.env').read_text(encoding='utf-8-sig').splitlines():
    key,sep,value=line.partition('=')
    if sep and not key.lstrip().startswith('#'):
        env[key.strip()]=value.strip().strip('"').strip("'")
out=Path(__file__).resolve().parents[1]/'backups'/'cis-week-20261028'
out.mkdir(parents=True,exist_ok=True)
day=args.start
while day <= args.stop:
    body=json.dumps({'date_from':day.isoformat(),'date_to':day.isoformat()}).encode()
    request=urllib.request.Request('https://api-seller.ozon.ru/v1/finance/products/buyout',data=body,
        headers={'Client-Id':env['OZON_SVOYO_CLIENT_ID'],'Api-Key':env['OZON_SVOYO_API_KEY'],'Content-Type':'application/json'})
    for attempt in range(12):
        try:
            with urllib.request.urlopen(request,timeout=45) as response:
                payload=json.load(response)
            break
        except urllib.error.HTTPError as exc:
            if exc.code!=429:
                raise
            wait=max(5,min(60,int(exc.headers.get('Retry-After','5'))))
            print(f'Rate limit for {day}, waiting {wait}s (attempt {attempt+1})',flush=True)
            time.sleep(wait)
    else:
        raise RuntimeError(f'Buyout API rate limit did not clear for {day}')
    if not isinstance(payload.get('products'),list):
        raise ValueError(f'Buyout report has no products list for {day}')
    (out/f'{day}.json').write_text(json.dumps({'day':day.isoformat(),
        'fetched_at':datetime.now(timezone.utc).isoformat(),'payload':payload},ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{day}: {len(payload["products"])} rows, {sum(r["quantity"] for r in payload["products"])} units',flush=True)
    day+=timedelta(days=1)
    if day<=args.stop:
        time.sleep(2)
