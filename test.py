import webbrowser
from bs4 import BeautifulSoup
import json
import requests
from summerizerRes import summery
from speak import speak
from gsearchapi import googleSearch

def getSummeryFromURL(url: str):
    wordLimit = 20
    response = None
    try:
        response = requests.get(url)
        print(response.contnet)
    except:
        print("Not")
        speak("There's an unusual error. Try again later")

    # Parser
    parsedContent = BeautifulSoup(response.content, 'html.parser')

    # Get Summerized text
    resultList = []
    iter = 0
    for result in parsedContent.find('body').find_all('p'):
        iter += 1
        resultList.append(str(result.text).replace(r"\n", " ").strip())

        if iter == 100:
            break
        
    content = ''.join(resultList)
    # UnCommand this line to get the summerizer activated
    # summerizedContent = summery(''.join(resultList))
    # summerizedLimit = sumerizedContent.split(" ")[0:wordLimit]
    
    headers = {
        "Content-Type": "application/json",
        "apikey": "02c72ff0-5e65-4c03-9144-e7bf57e572a6"
    }

    body = {
        "text": content
    }
    url = "https://app.thetextapi.com/text/summarize"
    response = requests.post(url, headers=headers, json=body)
    summary = json.loads(response.text)["summary"]
    print(summary)
    
    return summary


print(getSummeryFromURL("https://en.wikipedia.org/wiki/Ariana_Grande"))