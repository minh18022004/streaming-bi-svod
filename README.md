# Streaming Platform Strategy Analysis — Prime Video

## Project Overview
This project analyzes the content strategy of major streaming platforms (Netflix, Hulu, Prime Video, Disney+) using publicly available datasets, and develops a data-driven strategic recommendation for **Amazon Prime Video**. Catalog analytics from the Kaggle streaming dataset are combined with current market data (Nielsen's The Gauge, Amazon disclosures) to ground the recommendation in the 2026 streaming market.

Completed as the capstone for the **Open Avenues Build Fellowship — Streaming Video on Demand BI** project (Instructor: Yucheng Jiang).

## Objective
Identify a strategic growth opportunity for Prime Video, supported by exploratory data analysis, cross-platform comparison, and a SWOT assessment — and estimate its expected business impact.

## Dataset
**Movies and TV Shows on Streaming Platforms** (Kaggle):
- `MoviesOnStreamingPlatforms.csv` — 9,515 movies × 19 columns
- `TVShowsOnStreamingPlatforms.csv` — 5,368 TV shows × 19 columns

Key fields: `Title`, `Year`, `Age`, `IMDb`, `Rotten Tomatoes`, and platform availability indicators (`Netflix`, `Hulu`, `Prime Video`, `Disney+`). After cleaning and reshaping to one row per title-platform pair, the unified analysis table contains **15,551 rows**.

Market context data: Nielsen's The Gauge™ (Dec 2025), Amazon Prime Video advertising disclosures (2024–2025), and trade-press reporting.

## Methodology
1. **Data Cleaning** — handle missing values, parse Rotten Tomatoes scores (`98/100` → 98.0) and age ratings, validate score/year ranges, remove duplicates
2. **Exploratory Data Analysis** — profiling, descriptive statistics, distribution and trend charts for movies and TV shows
3. **Platform Comparison** — reshape to long format, pivot tables and charts comparing catalog volume, movie/TV mix, genre composition, release-year patterns, and score distributions across the four platforms
4. **Strategic Recommendation** — SWOT synthesis and an impact model estimating the revenue effect of the recommended strategy

## Key Findings
- **Prime Video has the largest catalog** in the dataset: 5,944 titles (4,113 movies + 1,831 TV shows), ahead of Netflix (5,666), Hulu (2,668), and Disney+ (1,273)
- **Prime Video skews toward movies** (~69% of its catalog), while Netflix and Hulu are more balanced between movies and TV
- **Prime Video's catalog reaches deepest into the back-catalog** — meaningful title counts back to the 1950s, versus Netflix's concentration in post-2015 releases
- **Quality perception gap**: Prime Video has the lowest average Rotten Tomatoes scores of the four platforms (≈50 for movies, ≈38 for TV, vs. Netflix's ≈54 for both) — breadth comes at the cost of average quality
- **Market context**: streaming hit a record 47.5% of U.S. TV viewing in Dec 2025 (Nielsen); Prime Video reached a platform-record 4.3% share, driven by Thursday Night Football and *Fallout*, and built the largest ad-supported audience in premium streaming (315M monthly viewers)
- **Recommendation**: program the new NBA/WNBA rights as a weekly appointment to convert event-driven viewers into habitual viewers monetized by ads — estimated at **$230M+/yr** in incremental revenue before ad-revenue upside

Full write-up in [`insights.md`](insights.md); final deck in [`presentation/final_slides.pptx`](presentation/final_slides.pptx).

## Repository Structure
```
Streaming-BI-Project
│
├── data/
│   ├── raw/                  # original Kaggle CSVs (input to cleaning)
│   └── cleaned/              # cleaned datasets produced by 01_data_cleaning.ipynb
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb        # ETL: missing data, parsing, validation
│   ├── 02_exploratory_analysis.ipynb # EDA: profiling, stats, trend charts
│   ├── 03_platform_analysis.ipynb    # single-platform content identity (Prime Video)
│   └── 04_market_comparison.ipynb    # multi-platform pivots, charts, positioning
│
├── visuals/                  # exported charts from the notebooks
├── presentation/
│   └── final_slides.pptx     # final presentation deck
│
├── insights.md               # written insights & strategic recommendation
└── README.md
```

## How to Run
1. Download the Kaggle dataset and place `MoviesOnStreamingPlatforms.csv` and `TVShowsOnStreamingPlatforms.csv` in `data/raw/`
2. Run `notebooks/01_data_cleaning.ipynb` — this writes the cleaned CSVs to `data/cleaned/`
3. Run notebooks `02`–`04` in order (each reads from `data/cleaned/`)

## Tools Used
Python (pandas, NumPy), Matplotlib, Jupyter Notebook, Git/GitHub
