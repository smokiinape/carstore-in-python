class Customer:
    def __init__(self, name, personNr):
        self.name = name
        self.personNr = personNr


class Personal:
    def __init__(self, name, titel):
        self.name = name
        self.titel = titel

    def __repr__(self):
        return self.name + ", " + self.titel


class Car:
    def __init__(self, brand, model, year, mileage, regNr, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.regNr = regNr
        self.price = price

    def __repr__(self):
        return self.brand + ', ' + self.model + ", year: " + self.year + ", mileage: " + self.mileage + ", RegNr " + self.regNr + ", price: " + self.price + "kr\n"


x = 1

car1 = Car("BMW", "320", "2020", "2000", "ABC123", "200000")
car2 = Car("Opel", "Astra", "1999", "13500", "DEF123", "23000")
car3 = Car("Audi", "A5", "2008", "5600", "GHJ123", "135000")

personal1 = Personal("Aman", "Salesman")
personal2 = Personal("Olof", "Salesman")

carsList = [car1, car2, car3]
personalList = [personal1, personal2]
salesList = []

serviceList = []

print("welcome to smokin ape car store\n")

while x != 0:
    x = int(input(
        "press 1 if you want to buy a car\n"
        "press 2 if you want to sell your car\n"
        "press 3 if you want to check the inventory of cars\n"
        "press 4 to see the list of sales we've made\n"
        "press 5 for service, repair or warranty\n"
        "press 6 to see the repair list\n"
        "press 0 to exit\n"))

    if x == 1:
        cName = input("Enter your name")
        cPersonNr = input("Enter your personnr")
        print(carsList)
        regNr = input("Which car do you want to buy, enter the regnr?")
        for x in carsList:
            if x.regNr == regNr:
                salesList.append(
                    "RegNr: " + regNr + " Customer: " + cName + " " + cPersonNr + ", " + personalList[0].titel + ": " +
                    personalList[0].name)
                carsList.remove(x)

    elif x == 2:
        print("You want to sell you car")
        brand = input("Enter brand")
        model = input("Enter model")
        year = input("Enter year")
        mileage = input("Enter mileage")
        regNr = input("Enter regNr")
        price = int(input("Enter price you want"))
        price *= 1.2

        carsList.append(Car(brand, model, year, mileage, regNr, str(price)))

    elif x == 3:
        print(carsList)
    elif x == 4:
        print(salesList)
    elif x == 5:
        typeOfWork = input("Service, repair or Warranty?")
        regNr = input("Whats your regNr?")
        cName = input("Whats your name")
        cNumber = input("Whats your number?")
        description = input("description of your problem")

        serviceList.append(typeOfWork + " | " + regNr + " | " + cName + " " + cNumber + " | " + description)

    elif x == 6:
        print(serviceList)
    elif x == 0:
        print("byebye")
    else:
        print("Wrong choice")
