import os
import random
from PIL import Image
from person import Person
from apartment import Address
from apartmentPooling import findApartment
permitCity=['sderot', 'ofakim', 'netivot', 'hotefAza', 'kriat shmona']
class Borrower (Person):
    permitCity = ['sderot', 'ofakim', 'netivot', 'hotefAza', 'kriat shmona']
    def __init__(self, name, city, phoneNumber):
        super(Borrower, self).__init__(name,phoneNumber)
        if city not in permitCity:
            print("Sorry,our city does not appear in the list of evacuated cities")
            return False
        self.city=city
        self.conditons={}
    def showPicture(self):
        num=random.randint(0,20)
        img = Image.open(f"ex/img/{num}.jpg")
        img.show()


    def chekAdjustment(self):
        find,percent =findApartment(self.conditons)
        if find == None:
            print("Sorry, no apartment found. We will send you an sms when the database is updated")
        else:
            print(f"We found an apartment for you with a {percent} percent match, the apartment owners will contact you as soon as possible")
            self.showPicture()

    def details (self):
        city=input("which city do you want?")
        neighborhood = input("which neighborhood  do you want?")
        requireAddress= Address(city,neighborhood)
        self.conditons['address']= requireAddress
        num = input("how many rooms do you need")
        while type(num)!=int:
            try:
               num=int(num)
            except :
                print("The value is invalid,enter again")
                num = input("how many rooms do you need")
        self.conditons['numRooms'] = num
        num = input("how many beds do you need")
        while type(num) != int:
            try:
                num = int(num)
            except:
                 print("The value is invalid, enter again")
                 num = input(" how many beds do you need")

        self.conditons['numBeds'] = num
        self.conditons['crib'] = input("Do you need crib?")
        if self.conditons['crib']=='yes' or self.conditons['crib']=='true' or self.conditons['crib']=='y':
            self.conditons['crib']=True
        else:
            self.conditons['crib']=False
        self.conditons['accessibility'] = input("Do you need accessibility?")
        if self.conditons['accessibility']=='yes' or self.conditons['accessibility']=='true'or self.conditons['accessibility']=='y':
            self.conditons['accessibility']=True
        else:
            self.conditons['accessibility']=False
        self.chekAdjustment()












