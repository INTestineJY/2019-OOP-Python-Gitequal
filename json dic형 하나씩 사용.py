import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

pprint(data) #data는 json 전체를 dictionary 형태로 저장하고 있음

#-----여기까지 동일-----

data["maps"][0]["id"] #값 하나하나 접근하기
data["masks"]["id"]
data["om_points"]