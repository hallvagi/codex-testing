# codex-testing
Testing of OpenAI Codex.

The dataset file `test.csv` has been moved into the `data/` directory.

## Repository Files

The repo contains a simple Python script and sample dataset:

- **read-data.py** – reads `data/test.csv` with pandas and prints basic
  statistics.
- **data/test.csv** – bike rental dataset from Kaggle used for testing.

## dataset
https://www.kaggle.com/datasets/aguado/bike-rental-data-set-uci

## Dataset Columns
The `test.csv` file includes the following columns:

- **id** – unique identifier for each record
- **year** – year of the measurement
- **hour** – hour of the day (0–23)
- **season** – numeric code for the season
- **holiday** – whether the day was a holiday
- **workingday** – indicates a standard working day
- **weather** – weather situation code
- **temp** – recorded temperature in Celsius
- **atemp** – perceived or "feels-like" temperature
- **humidity** – relative humidity percentage
- **windspeed** – wind speed value
