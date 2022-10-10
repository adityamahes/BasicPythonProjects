# challenge 1
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
my_email = "yourawesomebirthdaywisher@gmail.com"
password = "eWj5*5h$1RF)jPs"

while True:
    if now.weekday() == 6:
        with open("quotes.txt") as quotes:
            all_quotes = quotes.readlines()
            quote = random.choice(all_quotes)
            parts = quote.split(" - ")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="yourawesomebirthdaywisher2@gmail.com",
                msg=f"Subject:Monday Motivation from {parts[1]}\n\n{quote}"
            )
