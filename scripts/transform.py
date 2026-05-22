import pandas as pd
import os
os.makedirs("data/transformed", exist_ok=True)

df = pd.read_csv("data/clean/events.csv")

df["date"] = pd.to_datetime(
    df["timestamp"]
).dt.strftime("%Y-%m-%d")

df.to_csv(
    "data/transformed/events.csv",
    index=False
)