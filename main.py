from person import *
from lender import *
from borrower import *
from apartment import *
def borrowingDatails():
    name=input("Enter your name ")
    city=input("Enter your city of residence")
    phoneNumber=input("Enter your phone number")
    borrow=Borrower(name,city,phoneNumber)
    borrow.details()

def lenderDatails():
    name = input("Enter your name ")
    phoneNumber = input("Enter your phone number")
    lender=Lender(name,phoneNumber)
    lender.details()


flag=True
while flag:
    status=input("Welcome to the aid system of the State of Israel, are you borrowing or renting an apartment?")
    if status == 'borrowing':
        borrowingDatails()

    if status == 'renting':
        lenderDatails()
    flag = input("Do you want to log out?")
    if flag == "yes"or flag == 'y':
        flag = False
        print("We are strong together! Together we will win!")





