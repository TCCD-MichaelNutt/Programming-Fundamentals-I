
def main():
    # Get the number of hours worked
    hours = input("How many hours did you work? ")
    # Get the hourly rate
    rate = input("How much do you get paid per hour? ")

    # Calculate the pay
    pay = float(hours) * float(rate)

    # Display the pay
    print("You have earned $" + str(pay))


if __name__ == '__main__':
    main()