import tweepy
import requests
import random
API_KEY = "YOUR API KEY"
API_SECRET = "YOUR API SECRET KEY"
ACCESS_TOKEN = "YOUR ACCESS TOKEN"
ACCESS_TOKEN_SECRET = "YOUR ACCESS TOKEN SECRET"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

image_path = f'https://tanguyesteoule.github.io/thisalbumdoesnotexist/assets/covers/{random.randint(1,1500)}.png'
tmp_path = '/home/tanguy/workspace/jupyter/twitter/tmp.png'
img_data = requests.get(image_path).content
with open(tmp_path, 'wb') as handler:
    handler.write(img_data)
    
status = api.update_status_with_media('', tmp_path)