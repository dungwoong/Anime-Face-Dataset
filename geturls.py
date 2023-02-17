import os
import argparse
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

from lxml import html
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


chrome_options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')

url = "https://www.pinterest.ca/kasumi_maeko/anime-icons/"

driver = webdriver.Chrome('chromedriver', options=chrome_options)

# this may change but yeah.
classe = "hCL kVc L4E MIw"
xpath_str = f"""//img[@class='{classe}']/@src"""

def run(iters, target_file, url=url):
    links = set()
    driver.get(url)
    for i in range(0, iters):
        source = driver.page_source
        tree = html.fromstring(source)
        new = tree.xpath(xpath_str)
        for item in new:
            links.add(item)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        print(f"iter {i+1} / {iters}: {len(links)} items")
        df = pd.DataFrame({"Link": list(links)})
        df.to_csv(target_file, index=False)
        time.sleep(3)

    print(f"writing {len(links)} items to {target_file}")
    df = pd.DataFrame({"Link": list(links)})
    df.to_csv(target_file, index=False)
            
    driver.quit()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--outfile",
        type=str,
        required=True,
        help="output file")
    parser.add_argument(
        "--iters",
        type=int,
        required=True,
        help="number of iters")
    parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="input url")
    args = parser.parse_args()
    run(args.iters, args.outfile, args.url)