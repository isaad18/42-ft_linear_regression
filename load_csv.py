import pandas as pd


def parse_input(path: str) -> bool:
    """Validate that path is a non-empty string pointing to a .csv file."""
    if not isinstance(path, str):
        print("Error: path must be a string.")
        return False
    if not path.lower().endswith((".csv")):
        print("Error: only .csv files are supported.")
        return False
    return True


def load(path: str) -> pd.DataFrame:
    """Load a CSV file and print its dimensions. Returns DataFrame or None."""
    if not parse_input(path):
        return None
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None
    print(f"Loading dataset of dimensions {df.shape}")
    return df
