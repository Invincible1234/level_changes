import pygame
class ObjectManager:
    
    def __init__(self):
        self.objects = []
    
    def push_back(self, object):
        self.objects.append(object)

    def pop_back(self, index):
        if index is None:
            self.objects.pop()
        else:
            self.objects.pop(index)

    def remove(self, object):
        try:
            self.objects.remove(object)
        except ValueError:
            print("No object found!")

    def print_objs(self):
        print(self.objects)
    
#File might be unnecessary, might delete later.