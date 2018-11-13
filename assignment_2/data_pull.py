from twython import Twython
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

def pull_tweets(search, count=1000):
    """Pulls tweets for whatever string is placed inside the function"""
    TOKEN = '250817899-swqJ13ma87ENulvsYkKmgUuCjSj3mslYhLz4BIVM'
    TOKEN_SECRET = 'eRYHOHJuDZGspmXx07HLfIVq3TQWk4zfkutRfBc5DaDms'
    CONSUMER_KEY = 'uvDnCxP8wXu4JkVP6WfBEQBZ6'
    CONSUMER_SECRET = 'nBIpditFHIz86MUEY4ed9DEPX6tv4XfclAJ1cISeOCZsTmfb8F'
    t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
       TOKEN, TOKEN_SECRET)

    data = t.search(q=search, count=count)

    tweets = ''
    for status in data['statuses']:
        tweets = tweets + status['text']
    return tweets

def sentiment_table(search_list, hashtag=True):
    """Pulls the sentiment score for each item in the list and adds it into a table"""
    components = ['neg', 'neu', 'pos', 'compound']
    df = pd.DataFrame(index=search_list, columns=components)
    for team in search_list:
        if hashtag == True:
            tweets = pull_tweets('#'+team)
        else:
            tweets = pull_tweets(team)
        score = SentimentIntensityAnalyzer().polarity_scores(tweets)
        for x in components:
            df.loc[team][x] = score[x]
    return df

def print_sentiment_results(search_list, hashtag=True):
    results = sentiment_table(search_list, hashtag=hashtag)
    pprint(results)
    results.plot.bar()
    plt.show()

nfl_teams = ['Cardinals', 'Falcons', 'Ravens', 'Bills', 'Panthers', 'Bears', 'Bengals', 'Browns', 'Cowboys', 'Broncos',
             'Lions', 'Packers', 'Texans', 'Colts', 'Jaguars', 'Chiefs', 'Dolphins', 'Vikings', 'Patriots', 'Saints',
             'Giants', 'Jets', 'Raiders', 'Eagles', 'Steelers', 'Chargers', '49ers', 'Seahawks', 'Rams', 'Buccaneers',
             'Titans', 'Redskins']
nba_teams = ['Celtics', 'Nets', 'Knicks', '76ers', 'Raptors', 'Warriors', 'Clippers', 'Lakers', 'Suns', 'Kings', 'Bulls',
             'Cavaliers', 'Pistons', 'Pacers', 'Bucks', 'Mavericks', 'Rockets', 'Grizzlies', 'Hornets', 'Spurs', 'Hawks',
             'Bobcats', 'Heat', 'Magic', 'Wizards', 'Nuggets', 'Timberwolves', 'Thunder', 'Blazers', 'Jazz']
nhl_teams = ['Ducks', 'Coyotes', 'Flames', 'Blackhawks', 'Avalanche', 'Stars', 'Oilers', 'Kings', 'Wild', 'Predators',
             'Blues', 'Sharks', 'Canucks', 'GoldenKnights', 'Jets', 'Bruins', 'Sabres', 'Hurricanes', 'BlueJackets',
             'RedWings', 'Panthers', 'Canadiens', 'Devils', 'Islanders', 'Rangers', 'Senators', 'Flyers', 'Penguins',
             'Lightning', 'MapleLeafs', 'Capitals']
players = ['Lebron James', 'Sidney Crosby', 'Tom Brady', 'Steph Curry', 'Copper Kupp', 'Dez Bryant']


print_sentiment_results(nfl_teams)
print_sentiment_results(players, hashtag=False)