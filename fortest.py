import pandas as pd
import requests
import sys
import boto3
import os
s3 = boto3.resource('s3')
bucket = s3.Bucket('card-img')
df = pd.read_csv('cardimg.csv')
for image_data in df.itertuples():
    response = requests.get(image_data.image_uri)
    num = str(image_data.new_variables_card_id)
    name = 'pic/' + num
    open(name + '.jpg', 'wb').write(response.content)
    bucket.upload_file(name + '.jpg', num + '.jpg')
    os.remove(name + '.jpg')
    if int(num) % 100 == 0:
        print(num)
