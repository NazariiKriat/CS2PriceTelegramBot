import pandas as pd
from pathlib import Path

INPUT_DIR = Path("C:\Users\nazar\Desktop\Programming\TgBot\Gloves.csv")
OUTPUT_DIR = INPUT_DIR / "cleaned"
OUTPUT_DIR.mkdir(exist_ok=True)

PRICE_COLUMNS = [
    "Min_Price",
    "Max_Price",
    
]

for csv_file in INPUT_DIR.glob("*.csv"):
    try:
        df = pd.read_csv(csv_file)

        # чистим цены
        for col in PRICE_COLUMNS:
            if col in df.columns:
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.replace("$", "", regex=False)
                    .str.replace(",", "", regex=False)
                    .astype(float)
                )

        # ❗ удаляем полные дубликаты
        before = len(df)
        df = df.drop_duplicates()
        after = len(df)

        output_file = OUTPUT_DIR / csv_file.name
        df.to_csv(output_file, index=False)

        print(f"✔ {csv_file.name}: removed {before - after} duplicates")

    except Exception as e:
        print(f"❌ error in {csv_file.name}: {e}")
