# Google Trends Financial Modeling
## Ming Fong and Alexander Yang
STAT 198 Quantitative Finance

Fall 2020

## Introduction

We implement a trading strategy for an index (NASDAQ) based on moving averages of changes in Google Trend data for certain selected keywords.

The notebook can be found in `Presentation Notebook.ipynb`

## Alternative Data
We will use Google Trends search volume data to make predictions about the movements of an index.

Data is downloaded through the [Pytrends](https://pypi.org/project/pytrends/) module using the Google Trends API.

Financial data is from [yfinance](https://pypi.org/project/yfinance/)

Backtesting is done using the [Backtesting.py](https://kernc.github.io/backtesting.py/) package

## Resources
Paper to implement: https://www.researchgate.net/publication/326503702_Algorithmic_Trading_Systems_Based_on_Google_Trends

https://jackdry.com/predicting-realized-volatility-using-google-trends
