# VERSION HISTORY — What If You Bought Bitcoin On Any Day Ever?
# File: btc-any-day-ever.html
# Repo: bitcoin-any-day-ever
# Project: Zenca / BuildThisNext / Promptcraft

---

## v2.1 — 6 Apr 2026 ✦ CURRENT

### Identity
- Dashboard title: What If You Bought Bitcoin On Any Day Ever?
- GitHub repo: bitcoin-any-day-ever (BuildThisNext)
- HTML `<title>`: What If You Bought Bitcoin On Any Day Ever?
- HTML filename: btc-any-day-ever.html
- H1 heading: What If You Bought Bitcoin On Any Day Ever?

### Layout
- Full-width header: headline + subtitle (left 50%), 12-metric stats grid (right 50%)
- Tab buttons in header-left, below subtitle
- Sidebar (28%) collapses to tab-buttons-only on tab 03
- Main content (72%): chart fills full height on tab 01, heatmap on tab 02, editorial prose on tab 03
- Sidebar label and title swap per active tab

### Stats (12 metrics, 4×3 grid)
- Row 1: Overall win rate, Days of history, Pairs evaluated, Current price
- Row 2: All-time high, Longest losing streak (with end date), Longest winning streak (with end date), Worst drawdown ever (with trough date)
- Row 3: Best 1-year return (with buy date), Worst 1-year return (with buy date), Worst-case break-even, Days at new ATH
- Group borders: green (row 1 cols 1–3), red (row 2 cols 1–3), blue (row 3 cols 1–3), orange left border (col 4)

### Chart (tab 01)
- 27 holding periods: 1D/2D/3D/4D/5D/6D / 1W/2W/3W/4W / 1M/2M/1Q/4M/5M/2Q/7M/8M/3Q/10M/11M / 1Y/2Y/3Y/4Y/5Y/6Y
- Color: 10 discrete shades — 5 orange (0–49%) dark→bright, 5 green (50–100%) dark→bright, split at 50%
- 2-row compact data table below chart (Wins / Outcomes), columns aligned to chart bars with trailing spacer
- 50% dashed reference line

### Heatmap (tab 02)
- Axis arrangement: B10-BL, B26-BR, S10-BR, S26-TR
- X-axis (bottom): buy date, 2010→2026 left→right
- Y-axis (right): sell date, 2010→2026 bottom→top
- Labels on all 4 sides: primary axes full opacity, mirrored axes dimmed
- Canvas at 50% CSS width; chart-wrap is inline-block to hug canvas tightly
- Hover tooltip: buy date, sell date, return %

### Tab 03 — The Takeaway
- Sidebar collapses to 120px (tab buttons only), all content hidden
- Full right panel: editorial prose in Inter weight 300, left-aligned, vertically centred
- Ends with open question: "What is the right time horizon for me to have to ensure that my Bitcoin holdings are going to be profitable?"

### Narrative
- Header subtitle: 3 lines with `<br>` breaks, middle line in quotes
- Tab 01 sidebar: "Time converts volatility into probability" + methodology para (dynamic) + "What this shows" + "The behavioural gap" — all with line breaks
- Tab 02 sidebar: title swaps to "Every buy date. Every sell date. Every outcome." — "Green/Red" coloured to match grid, "How to read this" line-by-line, "A note on the data" replacing "Methodology"
- "four years" → "three years" in What this shows
- Methodology paragraph: exact line breaks as specified, ends with "Did the price go up? / We counted the wins."

### Build history (v2.1 iteration steps, continuing from v2.0 iter 18)
- iter 19 — 12-metric grid rearranged by logical clusters with group border colours
- iter 20 — Heatmap: sell date axis moved to right side; all 4 sides labelled
- iter 21 — Heatmap: axis arrangement explored (B10-BL/B26-TL/S10-BL/S26-BR), reverted to B10-BL/B26-BR/S10-BR/S26-TR
- iter 22 — Heatmap: canvas reduced to 50% CSS width; chart-wrap changed to inline-block
- iter 23 — Tab 03: full-width editorial layout; sidebar collapses on tab 03; Inter weight 300 font
- iter 24 — Tab 03: sidebar all-content hidden (not just content-03 div); label/title swap per tab via switchTab
- iter 25 — All copy revisions: line breaks in methodology/behavioural gap, "four"→"three" years, green/red coloured in heatmap copy, "How to read this" line-by-line, "Methodology"→"A note on the data", tab 03 prose restructured with open question
- iter 26 — Subtitle middle line wrapped in quotes

---

## v2.0 — 4 Apr 2026

### Layout
- Full-width header: headline + subtitle + tabs (left 50%), 10-metric stats grid (right 50%)
- Permanent sidebar (28%): section title, insight boxes, tab navigation
- Main content area (72%): chart or heatmap fills full height per tab
- Three tabs: 01 Holding Period / 02 Every Outcome / 03 The Takeaway
- Sidebar content swaps per active tab
- Footer: Built by Zenca · BuildThisNext · Promptcraft

### Stats (12 metrics, 4×3 grid)
- Row 1: Overall win rate, Days of history, Pairs evaluated, Current price
- Row 2: All-time high, Longest losing streak, Longest winning streak, Worst drawdown ever
- Row 3: Best 1-year return, Worst 1-year return, Worst-case break-even, Days at new ATH
- All computed from loaded price data, no extra API calls

### Chart
- 27 holding periods: 1D/2D/3D/4D/5D/6D / 1W/2W/3W/4W / 1M/2M/1Q/4M/5M/2Q/7M/8M/3Q/10M/11M / 1Y/2Y/3Y/4Y/5Y/6Y
- Color: 10 discrete shades — 5 orange (0–49%) stepping dark→bright, 5 green (50–100%) stepping dark→bright
- 2-row compact data table below chart (Wins / Outcomes), columns aligned to chart bars
- 50% reference line (dashed)

### Heatmap
- X-axis: buy date (left→right, 2010→2026)
- Y-axis: sell date (bottom→top, 2010→2026)
- Weekly intervals using 7-day average close (no arbitrary day selection)
- Hover tooltip: buy date, sell date, return %

### Data
- Source: CryptoCompare `histoday` API, paginated, no API key required
- Full history from 2010-07-17 to today, fetched fresh on every page load
- ~5 paginated calls of 2,000 rows each, stitched and deduplicated

### Narrative
- Header: "Most people think about Bitcoin wrong."
- Tab 01 title: "Time converts volatility into probability"
- Tab 03: full takeaway narrative + key milestones table
- Methodology paragraph dynamically populated with live N, date range, and pairs count

### Build history (v2.0 iteration steps)
- iter 01 — Dark theme (#111111), corrected heatmap axis copy (above/below diagonal)
- iter 02 — Heatmap axis swap: X=buy date left→right, Y=sell date bottom→top
- iter 03 — Tooltip background fixed (white-on-white contrast bug)
- iter 04 — Weekly averaging: 7-day average close per bucket instead of arbitrary single day; transparency note added to copy
- iter 05 — Full narrative rewrite: header provocation, behavioural gap, "time converts volatility into probability", Section 03 conclusion
- iter 06 — Tabbed layout: 3 tabs replacing vertical scroll, two-column per tab
- iter 07 — Sidebar + full-width header layout rebuild (30% sidebar, 70% main)
- iter 08 — Layout correction: header spans full width (50/50), sidebar+main below header only
- iter 09 — Tab buttons moved into header-left; ATH "from here" → "from there"; line breaks in sidebar copy; trailing spacer column for table alignment; footer updated to Zenca · BuildThisNext · Promptcraft
- iter 10 — Subtitle line breaks restructured (3 lines, no extra spacing)
- iter 11 — 27-period chart sequence: 1D–6D, 1W–4W, 1M/2M/1Q/4M/5M/2Q/7M/8M/3Q/10M/11M, 1Y–6Y
- iter 12 — Color: opacity-scaled two-color system (50% split, opacity by distance from 50%)
- iter 13 — Color: solid RGB interpolation through dark neutral midpoint (opacity removed)
- iter 14 — Color: HSL interpolation orange→yellow→green (too neon, reverted)
- iter 15 — Color: amber midpoint RGB interpolation (too dull/muddy)
- iter 16 — Color: 10 discrete shades, 5 orange + 5 green, stepped every 10% (current)
- iter 17 — 10 metrics in 5×2 grid: added longest losing streak, best/worst 1-year return, worst-case break-even, days at new ATH
- iter 18 — 12 metrics in 4×3 grid: added longest winning streak (with end date), worst drawdown ever (with trough date); losing streak also updated with end date

---

## v1.0 — 4 Apr 2026

### First complete working version
- Dark theme (#111111 background)
- Single-page vertical scroll layout
- Probability curve (7 holding periods, bar chart)
- Heatmap (weekly sampling, hover tooltip)
- Full narrative: header, section intros, insight boxes, conclusion
- 4-metric stat strip: win rate, days, pairs, current price
- Data: CryptoCompare, paginated, no key
- Loading screen with progress bar
- Footer: BuildThisNext · Promptcraft
