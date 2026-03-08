import requests


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def pocket_message(amount):
    return f"there is {amount} in my pocket"


def website_is_working(url="https://google.com"):
    response = requests.get(url, timeout=5)
    return response.status_code == 200


def count_invalid_lines(filename="notes.txt"):
    errors = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if "not valid" in line:
                errors += 1
    return errors


if __name__ == "__main__":
    num1 = 200
    print("this is my first python program")
    print(add_numbers(num1, 400))
    print(subtract_numbers(num1, 400))
    print(pocket_message(num1))
    print("Website is working" if website_is_working() else "Website is not working")
    print("The number of invalid lines is:", count_invalid_lines())
    print("first test autoamted remotw workflow on gitaction")