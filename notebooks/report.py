import marimo

app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    return pd, plt


@app.cell
def _(pd):
    df = pd.read_csv(
        "data/features/events.csv"
    )
    return df


@app.cell
def _(df, plt):
    plt.hist(df["duration_minutes"])
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Count")
    plt.title("Event Duration Distribution")
    plt.show()


if __name__ == "__main__":
    app.run()