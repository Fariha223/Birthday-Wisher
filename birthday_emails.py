import pandas
from datetime import datetime
import smtplib

my_email = "fariha.hasan.tonima@g.bracu.ac.bd"
password = "qfqp hfbe yxjr iols"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birth_dates.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open("birthday_text_contents.txt") as text:
        contents = text.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )


