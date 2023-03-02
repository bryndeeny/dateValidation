from datetime import datetime
from datetime import date

def ValidDate(test_str):
    print("The date you inputted is : " + str(test_str))
    # initializing format
    format = "%d-%m-%Y"
    # checking if format matches the date
    try:
        datetime.strptime(test_str, format)
        return True
    except ValueError:
        return False

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# get user input and validate date format
input_str = input('Enter birth date (dd-mm-yyyy): ')
while not ValidDate(input_str):
    print("Invalid date format.")
    input_str = input('Enter birth date in (dd-mm-yyyy): ')

# convert input string to datetime object
born = datetime.strptime(input_str, '%d-%m-%Y').date()

# calculate age and print result
age = calculate_age(born)
print("Age is:", age)
