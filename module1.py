import requests
import json
from textblob import TextBlob
import pandas as pd

#from googleapiclient.discovery import build

api_key = 'AIzaSyDtpMeb0bGkCzgwGFpI-JklXDaIf6VWZYc'

#youtube = build('youtube', 'v3', developerKey=api_key)

#request = youtube.channels().list(
#    part= 'statistics',
#    forUsername='smosh'
#)

#response = request.execute()
#print(response)

#video_id = "RASgqPsVXUM"
video_id = "Gb6RK32q4Qg"

#retrieve youtube information
video_info_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
video_info_response = requests.get(video_info_url)
video_info_data = video_info_response.json()
print(video_info_data)



comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
comments_response = requests.get(comments_url)
comments_data = comments_response.json()


#extract comments
comments = [item["snippet"]["topLevelComment"]["snippet"]["textOriginal"] for item in comments_data["items"]]
print(comments)


def get_comment_sentitment(comment):
    analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
    
    
for comment in comments:
    print(f"{comment} : {get_comment_sentitment(comment)}")
    
comment_text = []
comment_label = []

#display sentiment for youtube video comment's
for comment in comments:
    comment_text.append(comment)
    print(comment)
    t=get_comment_sentitment(comment)
    print(t)
    comment_label.append(t)
    

pd.DataFrame({"comments": comment_text, "sentiment": comment_label})

df1= pd.DataFrame({"comments": comment_text, "sentiment": comment_label})
print(df1)
df1.to_csv("ycomments.csv")


