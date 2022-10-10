##################### Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random

my_email = "yourawesomebirthdaywisher@gmail.com"
password = "eWj5*5h$1RF)jPs"

today = dt.datetime.now()

data = pandas.read_csv("birthdays.csv")

birthdays_list = data.to_dict(orient="records")

for item in birthdays_list:
    if (today.day,today.month) == (item["day"],item["month"]):
        file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            letter_contents = letter_file.read()
            letter_contents = letter_contents.replace("[NAME]", item["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=item["email"],
                msg=f"Subject: Happy Birthday!\n\n{letter_contents}"
            )
# Use python anywhere to run in the background in cloud (you can schedule it)
