
class Address:
    def __init__(self, city, neighborhood, street="",buildingNumber=0, apartmentNumber=0):
        self.city=city
        self.neighborhood=neighborhood
        self.street=street
        self.buildingNumber=buildingNumber
        self.apartmentNumber=apartmentNumber

class Apartment:
    def __init__(self, address, numRooms, numBeds,crib=False,accessibility=False):
        self.address=address
        self.numRooms = numRooms
        self.numBeds = numBeds
        self.crib=crib
        self.accessibility=accessibility

    def apartmentAdjustment(self, conditons):
        percent=100
        if self.address.city!= conditons['address'].city:
            percent=percent-30
        if self.address.neighborhood != conditons['address'].neighborhood:
            percent=percent-3
        if self.numRooms < conditons['numRooms']:
            percent=percent-5
        if self.numBeds < conditons['numBeds']:
            less = conditons['numBeds'] - self.numBeds
            percent=percent-(less * 2)
        if self.crib == False and conditons['crib'] == True:
            percent =percent-7
        if self.accessibility == False and conditons['accessibility'] == True:
            percent = 0
        return percent









