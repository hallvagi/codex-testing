import pandas as pd

def main():
    try:
        df = pd.read_csv('test.csv')
    except Exception as e:
        print(f'Error reading CSV: {e}')
        return
    print(df.describe(include='all'))

if __name__ == '__main__':
    main()
