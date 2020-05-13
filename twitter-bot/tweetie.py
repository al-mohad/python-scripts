# pip3 install tweepy
import tweepy
import time

auth = tweepy.OAuthHandler('yourAuthKey')
auth.set_access_token('youAccessToken')

api = tweepy.API(auth)
user = api.me()

search_string = 'python'
numbersOfTweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
    # ------------------------------------ #
    # Generous Bot --

    # def limit_handler(cursor):
    #     try:
    #         while True:
    #             yield cursor.next()
    #     except tweepy.RateError:
    #         time.sleep(300)

    # for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    #     if follower.name == 'almohad':
    #         follower.follow()
    #         break
    #     print(follower.name)
