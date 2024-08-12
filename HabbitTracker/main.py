import requests
from datetime import datetime

#constants
TOKEN = "hjuegt12"
USERNAME = "vaishvi01"
GRAPHID = "graph01"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params ={
    "token":TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# create pixela user
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit" : "min",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

#create the graph
#response = requests.post(url= graph_endpoint, json= graph_config, headers= headers)
#print(response.text)

#todays_date = datetime(year= 2024 , month=7, day=27)
todays_date = datetime.now()

pixel_config ={
    "date": todays_date.strftime("%Y%m%d"),
    "quantity": "10"
    }

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

#make a pixel on the graph
response = requests.post(url=pixel_endpoint,json= pixel_config ,headers=headers)
print(response.text)