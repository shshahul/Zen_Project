# Zen_Project
**snscrape**

snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.

**I am going to use  on twitter:**
Twitter: users, user profiles, hashtags, searches, tweets (single or surrounding thread), list posts, and trends


**streamlit-twitter-scraper**

**Requirements**

snscrape requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install snscrape.

. Snscrape

. Streamlit

. pandas

**Installation**

 #Install Snscraper
 
#A Scraper for social network is called Snscraper

pip install snscrape

 '#Now creating a GUI using streamlit'
'#install streamlit libreray'

pip install streamlit

**#Import Requirements**

 import streamlit as st
 
 import snscrape.modules.twitter as sntwitter
 
 import pandas pd
 
 **using the following query format**
 
 The query must be specified as a Python dictionary containing a list of fields
 
 
 (from:{Content}) until:{until_date} since:{Since_date}
 
 **until**
 
This parameter refers to the maximum allowed date. It has to be specified in the YYYY-MM-DD format.

**since**

This parameter refers to the minimum allowed date. It has to be specified in the YYYY-MM-DD format.
  
