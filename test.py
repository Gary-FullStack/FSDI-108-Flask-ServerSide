

def say_hello():
    print("hello")


def some_numbers():
    prices = [1.5, 2.5, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
              11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]

    total = 0
    count = 0
    for num in prices:
        total += num

        if num < 12:
            count += 1

    print(f"The total is: {total}")
    print(f"there are {count} lower than 12")


def some_colors():
    colors = ["red", "Green", "blue", "yellow", "green", "Orange", "Red", "BLUE",
              "YELLOW", "blue", "purple", "Pink", "brown", "Black", "white", "GREY", "silver",
              "Gold", "Cyan", "magenta", "BluE"]

    print(len(colors))

    count = 0
    for color in colors:
        if color.lower() == "blue":
            count += 1

    print(f"Blue appears {count} times")

    results = []
    for color in colors:
        color = color.lower()
        if color not in results:
            results.append(color)

    print(results)


def some_ages():
    ages = [24, 35, 18, 46, 29, 51, 22, 33, 40,
            27, 55, 19, 31, 37, 43, 25, 49, 20, 23, 26]

    over30 = 0
    between = 0
    for age in ages:
        if age > 30:
            over30 += 1

        if age >= 25 and age <= 35:
            between += 1

    print(f"there are {over30} and {between} between 25 and 35")


say_hello()
some_numbers()
some_colors()
some_ages()
