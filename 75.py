class CountIterator:
def __init__(self):
self.counter=0
def __iter__(self):
while 1:
self.counter+=1
yield self.counter