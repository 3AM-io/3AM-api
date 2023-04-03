import webbrowser
from bs4 import BeautifulSoup
import os
import requests
from summerizerRes import summery
from speak import speak
from gsearchapi import googleSearch

# Search Query as URL
def searchSite(site: str):
    print(f"Opening {site}")
    webbrowser.open_new_tab(site)
    
# Summerizer
def getSummeryFromURL(url: str):
    wordLimit = 20
    response = None
    try:
        response = requests.get(url)
    except:
        speak("There's an unusual error. Try again later")

    responseFile = open(".tempResponse.html", "w")
    responseFile.write(str(response.content))

    # Parser
    f = open(".tempResponse.html", "r")
    parsedContent = BeautifulSoup(f, 'html.parser')
    f.close()
    os.unlink(f)
    # Get Summerized text
    resultList = []
    iter = 0
    for result in parsedContent.find('body').find_all('p'):
        iter += 1
        resultList.append(str(result.text).replace(r"\n", " ").strip())

        if iter == 100:
            break
    
    if len(resultList) < 1:
        for result in parsedContent.find('body').find_all('div'):
            iter += 1
            resultList.append(str(result.text).replace(r"\n", " ").strip())

            if iter == 100:
                break
    
    summary = ''.join(resultList)
    # UnCommand this line to get the summerizer activated
    # summerizedContent = summery(''.join(resultList))
    # summerizedLimit = sumerizedContent.split(" ")[0:wordLimit]
    
    
    return summary


# Search Query as Keyword
def gSearch(query: str):
    response = googleSearch(query)
    # webbrowser.open_new_tab(response["links"])
    print(response["links"])
    return getSummeryFromURL(response["links"])