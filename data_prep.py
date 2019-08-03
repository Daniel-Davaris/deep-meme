import pandas as pd
import requests
import numpy as np
import cv2
import h5py 
from scraper import scrape

max_score = 0
min_score = 0

# converts the image 
def pull_img_web(url):
    # pull image
    resp = requests.get(url)
    image = np.asarray(bytearray(resp.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # resize
    image = cv2.resize(image, (100, 100))
    print(image.shape)
    return image
# array change
def csv_to_np():
    # I know this is bad dw
    global max_score, min_score
    # print(topics_data)
    x = pd.read_csv('exported_data.csv')
    print(x.keys())
    df = pd.DataFrame(x, columns=["id", "url", "score"])

    max_score = df.score.max() - df.score.min()
    min_score = df.score.min()
    em = df.as_matrix()
    print("OK!")
    out = []
    for row in em:
        try:
            img = pull_img_web(row[1])
            out.append((clamp_score(row[2], row[0]), img))
        except:
            continue
    return np.array(out)
# convert to h5
def np_to_h5py():
    stuffs = csv_to_np()
    print(len(stuffs))
    labels, imgs = zip(*stuffs)
    h5f = h5py.File('data.h5', 'w')
    h5f.create_dataset('imgs', data=imgs)
    h5f.create_dataset('labels', data=labels)
    h5f.close()
    return (labels, imgs)
#convert to labels and iamges
def h5py_to_np():
    h5f = h5py.File('data.h5','r')
    return (h5f['labels'][:], h5f['imgs'][:])
# regularisation
def clamp_score(score, index):
    # Sorry in advance
    global max_score, min_score
    score -= min_score
    score /= int(max_score / 10)
    lst = [0 for _ in range(10)]
    lst[int(score)] = 1
    print(lst)
    return lst

def export_to_csv(topics_data):
    topics_data.to_csv('exported_data.csv', index=False) 



    

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


if __name__ == '__main__':
    a = scrape()
    export_to_csv(a)
    a = np_to_h5py()
    b = h5py_to_np()
    print("WOOOO" if a[0][0][0] == b[0][0][0] else ";(")
