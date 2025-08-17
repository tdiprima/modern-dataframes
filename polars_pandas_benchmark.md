# 🚀 Benchmark Highlights (Polars vs Pandas)

## 📊 Graph 1: Speed (Higher = Better)

Polars is a speed demon compared to Pandas:

* 🔤 **Strings absolutely pop off** → **6.9x faster**
* 📂 **Loading CSVs** → **6.7x faster**
* 🔎 **Filtering** → **5.6x faster**
* ↕️ **Sorting** → **4.0x faster** (still solid)
* 👯 **GroupBy** → **3.6x faster**

👉 TL;DR: Every operation is way faster. Big W. ✅

---

## ⏱ Graph 2: Actual Time (Log Scale)

This one’s about real execution times, not just ratios:

* 📂 **Loading** → Pandas crawls at 1s, Polars zooms at \~0.15s
* 🔤 **Strings** → Polars blinks (ms), Pandas snoozes 😴
* 🔎 **Filtering** → Pandas struggles, Polars breezes through
* 👯/↕️ **GroupBy & Sorting** → not as dramatic, but still faster

👉 Polars is consistently *an order of magnitude* quicker.

---

## 🧠 Graph 3: Memory Usage

Here’s where it gets interesting:

* 📂 **Loading** → Polars uses a bit more (230MB vs 200MB)
* 🔎 **Filtering** → Polars wins on memory
* 👯 **GroupBy** → Polars eats more RAM (115MB vs 20MB) 🤷
* 🔤 **Strings** → Polars super memory-efficient
* ↕️ **Sorting** → basically the same

👉 Polars sometimes spends more RAM to go fast. Trade-off vibes.

---

## 🌈 Graph 4: Heatmap (Green = Good)

Quick visual summary:

* ✅ Lots of green → Polars dominates
* 🟥 Red pops up on **filtering + groupby memory** (Polars eats more there)
* 🔤 Strings are pure green → total Polars flex
* 📂 + ↕️ Still solid even with memory trade-offs

---

## 💡 Bottom Line

Polars = 🚀 **3.6–6.9x speedups** across the board.
Yeah, sometimes it hogs more memory, but the performance gains? **Totally worth it.**

<br>
