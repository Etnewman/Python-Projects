AUTHOR: Ethan T. Newman
Version: 
Date:



Functions:
	1. AuthBot ->
			The authentication class. This class takes care of the handshake between the Python code and my Twitter account: @EthanTheDev1.
			It has as local variables the valid authentication tokens and one method. This method uses those variables to initalize a Tweepy API
			method.
	2. FollowBot ->
			The follow class. This class takes in one initial variable, the API Authentication. This class handles all things regarding to following/unfollowing.
	3. BlockBot ->
			The block class. This class takes in one initial variable, the API Authentication. This class handles all things regarding blocking/unblocking.


Plans:
	1. TweetBot ->
			This class will handle tweeting messages, main function.
	2. SearchBot ->
			This class will handle searches, not a main function.
	3. StreamBot ->
			This class will handle streaming, main function.
	4. MessagingBot ->
			This class will handle direct messaging, main function.
	5. TrendBot ->
			This class will handle trending posts, main function.
	6. TimelineBot ->
			This class will handle timeline related functions, main functions.