import tweepy
import time

class FollowBot():
    
    def __init__(self, api):
        self.api = api                          #init

    def GetCheckFollow(self, ID, api):
        return api.exists_friendship            #Returns boolean of if user 

    def LimitHandled(self, cursor):
        i=0
        while True:
            try:
                yield next(cursor)

            except tweepy.RateLimitError:
                print('Sleeping, 15 Minutes remain.')
                time.sleep(5*60)
                print('Sleeping, 10 Minutes remain.')
                time.sleep(5*60)
                print('Sleeping, 5 Minutes remain.')
                time.sleep(4*60)
                print('Sleeping, 1 Minute remains.')
                time.sleep(60)          #Handles Twitter Follow Limit.

    def FollowAll(self, ID, api):
        i=0
        for follower in FollowBot.LimitHandled(self, tweepy.Cursor(api.followers, ID).items()):
            try:
                follower.follow()
                i=i+1
                print(str(i) + '. ' + follower.name)

            except tweepy.error.TweepError:
                pass            #Follow ALL Followers of a given user.

    def Follow(self, ID, api):
        print('Now following: ' + str(ID))
        api.create_friendship(ID)               #Follow a single user.

    def Unfollow(self, ID, api):
        print('Unfollowing: ' + str(ID))
        api.destroy_friendship(ID)             #Unfollow a single user.

    def ShowCheckFollow(self, ID, api):
        if (api.exists_friendship):
            print('Yes! You follow: ' + str(ID))
        else:
            print('No, You do not follow: ' + str(ID))      #Shows if authenticated user is following another user.

    def WhoIsFollowing(self, ID, api):     
        i=0
        print('Showing followers for: ' + str(ID))
        for follower in tweepy.Cursor(api.friends_ids, ID):
            i=i+1
            print(str(i) + '. ' + follower)       #Shows all followers of a given user.



