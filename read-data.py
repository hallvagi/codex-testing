import pandas as pd
import io
import os
import seaborn as sns
import matplotlib.pyplot as plt


def load_csv_clean(path: str) -> pd.DataFrame:
    """Load a CSV that may be padded with NUL bytes."""
    with open(path, "rb") as f:
        content = f.read()

    # Remove leading NUL bytes to avoid corrupt column names
    content = content.lstrip(b"\x00")

    return pd.read_csv(io.BytesIO(content), sep=";")


def plot_rentals_per_year(df: pd.DataFrame, output_path: str | None = None) -> None:
    """Display a histogram of the number of bike rentals per year.

    If ``output_path`` is provided, the plot will also be saved to that
    location as a PNG image. Necessary directories are created
    automatically.
    """
    sns.set_style("whitegrid")
    sns.countplot(x="year", data=df)
    plt.title("Bike Rentals per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Rentals")
    plt.tight_layout()
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path)
    plt.show()

def main():
    try:
        df = load_csv_clean("data/test.csv")
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(df.describe(include="all"))
    plot_rentals_per_year(df, "results/histogram.png")

if __name__ == '__main__':
    main()
