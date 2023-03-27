import requests
import json

def summery(searchKey):
    headers = {
        "Content-Type": "application/json",
        "apikey": r"02c72ff0-5e65-4c03-9144-e7bf57e572a6"
    }

    body = {
        "text": searchKey
    }
    url = "https://app.thetextapi.com/text/summarize"
    
    response = requests.post(url, headers=headers, json=body)
    summary = json.loads(response.text)["summary"]
    
    return summary

# thanks to TheTextApi Summerizer <https://www.thetextapi.com/>