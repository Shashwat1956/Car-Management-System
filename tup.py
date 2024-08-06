print("Welcome user = 1956")
print("-------------------")
print("CARS DETAILS")
print("*************")
a = input("Enter your name: ")
print("Hello", a)

car_details = []
service_details = []

while True:
    print("Choose one option.")
    print("1. Register your car \n2. Check the details \n3. Services \n4. Exit")
    b = int(input("Enter your choice: "))

    if b == 1:
        print("Welcome", a)
        print("Register your car")
        print("-----------------")
        print("Fill the details..")
        date = float(input("Date: "))
        num = int(input("Enter your car number: "))
        model_num = int(input("Model Number: "))
        car_details.append((a, date, num, model_num))
        print("Car registered.") 
        print("Thank you")

    elif b == 2:
        print("Welcome", a)
        print("Check your details")
        print("------------------")
        c = int(input("Enter your car number: "))
        car_found = False
        for car in car_details:
            if car[2] == c:
                print("Details.")
                print("--------")
                print("Hello user", car[0])
                print("Registered date:", car[1])
                print("Car number:", car[2])
                print("Model Number:", car[3])
                car_found = True
                break
        if not car_found:
            print("Invalid car number!")

    elif b == 3:
        print("Welcome", a)
        print("Services")
        print("--------")

        while True:
            print("Choose an option:")
            print("1. Car wash \n2. Car paint \n3. Servicing \n4. Exit")
            d = int(input("Enter your choice: "))

            if d == 1:
                print("Car Wash")
                print("--------")
                print("Enter your details:")
                dat = float(input("Date: "))
                number = int(input("Enter your car number: "))
                model = int(input("Model Number: "))
                service_details.append(("Car Wash", dat, number, model))
                print("Thank you")

            elif d == 2:
                print("Car Paint")
                print("--------")
                print("Enter your details:")
                g = float(input("Date: "))
                n = int(input("Enter your car number: "))
                m = int(input("Model Number: "))
                service_details.append(("Car Paint", g, n, m))
                print("Thank you")

            elif d == 3:
                print("Servicing")
                print("---------")
                print("Sorry, we are out of service.!")
            
            elif d == 4:
                print("Exiting")
                break

            else:
                print("Invalid choice.!")

            cont = input("Continue? (yes/no): ")
            if cont != 'yes':
                break

    elif b == 4:
        print("Exiting..")
        break

    else:
        print("Invalid choice.!")

    cont = input("Do you want to continue? (yes/no): ")
    if cont != 'yes':
        break

print("Goodbye!")

