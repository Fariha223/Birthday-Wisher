import smtplib
import datetime as dt
import random

my_email = "fariha.hasan.tonima@g.bracu.ac.bd"
password = "qfqp hfbe yxjr iols"

now = dt.datetime.now()
weekday = now.weekday()
try:
    if weekday == 3:
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)

        print(quote)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: Thursday Motivation\n\n{quote}"
            )
            print("Email sent successfully.")
    else:
        print("Today is not Thursday! Email not sent.")

except FileNotFoundError:
    print("The quotes.txt file was not found.")

except Exception as e:
    print(f"An error occurred: {e}")

print(now)