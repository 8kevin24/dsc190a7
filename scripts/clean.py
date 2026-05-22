import pandas as pd

VALID_EVENTS = {
    "click",
    "view",
    "purchase",
    "login",
    "logout"
}

df = pd.read_csv("./data/raw/events.csv")

df = df.dropna()

df["event_type"] = df["event_type"].str.strip().str.lower()

df = df[df["event_type"].isin(VALID_EVENTS)]

df["duration_seconds"] = pd.to_numeric(
    df["duration_seconds"],
    errors="coerce"
)

df = df[df["duration_seconds"] > 0]

df["duration_seconds"] = df["duration_seconds"].astype(int)

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

df = df.dropna(subset=["timestamp"])

df["timestamp"] = df["timestamp"].dt.strftime(
    "%Y-%m-%dT%H:%M:%S"
)

df["date"] = df["timestamp"].str[:10]

df["duration_minutes"] = (
    df["duration_seconds"] / 60
)

df["weekday"] = pd.to_datetime(
    df["date"]
).dt.day_name()

df = df.dropna()

df.to_csv(
    "./data/features/events.csv",
    index=False
)