import os
from dotenv import load_dotenv




if __name__ == "__main__":

    load_dotenv()
    mypassword = os.getenv("MYPASSWORD")
    print(mypassword)