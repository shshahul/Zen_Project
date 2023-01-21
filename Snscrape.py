#Install Snscraper
#A Scraper for social network is called Snscraper
pip install snscrape
#To run Snscrape program need to import liberaries
#Importing Relevant Libraries
import pandas as pd
import snscrape.modules.twitter as sntwitter
# here if we want limits of tweets we need to set the limit
limit =100
#I am giving a empty list where i can store/add the tweets
tweets_list=[]
#i am using for loop to extract tweets
for tweet in sntwitter.TwitterSearchScraper("elonmusk").get_items():
#Next step i am using a if loop stating that my len of  tweet_list is equal to limit
    if len(tweets_list) == limit:
        break
    else:
        tweets_list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username,
                           tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])
#After adding the required attributes in tweet_list i am saving in a dataframe
df = pd.DataFrame(tweets_list, columns=["date","tweet id","tweetURL","tweet","userinfo","replaycount",
                                        "retweetCount","language","Source","LikeCount"])
print(df)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


#same code implementing with date picker##slecting until and since date##

import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient
content=input("enter user: ")
start =input("enter from wich month: ")
to = input("enter till what month: ")

query = f"'(from:{content}) until:{start} since:{to}'"
print(query)

tweets_py_list=[]

limit= 500

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets_py_list) == limit:
        break
    else:
        tweets_py_list.append([tweet.date, tweet.user.username,tweet.content])
    
df = pd.DataFrame(tweets_py_list, columns=['Date','User','Content'])
print(df)

#The collected dataset need to be stored in mongodb
#To store the data collection need to import important liberaries
#from pymongo import MongoClient
client = MongoClient("Give your mongoDB client")
client.list_database_names()
#Convert the dataframe to CSV file
df.to_csv('df.csv',index=False)
#create the data base and collection
db = client.Tweets_database
collection = db.tweets_collection
#coverting my data in to dict format
tweet_data = df.to_dict("records")
collection.insert_many(tweet_data)
data = collection.find({
    'tweet id': 1614939279683358720})
for i in data:
    print(i)
    break



