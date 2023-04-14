from app import responseGen
from speechrecognition import takeCommand

if __name__ == 'main':
    query = takeCommand()
    responseGen(query)
