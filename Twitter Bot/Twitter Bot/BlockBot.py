import tweepy
import time

class BlockBot():
    
    def __init__(self, api):
        self.api = api

    def Block(self, ID, api):
        print('Are you sure you want to block: ' + str(ID) + '?')

        usr = str(input('Enter Y or N:'))
    
        if (usr == 'Y') or (usr == 'y'):
            #Some Code
        else:
            #Some Code


            