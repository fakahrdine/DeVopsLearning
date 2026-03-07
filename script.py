import time
import requests

print("this my first python programme")
num1 = 200
print(num1 + 400)
print(num1 - 400)
print("there is " + str(num1) + " in my pocket")
print("there is " + str(400) + "    in my pocket")
print("there is " + str(num1) + " in my pocket")
print(f"hellow man I have {num1 + 400} in my pocket")
num_days = 60
num_hours = 24
num_seconds = 60
num_months = 12
num_minuts = 60
num_days_years = 365
calendar = ("day", "week", "month", "year")
one_day_minuts = num_hours * num_minuts
one_wk_minuts = one_day_minuts * 7
one_month_minuts = one_wk_minuts * 4
one_year_minuts = one_month_minuts * 12

calendar = ("day" or "week" or "month" or "year")


#print(f"the total  nunmber of minnuts in one day is {num_minutsInDay} ")
# lets study function


def scop_check(my_name):
    print(calendar)
    print(my_name)
    scop_check("mohamed")


def days_to_units():
    print("All days are good")
    print("the numbers of days in one year is :" + str(num_days_years))


#seconds = 0
#while seconds < 100*3:
#  time.sleep(1)
#  seconds = seconds + 1
print("Iam done withing for 5 minuts")
requests.get("https://google.com")
if requests.get("https://google.com").status_code == 200:
    print("Website is working ")
else:
    print("Website is not working")
print("Iam done withing for 5 minuts")

errors = 0

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

        for line in file:
            if "not valid" in line:
                errors += 1
    print(" the numbers of notvalid lines is: ", errors)
    notes = file.read()

    # hello

  # Iam now on new branch called version2 doing som changes