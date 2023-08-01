########################################
#   CREATING DICTIONARY TO STORE THE DATA WHICH WILL BE CONVERTED TO A DATAFRAME
########################################

#   NOTE: ALL THE POST DATA WILL BE SAVED IN A DIFFERENT

# SCRAPING CAN BE DONE VIA VARIOUS STRATEGIES {HOT,TOP,etc} we will go with keyword strategy i.e using search a keyword
######################################## 
#    Use 
#    pip install fire
#    pip install praw
#    python Reddit_Scraper.py --query [list of queries] -output_dir "path to output directory"
    
########################################

import fire
import os
import praw
import pandas as pd

def reddit_scraper(query : list,output_dir : str):

    client_id = os.environ.get("reddit_client_id")
    client_secret = os.environ.get("reddit_client_secret")
    user_agent = os.environ.get("user_agent")
    username = os.environ.get("username")
    password = os.environ.get("password")
    reddit = praw.Reddit(client_id = client_id,#my client id
                     client_secret = client_secret,  #your client secret
                     user_agent = user_agent, #user agent name
                     username = username,     # your reddit username
                     password = password)     # your reddit password

    sub = ['AskReddit'] 
    df = pd.DataFrame(columns=["title",
            "score" ,
            "id" ,
            "url" ,
            "comms_num",
            "created" ,
            "body"]) 
    for s in sub:
        subreddit = reddit.subreddit(s) 

        for item in query:
            post_dict = {
            "title" : [],
            "score" : [],
            "id" : [],
            "url" : [],
            "comms_num": [],
            "created" : [],
            "body" : []
            }
            
            for submission in subreddit.search(query,sort = "top",limit = 10):
                post_dict["title"].append(submission.title)
                post_dict["score"].append(submission.score)
                post_dict["id"].append(submission.id)
                post_dict["url"].append(submission.url)
                post_dict["comms_num"].append(submission.num_comments)
                post_dict["created"].append(submission.created)
                post_dict["body"].append(submission.selftext)

            post_data = pd.DataFrame(post_dict)
            df = pd.concat([df,post_data],axis=0,ignore_index=True)
    df.to_csv(os.path.join(output_dir,"subreddit.csv"))
    return

if __name__ == "__main__":
  fire.Fire(reddit_scraper)

