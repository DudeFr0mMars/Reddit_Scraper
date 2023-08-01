import fire
import os
import praw
import pandas as pd
from datetime import date

def run(query: list, dirout: str, subreddits=None):

    client_id     = "KqVbVrlmGdbowtjuNIMAmQ" 
    client_secret = "XN4XRE7_pOw9rzreelTFYogmBTWW_g" 
    user_agent    = "DailyNews"  ### Same from Secret page
    reddit = praw.Reddit(
        client_id=client_id,  # my client id
        client_secret=client_secret,  # your client secret
        user_agent=user_agent,  # user agent name
    )

    if subreddits is None:
        subreddits = [
            "MachineLearning",
            "OpenAI",
            "ChatGPT",
            "OpenAIDev",
            "learnmachinelearning",
        ]

    #ymd = date.today()    
    #ymd = ymd.strftime("%d/%m/%Y")
    
    print("########## Start Scraping")
    
    dfall = pd.DataFrame() 
    for s in subreddits:
        subreddit = reddit.subreddit(s) 
        print("fetching:", s)

        for item in query:
            ddict = {
                "title": [],
                "score": [],
                "id": [],
                "url": [],
                "comms_num": [],
                "created": [],
                "body": [],
             }
            
            for submi in subreddit.search(query, sort="hot", limit=10):
                ddict["title"].append(submi.title)
                ddict["score"].append(submi.score)
                ddict["id"].append(submi.id)
                ddict["url"].append(submi.url)
                ddict["comms_num"].append(submi.num_comments)
                ddict["created"].append(submi.created)
                ddict["body"].append(submi.selftext)

            dfres = pd.DataFrame(ddict)
            print( f'{item}: N article: ', len(dfres))
            dfall = pd.concat([dfall,dfres], axis=0,ignore_index=True)
    filename = "fetch.csv"
    path = os.path.join(dirout,filename)
    dfall.to_csv(path)
    return

if __name__ == "__main__":
  fire.Fire(run)
