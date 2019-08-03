#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import urllib

def scrape():
    reddit = praw.Reddit(client_id='zYB_XDoA3o_YKQ', \
                        client_secret='FxM4ELY9LdRHigqU7gFmp-NUvms', \
                        user_agent='scraper', \
                        username='daniel_davaris2', \
                        password='@Anvil2689')

    subreddit = reddit.subreddit('memes')

    top_subreddit = subreddit.top()

    for submission in subreddit.top(limit=1):
        print(submission.title, submission.id)

    topics_dict = { "title":[], 
                    "score":[], 
                    "len_title":[],
                    "id":[], "url":[], 
                    "comms_num": [], 
                    "created": [], 
                    "body":[]}

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

# print("worked",topics_data )

def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.to_csv('exported_data.csv', index=False) 

def pull_img_web(url):
    # pull image
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # resize 
    image = cv2.resize(image, (200, 200))
    return image

def load_data():
    for item in pd.read_csv('exported_data.csv'):
        yield (item.score, pull_img_web(item.url))


if __name__ == '__main__':
    scrape()