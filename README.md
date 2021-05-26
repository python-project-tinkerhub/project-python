# Twitter Assist

A django application which helps you to save twitter threads.You can save some valuable twitter tweets by mentioning a bot name inside the tweet using your twitter account. With the help of twiteer API these mentioned tweets can be downloaded from the Dashboard.To try out visit (http://18.220.159.14)

## Team Id

BFH/receQLwqYEjVRwpEI/2021

## Team members

1. [Achyuth Mohan](https://github.com/AchyuthMohan)
2. [Adithya Kartha](https://github.com/adithyakartha)
3. [Athul Reji](https://github.com/athulreji)

## How it Works ?

### For users:
  1.  For using the web application you must have a twitter account
  1.  You can create an account through the provided link, where you will be giving your name, email id, twitter id etc.
  2.  Then you must login from the index page using username and password which was created initially. This will take you to dashboard.
  3.  Here you will be provided with a bot name. The thing you should do is just mention this bot name in your tweets which must be saved.
  4.  After giving all your tweets you can click the 'pull tweet list' button which is provided in the dashboard.
  5.  That's all now you will receive all your tweets as a text file.

### For Developers:
  1.  The program tracks the tweets of user by using Twitter API and Tweepy. You should have a Twitter Developer account to access the API.
  2.  When the user creates an account in the website using twitter id and other details it will be saved in the DB.
  3.  When the user log in into the dashboard, the progrram collects the tweets from user using the API.
  4.  When the user clicks the download button the program writes the current tweets in a text file and this text file will be made available for the user to download.
  5.  The python file containing API keys are 'ignored' for security issues in GitHub repo. A security_keys.py file with api keys must be added to twitter_assist/mainappp directory.
   
   
