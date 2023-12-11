def setupEnvironment():    
    SENDER_EMAIL = input("Enter your email: ")
    SENDER_PASS = input("Enter your email secret pass: ")
    SPOTIFY_USERNAME = input("Enter your spotify username: ")
    SPOTIFY_CLIENT_ID = input("Enter your spotify client id: ")
    SPOTIFY_SECRET = input("Enter your spotify secret key: ")
    
    
    # Write to .env file
    with open('../.env', 'w') as f:
        f.write(f"SENDER_MAIL=\"{SENDER_EMAIL}\"\n")
        f.write(f"SENDER_PASS=\"{SENDER_PASS}\"\n")
        f.write(f"SPOTIFY_USERNAME=\"{SPOTIFY_USERNAME}\"\n")
        f.write(f"SPOTIFY_CLIENT_ID=\"{SPOTIFY_CLIENT_ID}\"\n")
        f.write(f"SPOTIFY_SECRET=\"{SPOTIFY_SECRET}\"\n")
    print("Environment setup done. Please restart the program")
 