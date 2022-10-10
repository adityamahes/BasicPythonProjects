import smtplib

my_email = "yourawesomebirthdaywisher@gmail.com"
password = "eWj5*5h$1RF)jPs"

with smtplib.SMTP("smtp.gmail.com") as connection: # Object, a way to connect to emailproviders
    # We need to specify the location of our email providers SMTP server (HOST)
    connection.starttls() # Transport layer security: Way of securing our connection to email server
    # If someone intercepts our email in its journey to the recipient, that message will be encrypted. They can't read it
    connection.login(user=my_email, password=password) # to login
    connection.sendmail(
        from_addr=my_email,
        to_addrs="yourawesomebirthdaywisher2@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email"
    )
# We don't need to use connection.close() if we use with as
# This won't work unless you remove security bounding in GMAIL account (turn on acces to less secure apps)


