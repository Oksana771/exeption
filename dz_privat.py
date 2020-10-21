import datetime
import requests
import os
import time
import random

def test_code():
    error_file = open("error.log", "a")
    success_file = open("success.log", "a")
    time.sleep(random.randint(30, 60))
    try:
        URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        currency = requests.get(URL)
        currency = currency.json()
        print(currency)
        data = datetime.datetime.today().strftime("%d/%m/%y %H:%M")
        print(data)

        success_file.write(os.getlogin() + " " + data +
                       " " + "Status code = 200" + "\n")
   
    except Exception as e:
        error_file.write(os.getlogin() + " " + data + " " + str(e) + "\n")

    finally:
        success_file.close()
        error_file.close()
while True:
    test_code()

    