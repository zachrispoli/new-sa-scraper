# Skillattack Scraper

### Install

You'll need [Python 3](https://www.python.org/downloads/) (any version of 3 will work)

### How To Use

**First, run the scraper:**

```
python3 scraper.py
```

This will download the songlist and every page for each song. It is throttled for ten seconds between each request to avoid excessive bandwidth use on skillattack.

There are ~1000 songs so this will take about three hours total.

**Next, run the parser:**

```
python3 parse.py
```

This will parse all the data downloaded using `scraper.py`. 

This part's not done yet but it will probably spit out a big CSV or something.
