"""
fetch_data.py
Fetches full Bitcoin price history:
- CryptoCompare (2010 -> 1 year ago): full history, paginated, API key required
- CoinGecko (last 365 days): recent data, Demo API key
Stitches both into btc_data.json for the dashboard.
"""

import json
import os
import sys
import time
import requests
from datetime import datetime, timezone, timedelta

CC_API_KEY  = os.environ.get("CRYPTOCOMPARE_API_KEY", "")
CG_API_KEY  = os.environ.get("COINGECKO_API_KEY", "")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "btc_data.json")

CC_BASE = "https://min-api.cryptocompare.com/data/v2/histoday"
CG_BASE = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
LIMIT   = 2000


def ts_to_date(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def fetch_cryptocompare():
    """Fetch full history from CryptoCompare, paginated back to 2010."""
    if not CC_API_KEY:
        print("  WARNING: No CRYPTOCOMPARE_API_KEY — skipping historical fetch.")
        return {}

    print("  Fetching from CryptoCompare (2010 -> ~1 year ago)...")
    rows = {}
    to_ts = int((datetime.now(timezone.utc) - timedelta(days=366)).timestamp())
    call = 0

    while True:
        call += 1
        url = f"{CC_BASE}?fsym=BTC&tsym=USD&limit={LIMIT}&toTs={to_ts}"
        resp = requests.get(url, headers={"authorization": f"Apikey {CC_API_KEY}"}, timeout=60)
        if resp.status_code != 200:
            print(f"  ERROR: CryptoCompare HTTP {resp.status_code}: {resp.text[:200]}")
            break
        data = resp.json()
        if data.get("Response") == "Error":
            print(f"  ERROR: {data.get('Message')}")
            break

        batch = [r for r in data["Data"]["Data"] if r.get("close", 0) > 0]
        if not batch:
            break

        for r in batch:
            date = ts_to_date(r["time"])
            rows[date] = {"time": r["time"], "close": r["close"]}

        earliest = batch[0]["time"]
        print(f"    Call {call}: {len(batch)} rows, earliest {ts_to_date(earliest)}")

        if datetime.fromtimestamp(earliest, tz=timezone.utc).year <= 2010:
            break
        to_ts = earliest - 1
        time.sleep(0.3)

    print(f"  CryptoCompare: {len(rows)} rows fetched.")
    return rows


def fetch_coingecko():
    """Fetch last 365 days from CoinGecko."""
    if not CG_API_KEY:
        print("  WARNING: No COINGECKO_API_KEY — skipping recent fetch.")
        return {}

    print("  Fetching from CoinGecko (last 365 days)...")
    resp = requests.get(
        CG_BASE,
        params={"vs_currency": "usd", "days": "365", "interval": "daily"},
        headers={"x-cg-demo-api-key": CG_API_KEY},
        timeout=60,
    )
    if resp.status_code != 200:
        print(f"  ERROR: CoinGecko HTTP {resp.status_code}: {resp.text[:200]}")
        return {}

    data = resp.json()
    rows = {}
    for ts_ms, price in data.get("prices", []):
        if price > 0:
            date = ts_to_date(int(ts_ms / 1000))
            rows[date] = {"time": int(ts_ms / 1000), "close": price}

    print(f"  CoinGecko: {len(rows)} rows fetched.")
    return rows


def main():
    print(f"\nFetching BTC price data...")

    # Fetch from both sources
    cc_rows = fetch_cryptocompare()
    cg_rows = fetch_coingecko()

    # Merge — CoinGecko takes priority for recent dates (more accurate)
    merged = {**cc_rows, **cg_rows}

    if not merged:
        print("ERROR: No data fetched from either source.")
        sys.exit(1)

    # Sort by date
    rows = sorted(merged.values(), key=lambda r: r["time"])

    output = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "sources": "CryptoCompare (historical) + CoinGecko (recent 365 days)",
        "rows": rows,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, separators=(",", ":"))

    first = rows[0]
    last  = rows[-1]
    print(f"\nSaved {len(rows)} rows -> btc_data.json")
    print(f"Range: {ts_to_date(first['time'])} (${first['close']:,.2f}) -> {ts_to_date(last['time'])} (${last['close']:,.2f})")


if __name__ == "__main__":
    main()
