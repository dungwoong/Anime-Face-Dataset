# Pinterest Scraper
The original goal of this script was to assemble an anime face dataset from Pinterest.

I was inspired by the sheer lack of quality of existing datasets, to create my own script to scrape Pinterest.

Due to copyright issues, I probably shouldn't release the dataset, but the scraping scripts will be made available here.

## Sample Images from the dataset:
<p align="center">
<img src="images.jpg" width="600" height="600" />
<\p>

The dataset is no longer available, only the scripts will be provided.

## Sample usage
```
> python geturls --iters 200 --outfile links.csv --url https://www.pinterest.ca/kasumi_maeko/anime-icons/
> python downloadpins --csv links.csv --outfolder imgs
```

## The original dataset
The original data was assembled by scraping anime icon boards. Anime icon boards have cropped head shots of anime characters, although they may be filtered/given other effects

## Data sources

https://www.pinterest.ca/aweyourecute/anime-icons/

https://www.pinterest.ca/kasumi_maeko/anime-icons/
