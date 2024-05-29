import pandas
from random import choice
import smtplib
import datetime as dt

MY_EMAIL = "necamark@gmail.com"
PASSWORD = "xuklpbmootnalxdi"
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

now = dt.datetime.now()
day = now.day
month = now.month


birthdays = pandas.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    if row["month"] == month and row["day"] == day:
        rand_letter = choice(letters)
        with open("letter_templates/"+rand_letter) as letter:
            letter_to_send = letter.read()
            letter_to_send = letter_to_send.replace("[NAME]", row["name"])
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=row["email"],
                    msg=f"Subject:Birthday Card\n\n{letter_to_send}"
                )
