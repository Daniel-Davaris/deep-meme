#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import urllib
import numpy as np
import cv2
import passwords
import h5py 

def scrape():
    reddit = praw.Reddit(client_id='zYB_XDoA3o_YKQ',
                         client_secret='FxM4ELY9LdRHigqU7gFmp-NUvms',
                         user_agent='scraper',
                         username='daniel_davaris2',
                         password=passwords.reddit_pass)

    subreddit = reddit.subreddit('memes')

    top_subreddit = subreddit.top(limit=500)

    for submission in subreddit.top(limit=1):
        print(submission.title, submission.id)

    topics_dict = {"title": [],
                   "score": [],
                   "len_title": [],
                   "id": [], "url": [],
                   "comms_num": [],
                   "created": [],
                   "body": []}

    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["len_title"].append(len(submission.title))
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)

    topics_data = pd.DataFrame(topics_dict)

    _timestamp = topics_data["created"].apply(get_date)
    topics_data = topics_data.assign(timestamp=_timestamp)
    print("worked",topics_data )
    return topics_data


def get_date(created):
    return dt.datetime.fromtimestamp(created)


# topics_data.to_csv('exported_data.csv', index=False)

def pull_img_web(url):
    # pull image
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # resize
    image = cv2.resize(image, (200, 200))

    return image

def load_data():
    # print(topics_data)
    x = pd.read_csv('exported_data.csv')
    df = pd.DataFrame(x, columns=["url", "score"])
    for v in df:
        v.as_matrix
    em = df.as_matrix()
    return (clamp_score(em[1]), pull_img_web(em[0]))
    

def clamp_score():
    pass
    # print(em)
    # print(type(em))
    # h5f = h5py.File('data.h5', 'w')
    # h5f.create_dataset('dataset_1', data=a)

    
    # for index, row in df.iterrows():
    #     new_score = (row['score'])
        # em.append(index, row['url'], new_score)
        # print("max", max(new_score))
        # print(index, row['url'], new_score)

        
    # for item in pd.read_csv('exported_data.csv')[1:]:
    #     print(item)
        # var = [item.score, pull_img_web(item.url)]
        
        # h5f = h5py.File('data.h5', 'w')
        # h5f.create_dataset('dataset_1', data=a)
           
def export_to_csv(topics_data):
    topics_data.to_csv('exported_data.csv', index=False) 

if __name__ == '__main__':
    # a = scrape()
    # export_to_csv(a)
    load_data()
