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

"""

Fetch secret from here:
https://www.reddit.com/prefs/apps/


pip install praw fire utilmy


export reddit_client='i05gtu1-NrbJqCxHFHxW3g'
export reddit_client_secret='Ak1qkvZdqnAfCCSK7rq9HcyBuaWoTQ'
export reddit_ua='Bot'
export reddit_subreddit='MachineLearning,OpenAI,ChatGPT,OpenAIDev,learnmachinelearning'


cd utilmy/webscrapper/

python cli_redditnews.py run --query 'icml 2023, neurips 2023'  --dirout ztnp/reddit/



"""
import fire, os, praw, pandas as pd
from datetime import date

def run(query:str, dirout:str, subreddits=None, reddit_limit=10, reddit_sort='top'):

    ### from https://www.reddit.com/prefs/apps/
    client_id     = "KqVbVrlmGdbowtjuNIMAmQ" 
    client_secret = "XN4XRE7_pOw9rzreelTFYogmBTWW_g" 
    user_agent    = "DailyNews" 
    reddit = praw.Reddit(client_id = client_id,#my client id
                     client_secret = client_secret,  #your client secret
                     user_agent    = user_agent #user agent name
                     )

    if subreddits is None :
        subreddits = ['MachineLearning','OpenAI','ChatGPT','OpenAIDev','learnmachinelearning']
        
    if isinstance(query, str):
        query = query.split(",")

    ymd = date.today()    
    ymd = ymd.strftime("%d/%m/%Y")
    
    print("########## Start Scrapping")
    
    dfall = pd.DataFrame() 
    for s in subreddits:
        subreddit = reddit.subreddit(s) 
        print('fetching:', s)

        for item in query:
            ddict = {
            "title" : [], "score" : [], "id" : [], "url" : [], "comms_num": [], "created" : [], "body" : []
            }
            
            for submi in subreddit.search(query,sort = reddit_sort,limit = reddit_limit):
                ddict["title"].append(submi.title)
                ddict["score"].append(submi.score)
                ddict["id"].append(submi.id)
                ddict["url"].append(submi.url)
                ddict["comms_num"].append(submi.num_comments)
                ddict["created"].append(submi.created)
                ddict["body"].append(submi.selftext)

            dfres = pd.DataFrame(ddict)
            log( f'{item}: N article: ', len(dfres))
            dfall = pd.concat([dfall,dfres], axis=0,ignore_index=True)
    filename = ymd + "-fetch.csv"
    path = os.path.join(dirout,filename)
    df.to_csv(path)
    return

if __name__ == "__main__":
  fire.Fire(run)
