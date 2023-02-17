import urllib
import requests
import pandas as pd
import time
import argparse
import sys

def run(dfpath, newfolder):
    df = pd.read_csv(dfpath)

    links = df.loc[:5, "Link"]

    for idx in df.index:
        row = df.iloc[idx, :]
        link = row["Link"]
        if "236x" not in link:
            print(f"SKIPPING {link}")
            continue
        link = link.replace("236x", "564x")
        
        if not pd.isnull(row["ImagePath"]):
            print(f"ALREADY DONE {link}")    
            continue
        print(f"retrieving {link}")
        num = "{:06d}".format(idx)
        fpath = f"{newfolder}/{num}.jpg"
        print(fpath)
        urllib.request.urlretrieve(link,fpath)
        df.loc[idx, "ImagePath"] = fpath
        df.to_csv(dfpath, index=False)
        time.sleep(1)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--outfolder",
        type=str,
        required=True,
        help="output folder path")
    parser.add_argument(
        "--csv",
        type=int,
        required=True,
        help="csv with columns Link and ImagePath")
    args = parser.parse_args()
    run(args.csv, args.outfolder)
	