from apartment import Apartment
from apartment import *

permitCity=['sderot', 'ofakim', 'netivot', 'hotefAza', 'kriat shmona']
d1=Address("Jerusalem", "Har Nof", "Mishklov", 6,10)
a1=Apartment(d1,5,20,True, True)
d2=Address("Bney Brak", "Ramat Elchanan", "Chidooshey Harim", 5,15)
a2=Apartment(d2,4,10,True, False)
pooling=[a1,a2]

def findApartment(conditions):
    maxPercent = 0
    bestApartment=None
    for ap in pooling:
        current=ap.apartmentAdjustment(conditions)
        adjust_check = lambda current, maxPercent: current > maxPercent
        if adjust_check(current, maxPercent):
            maxPercent = current
            bestApartment = ap
    return bestApartment,maxPercent



def addApartment(apartment):
    pooling.append(apartment)
    print(f'Number of apartments in the database: {len(pooling)}')
    validCity(pooling)

def validCity(pooling):
    return [ap for ap in pooling if ap.address.city not in permitCity]