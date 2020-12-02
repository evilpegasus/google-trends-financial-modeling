## Data Collection and Processing
We sourced our alternative data from [Google Trends](https://trends.google.com/trends/?geo=US). Downloading data over a long time frame from the Google Trends website gives weekly datapoints with dates that are hard to control. To work around this, we used the third-party [pytrends](https://pypi.org/project/pytrends/) API for Python. This API allows us to request daily data for any time interval.

### Problems
Because the API is third-party, you will get 429 (too many requests) errors after about 3 years of daily data. We created a script that downloads and saves Google search trend data and ran it in a Kaggle Docker Container to save time.

Another problem is how the search volume values are computed by Google. Google samples a subset of its servers for the volume data. As a result, there are small variations between different requests with the same parameters. We determined that the difference was negligible to the overall trends although this could be looked into more thoroughly.

**Loading data here**

# EDA
Our downloaded Google Trends DataFrame looks like this.
```
word_trends["debt"].head()
```
We are primarily interested in the last column which gives the scaled search volume. The other columns are used to calculate the scaling.
