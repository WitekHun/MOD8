import pandas as pd
import numpy as np
import missingno as msno

# import xlsxwriter
# import lxml

if __name__ == "__main__":
    data = pd.read_html(
        "https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/",
        header=0,
    )
    data[0].columns = ["POZ", "TYTUŁ", "ARTYSTA", "ROK", "MAX POZ"]
    data[0].to_csv("Full.csv", index=True)
    n = data[0]["ARTYSTA"].nunique()
    print(f"Na liście znajduje się {n} pojedyńczych artystów")
    most_freq_art = pd.DataFrame(data[0].value_counts("ARTYSTA", normalize=False))
    # most_freq_art.columns = ["Count"]
    m = most_freq_art.max().iloc[0]
    top_art = most_freq_art.loc[most_freq_art["count"] == m]
    print(f"Najczęściej na liście pojawiają się:\n{top_art}")
    df = data[0].rename(str.title, axis=1).drop(["Max Poz"], axis=1)
    year_prod = df.groupby(df["Rok"]).Tytuł.agg(["count"])
    print(
        f"Najwięcej albumów na liście jest z:\n{year_prod[year_prod == year_prod.max()].dropna()}"
    )
    """
    left = df.groupby(["Artysta"]).agg({"Rok": "min"})
    left.to_csv("left.csv", index=True)
    pd.merge(left, df, how="inner", on="Artysta").sort_values(
        by="Rok_y"
    ).drop_duplicates(subset=["Artysta"]).to_csv("Album.csv", index=False)
    """
    df.sort_values(by="Rok").drop_duplicates(subset=["Artysta"]).drop(
        ["Poz"], axis=1
    ).to_csv("Albums.csv", index=False)
    youngest_album_year = df["Rok"].max()
    print(f"Najpóźniej wydany album na liście jest z roku {youngest_album_year}")
    # data_1960_1990 = df.query("1960<=Rok<=1990")["Poz"].nunique()
    data_1960_1990 = df[(df.Rok >= 1960) & (df.Rok <= 1990)]["Poz"].nunique()
    print(f"Na liście znajdują się {data_1960_1990} albumy wydane w latach 1960-1990")
