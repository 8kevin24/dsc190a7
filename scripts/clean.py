import pandas as pd

VALID_EVENTS = {"click", "view", "purchase"}

df = pd.read_csv("data/raw/events.csv")

df = df.dropna()

df = df[df["event_type"].isin(VALID_EVENTS)]

df["duration_seconds"] = pd.to_numeric(
    df["duration_seconds"],
    errors="coerce"
)

df = df[df["duration_seconds"] > 0]

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

df = df.dropna(subset=["timestamp"])

df["timestamp"] = df["timestamp"].dt.strftime(
    "%Y-%m-%dT%H:%M:%S"
)

df.to_csv("data/clean/events.csv", index=False)