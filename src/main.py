import os
from app import responseGen
from speechrecognition import takeCommand
from dotenv import load_dotenv
from setup import setupEnvironment

if __name__ == '__main__':
    # Local environment setup
    load_dotenv()
    senderMail = os.environ.get('SENDER_MAIL')
    if senderMail == "example123@gmail.com":
        setupEnvironment()

    query = takeCommand()
    responseGen(query)
