from pytrends import dailydata

"""
Makes requests for each word in words.txt
Run this on a server overnight
Takes about 9 hours before failing
"""

with open("words.txt") as f:
    words = f.readlines()
words = [x.strip() for x in words]
words = words[49]
print(words)
for word in words:
    try:
        dailydata.get_daily_data(word, 2010, 1, 2020, 11).to_csv(word + ".csv")
    except:
        pass