import pandas as pd
import os
os.makedirs("data/clean", exist_ok=True)

VALID_EVENT_TYPES = {
    "click",
    "view",
    "purchase",
    "login",
    "logout"
}

df = pd.read_csv("data/raw/events.csv")

# remove empty/whitespace-only cells
df = df.replace(r"^\s*$", pd.NA, regex=True)
df = df.dropna()

df["event_type"] = df["event_type"].str.strip().str.lower()
df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
df = df[df["duration_seconds"] > 0]
df["duration_seconds"] = df["duration_seconds"].astype(int)

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.dropna(subset=["timestamp"])

df.to_csv("data/clean/events.csv", index=False)