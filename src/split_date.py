#!/usr/bin/env python3

from os import sep
import pandas as pd
import numpy as np


def split_date():
    df1 = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df =df1.dropna(how="all").dropna(axis=1, how="all")
    df[["Weekday","Day","Month","Year","Hour"]]=df["Päivämäärä"].str.split(expand=True)
    df.drop("Päivämäärä", inplace=True, axis=1)
    df["Weekday"] = (df["Weekday"].replace({"ma": "Mon", "ti": "Tue", "ke" : "Wed", "to": "Thu", "pe":"Fri", "la":"Sat", "su":"Sun"}))
    df["Month"]=df["Month"].replace({ "tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12 })
    df["Hour"] = df["Hour"].str.split(":", expand=True)[0]
    print(df["Hour"])
    df[["Day","Month","Year","Hour"]]= df[["Day","Month","Year","Hour"]].map(int)
    return df[["Weekday","Day","Month","Year","Hour"]]

def main():
    split_date()
       
if __name__ == "__main__":
    main()
