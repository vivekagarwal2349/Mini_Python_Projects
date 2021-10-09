import requests
import time
from datetime import datetime, timedelta

age = int(input("Enter Age "))
zipcode = input("Enter Pin Code ")
pin = zipcode.split()
no_days = int(input("Enter Days "))
flag = 'Y'

current = datetime.today()
form = [current + timedelta(days=i) for i in range(no_days)]
date_format = [i.strftime("%d-%m-%y") for i in form]

while 1:
    i = 0
    for find in pin:
        for enter_date in date_format:
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(find, enter_date)

            requirements = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

            final = requests.get(url, headers=requirements)

            if final.ok:
                file_json = final.json()
                flag2 = False
                if file_json["centers"]:
                    if flag.lower() == "y":

                        for place in file_json["centers"]:
                            for vaccine in place["sessions"]:
                                if vaccine["min_age_limit"] <= age and vaccine["available_capacity"] > 0:
                                    print("")
                                    print("PinCode :- ", pin)
                                    print("Date :- {}".format(enter_date))
                                    print("Location :- ", place["name"])
                                    print("Block :-", place["block_name"])
                                    print("Price :-", place["fee_type"])
                                    print("Vaccine :-", vaccine["available_capacity"])

                                    if vaccine["vaccine"] != '':
                                        print("Type :- ", vaccine["vaccine"])
                                        print("")

                                    i = i + 1
                                else:
                                    pass
                    else:
                        pass
                else:
                    print("x.x No Response")
    if i == 0:
        print("No Vaccine... Try Again Later ")
    else:
        print("Search End")

    date_now = datetime.now() + timedelta(minutes=1)

    while datetime.now() < date_now:
        time.sleep(1)
