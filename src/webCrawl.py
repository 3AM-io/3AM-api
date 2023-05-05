import webbrowser
from bs4 import BeautifulSoup
import re
import requests
from summerizerRes import summery
from speak import speak
from gsearchapi import googleSearch

ansi_escape = re.compile("[^a-zA-Z' ]+")

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
    # Get Summerized text
    resultList = []
    iter = 0
    for result in parsedContent.find('body').find_all('p'):
        iter += 1
        resultList.append(re.sub(r'\\.*$', '', str(result.text)))
        resultList.append(str(result.text).replace(r"\t", " ").replace(r"\n", " ").replace(r"\x", " ")
                          .replace(r"\s", " ").strip())

        if iter == 20:
            break
    
    if len(resultList) < 1:
        for result in parsedContent.find('body').find_all('div'):
            iter += 1
            resultList.append(re.sub(r'\\.*$', '', str(result.text)))
            resultList.append(str(result.text).replace(r"\t", " ").replace(r"\n", " ").replace(r"\x", " ")
                              .replace(r"\s", " ").strip())

            if iter == 20:
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
    print(response)
    print(response["links"])
    result = ansi_escape.sub('', getSummeryFromURL(response["links"]))
    return result