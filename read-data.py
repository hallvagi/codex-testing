import pandas as pd
import io


def load_csv_clean(path: str) -> pd.DataFrame:
    """Load a CSV that may be padded with NUL bytes."""
    with open(path, "rb") as f:
        content = f.read()

    # Remove leading NUL bytes to avoid corrupt column names
    content = content.lstrip(b"\x00")

    return pd.read_csv(io.BytesIO(content), sep=";")

def main():
    try:
        df = load_csv_clean("data/test.csv")
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(df.describe(include="all"))

if __name__ == '__main__':
    main()
