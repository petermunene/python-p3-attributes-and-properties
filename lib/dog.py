#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="doggo", breed="Mastiff"):
        self.name=name
        self.breed=breed
    @property
    def name  (self):
        return self._name
    @name.setter
    def name (self,value):
        if not isinstance(value, str) or not (1<len(value)<25):
            print('Name must be string between 1 and 25 characters.')
        else :
            self._name=value


    @property
    def breed(self):
        return self._breed 
    @breed.setter
    def breed (self,breed_name):
        if breed_name in (APPROVED_BREEDS):
            self._breed=breed_name
        else :
            print("Breed must be in list of approved breeds.")
    pass
