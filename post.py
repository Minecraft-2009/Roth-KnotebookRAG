import requests
import json


test_text = """
Earendil was a mariner who tarried in Arvenien
He built a boat of timer felled in Nimbrethel to journey in
Her sails he wove of silver fair of silver were her lanterns made
Her prow was fashioned like a swan and light upon her banners laid
In panoply of Ancient kings in chained rings he armoured him
His shining shield was scored with runes to ward all runes and harm from him
His sword of steel was valiant of adamant his helmet tall
An eagle plume upon his crest upon his breast an emerald
Beneath the moon and under star he wandered far on northern strands
Bewildered on enchanted ways beyond the days of mortal lands
From gnashing of the narrow ice where shadow lies on frozen hills
From nether heats and burning waste he turned in haste and roving still
On starless waters far a stray at last he came ti night of naught
And passed and never sight he saw of shining shore nor light he sought
The winds of wrath came driving him and blindly in the foam he fled
From east to west and errandless unheralded he homeward sped

"""


base_url = "http://127.0.0.1:5000" 
path = "/new"
url = base_url + path

data = { "text": test_text, "doc_id": "892", "user_id": "steve", "notebook_id": "123" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)