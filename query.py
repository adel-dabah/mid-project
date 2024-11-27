import requests
url='http://localhost:9696/predict'

user={"tags":"interested_in_other_courses","totalvisits":0.0,"total_time_spent_on_website":0,"last_notable_activity":"modified","city":"select"}
print(requests.post(url,json=user).json())