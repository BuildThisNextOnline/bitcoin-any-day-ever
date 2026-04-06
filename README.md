# What If You Bought Bitcoin On Any Day Ever?

**Live dashboard → [buildthisnext.github.io/bitcoin-any-day-ever](https://buildthisnext.github.io/bitcoin-any-day-ever)**

Built by [Zenca](https://zenca.global) · [BuildThisNext](https://buildthisnext.substack.com) · [Promptcraft](https://promptcraftai.substack.com)

---

## What is this?

A data-driven dashboard that answers a simple but powerful question:

> Across Bitcoin's entire recorded history, how often would you have come out ahead — if you simply bought and held?

We calculated **every possible buy/sell pair** across every day Bitcoin has ever traded. For each pair, one question: did the price go up? We counted the wins.

---

## What's inside

### 01 — Holding Period
A bar chart showing the probability of profit for 27 holding periods, from 1 day to 6 years. Each bar answers: *"If you bought on any random day in history and held for exactly this long, what fraction of the time would you have been in profit?"*

The 50% dashed line marks the coin-flip threshold. Everything above it means the odds favoured you. Watch how quickly the bars climb as the holding period extends.

### 02 — Every Outcome
A heatmap of every possible buy/sell combination across Bitcoin's history. Each cell is a unique outcome — a week you could have bought paired with a later week you could have sold. Green = profit. Red = loss.

- X-axis (bottom): buy date, 2010 → 2026
- Y-axis (right): sell date, 2010 → 2026
- Hover any cell to see exact dates, prices, and return

### 03 — The Takeaway
The narrative behind the numbers. Why most people get Bitcoin wrong, and the only question that actually matters.

---

## Key stats (live, updated on every page load)

| Metric | Description |
|---|---|
| Overall win rate | % of all buy/sell pairs that resulted in profit |
| Days of history | Total trading days in the dataset |
| Pairs evaluated | Total buy/sell combinations calculated |
| Current price | Live BTC/USD price |
| All-time high | Peak price and % below current |
| Longest losing streak | Max consecutive down days |
| Longest winning streak | Max consecutive up days |
| Worst drawdown ever | Peak-to-trough decline and date |
| Best 1-year return | Highest 365-day gain and entry date |
| Worst 1-year return | Worst 365-day loss and entry date |
| Worst-case break-even | Longest time to recover from any buy |
| Days at new ATH | % of all days that set a new all-time high |

---

## How it works

- **Data source:** [CryptoCompare](https://cryptocompare.com) `histoday` API — no API key required, no cost
- **Coverage:** 2010-07-17 to today, fetched fresh on every page load
- **Computation:** All metrics computed in-browser in JavaScript — no backend, no server
- **Hosting:** GitHub Pages — static HTML, loads anywhere

---

## Files

| File | Description |
|---|---|
| `index.html` | The dashboard (auto-generated copy of btc-any-day-ever.html) |
| `btc-any-day-ever.html` | Source file |
| `VERSION_HISTORY.md` | Full version and build history |

---

## Version

**v2.1** — See [VERSION_HISTORY.md](VERSION_HISTORY.md) for full changelog.
