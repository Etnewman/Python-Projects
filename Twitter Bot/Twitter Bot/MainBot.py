import tweepy
import AuthBot
import FollowBot
import BlockBot

class MainBot():


    auth_bot = AuthBot.AuthBot()                                         #Init Authentication Bot
    api = auth_bot.Authenticate()                                        #Authenticates User

    follow_bot = FollowBot.FollowBot(api)                                #Init Follow Bot
    follow_bot.FollowAll('@j_aikens32', api)

    block_bot = BlockBot.BlockBot(api)
    block_bot.Block('@Nux_Taku', api)


