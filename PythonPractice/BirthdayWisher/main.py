import smtplib
import random
import datetime
import pandas

MY_EMAIL = "jwitkowsky1@gmail.com"
PASSWORD = "Baseball!0!!"

quote_list = []
with open("quotes.txt") as file:
    for data in file:
        line = data.strip()
        quote_list.append(line)
quote_today = random.choice(quote_list)

birthday_file = pandas.read_csv("birthdays.csv")
new_dict = birthday_file.to_dict()

today = datetime.datetime.today()

for birthday in new_dict:
    if (birthday["day"] == today.day) and (birthday["month"] == today.month) and (birthday["year"] == today.year):

        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday["email"],
            msg="Subject:Motivational Monday\n\n" + quote_today
        )
        connection.close()



#smtp.mail.yahoo.com