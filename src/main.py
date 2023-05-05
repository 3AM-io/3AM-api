from app import responseGen
from speechrecognition import takeCommand

if __name__ == '__main__':
    query = takeCommand()
    responseGen(query)
