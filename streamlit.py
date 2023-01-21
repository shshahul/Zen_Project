import streamlit as st
import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient

st.header("Twitter Analysis")
with st.form(key="Twitter_Analysis"):
    Content = st.text_input("Enter the search term: ")

    until_date = st.text_input("enter Until date: ")

    Since_date = st.text_input("enter since date: ")

    query = f'"(from:{Content}) until:{until_date} since:{Since_date}"'

    limit = st.slider("How many tweets dp you want to get?",0,1000)

    submit_button = st.form_submit_button(label='search')

    # search = print(query)

    tweets_list = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets_list) == limit:
            break
        else:
            tweets_list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username,
                                tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])


    file_name = st.text_input("Name the CSV file to dowload before you search: ")
    df= pd.DataFrame(tweets_list,
                              columns=["date", "tweet id", "tweetURL", "tweet", "userinfo", "replaycount",
                                       "retweetCount", "language", "Source", "LikeCount"])
    search = print(df)
    st.dataframe(df)


st.download_button("Download CSV",
                       df.to_csv(),
                       file_name = f'{file_name}',
                       mime="text/csv")

with st.form(key="Updating_Tweets_in_to_DataBase"):
    if st.form_submit_button(label='Update'):
        client = MongoClient('usernae:password')
        db = client.Tweets_database
        collection = db.twitter_collection
        tweet_data = df.to_dict("records")


        Update = collection.insert_many(tweet_data)

















