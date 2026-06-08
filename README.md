# Streaming BI Project (SVoD)

This repo contains analyses and materials for an 8-session BI project focused on the Streaming Video on Demand (SVoD) industry (Netflix, Hulu, Prime Video, Disney+).

## Structure
```
streaming-bi-template/
├─ notebooks/        # Jupyter notebooks
├─ data/             # Raw / interim data (excluded from git by default)
├─ src/              # Reusable helper functions
├─ figures/          # Exported charts
├─ requirements.txt  # Python dependencies
└─ README.md         # This file
```

## Quick Start
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
3. Open `notebooks/01_explore.ipynb` and run the first cell.

## Notes
- Keep large datasets out of git. Use `data/` (gitignored).
- Save charts to `figures/` for use in the presentation deck.
