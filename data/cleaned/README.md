# Cleaned data

Output of `notebooks/01_data_cleaning.ipynb`:

- `MoviesOnStreamingPlatforms_Cleaned.csv` — 9,515 rows × 19 columns
- `TVShowsOnStreamingPlatforms_Cleaned.csv` — 5,368 rows × 19 columns

Cleaning applied: Rotten Tomatoes parsed to numeric (`98/100` → 98.0), age ratings
parsed to `Age_Min`, missing values imputed (median / mode), rows missing `Title`
or `Year` dropped, score and year ranges validated, duplicates checked.

Notebooks `02`–`04` read from this folder.
