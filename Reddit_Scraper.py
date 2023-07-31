import os
import praw
import pandas as pd

def reddit_scraper(query : list,output_dir : str):

    client_id = os.environ.get("reddit_client_id")
    client_secret = os.environ.get("reddit_client_secret")
    user_agent = os.environ.get("user_agent")
    reddit = praw.Reddit(client_id = client_id,#my client id
                     client_secret = client_secret,  #your client secret
                     user_agent = user_agent #user agent name
                     )

    sub = ['MachineLearning','OpenAI','ChatGPT','OpenAIDev','learnmachinelearning'] 
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
    df.to_csv(os.path.join(output_dir,"subreddit.csv")
    return

