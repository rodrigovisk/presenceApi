import requests
import json

# set to your own subscription key value
subscription_key = '0db517a3662249309d44cf5d0bfb02f2'
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://reconhecerface.cognitiveservices.azure.com/face/v1.0/detect'

image_url = 'https://br.web.img2.acsta.net/pictures/18/08/08/18/23/1187644.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
print(json.dumps(response.json()))

