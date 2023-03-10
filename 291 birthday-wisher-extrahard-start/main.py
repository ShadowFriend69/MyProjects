import datetime as dt
import smtplib
import random
import pandas
import os


PLACEHOLDER = '[NAME]'
MY_EMAIL = 'day32.0001@gmail.com'
MY_PASSWORD = 'wgnavynehmlbghzu'

now = dt.datetime.now()
month = now.month
day = now.day

bdays_file = pandas.read_csv("birthdays.csv")
bdays_dict = bdays_file.to_dict()
days = bdays_dict['day']

if day in days:
    key = day-1
    if bdays_dict['month'][key] == month:
        name = bdays_dict['name'][key]
        email = bdays_dict['email'][key]
        current_letter = random.choice(os.listdir("letter_templates"))

        with open(f'letter_templates/{current_letter}') as letter:
            letter_content = letter.read()
            new_letter = letter_content.replace(PLACEHOLDER, name)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f'Subject:Happy Birthday!\n\n{new_letter}'
            )









