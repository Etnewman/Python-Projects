
import tweepy
import configparser


#AUTHENTICATION
class AuthBot:

    config = configparser.ConfigParser()
    config.read('mypy.ini')

    consumer_token = str(config['Secret']['consumer_token'])
    consumer_secret = str(config['Secret']['consumer_secret'])
    access_token = str(config['Secret']['access_token'])
    access_secret = str(config['Secret']['access_secret'])             #Access Tokens


    def Authenticate(self):
        auth = tweepy.OAuthHandler(self.consumer_token, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        api = tweepy.API(auth)
        return api
    