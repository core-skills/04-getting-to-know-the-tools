import pandas as pd
from pathlib import Path

output_filename = "LondonAQ"

csvs = [i for i in Path("./").glob("*.csv") if not i.name.startswith(output_filename)]

df = pd.concat([pd.read_csv(csv_filepath) for csv_filepath in csvs]).reset_index(
    drop=True
)

df.to_csv((Path("./") / output_filename).with_suffix('.csv'), index=False)
)

# df = pd.read_csv('LondonAQ.csv')
# pd.read_csv("https://storage.googleapis.com/coreskillsdata2020/AQ/LondonAQ.csv")
