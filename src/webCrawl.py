import webbrowser
#from googlesearch import search
from bs4 import BeautifulSoup
import requests
from summerizerRes import summery
from speak import speak

# Search Query as URL
def searchSite(site: str):
    print(f"Opening {site}")
    webbrowser.open_new_tab(site)
    
# Summerizer
def getSummeryFromURL(url: str):
    response = None
    try:
        response = requests.get(str)
    except:
        speak("There's an unusual error. Try again later")

    responseFile = open(".tempResponse.html", "w")
    responseFile.write(str(response.content))

    # Parser
    f = open(".tempResponse.html", "r")
    parsedContent = BeautifulSoup(f, 'html.parser')

    # Get Summerized text
    resultList = []
    iter = 0
    for result in parsedContent.find('body').find_all('p'):
        iter += 1
        resultList.append(str(result.text).replace(r"\n", "").strip())

        if iter == 1000:
            break

    sumerizedContent = ""
    # UnCommand this line to get the summerizer activated
    # summerizedContent = summery(''.join(resultList))

    return sumerizedContent


# Search Query as Keyword
def gSearch(query: str):
    url = r'https://www.google.com/search?q="' + query + '"'
    webbrowser.open_new_tab(url)