from person import Person
from apartment import *
from apartmentPooling import addApartment

class Lender(Person):
    def __init__(self, name, phoneNumber):
        super(Lender, self).__init__(name,phoneNumber)

    def details(self):
        print("Enter the address of the apartment:")
        city = input("Enter city:")
        neighborhood = input("Enter neighborhood:")
        street = input("Enter street:")
        buildingNumber = input(" buildingNumber:")
        while type(buildingNumber) != int:
            try:
                buildingNumber = int(buildingNumber)
            except:
                print("The value is invalid,enter again!")
                buildingNumber = input(" buildingNumber:")
                # בדיקת תקינות גם למספר דירה
        apartmentNumber = input("Enter apartmentNumber:")
        address = Address(city, neighborhood, street, buildingNumber, apartmentNumber)
        numRooms = input("how many rooms do you have?")
        while type(numRooms) != int:
            try:
                numRooms = int(numRooms)
            except:
                print("The value is invalid,enter again:")
                numRooms = input("how many rooms do you have?")
        numBeds = input("how many beds do you have?")
        while type(numBeds) != int:
            try:
                numBeds = int(numBeds)
            except:
                print("The value is invalid, enter again")
                numBeds = input("how many beds do you have?")
        crib = input("Do you have a crib?")
        if crib == 'yes' or crib == 'true' or crib == "y":
            crib = True
        else:
            crib = False
        accessibility = input("Is your apartment accessible?")
        if accessibility == 'yes' or accessibility == 'true' or accessibility == 'y':
            accessibility = True
        else:
            accessibility = False
        apartment = Apartment(address, numRooms, numBeds, crib, accessibility)
        addApartment(apartment)
        print("The apartment has entered the database, thank you very much!")

