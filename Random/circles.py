
import math
from random import randint
import cProfile

# The map area
# You can experiment with the values
# to see how that affects cProfile results.

MIN_LONG = -1000000
MAX_LONG = 1000000

MIN_LAT = -1000000
MAX_LAT = 1000000

MIN_RADIUS = 2000
MAX_RADIUS = 40000

DISK_COUNT = 2000000


# These two functions are used
# to create unique ids for the disks.
# They use decorators, I just copied
# the code from StackOverflow.

def static_vars(**kwargs):
    
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
        
    return decorate


@static_vars(ids = [0])
def get_unique_id():
    
    last_id = get_unique_id.ids[-1]
    new_id = last_id + 1
    get_unique_id.ids.append(new_id)
    
    return new_id


# Use the Pythagorean theorem
# to determine if a disk contains
# a point with the x and y coordinates.
# Returns true if the disk does contain the point.
  
def contains_point(disk, x, y):
    
    lat = disk[0]
    long = disk[1]
    radius = disk[2]
    
    distance = math.sqrt((lat - x)**2 + (long - y)**2)
    
    ret_value = False
    
    if distance <= radius:
        ret_value = True
        
    return ret_value
        

# This is the function from the task's general API
# It is a bit strange that batch_create()
# should accept a list of disks
# but we can fix it later.
# Maybe it is because batch_create()
# is supposed to accept a list
# and return that 'data structure'
# we are supposed to create.

def batch_create():
    
    disks = list()
    
    # create the specified number of disks
    for _ in range(DISK_COUNT):
        # lat, long and radius are all
        # random integers from the specified range
        lat = randint(MIN_LAT, MAX_LAT)
        long = randint(MIN_LONG, MAX_LONG)
        radius = randint(MIN_RADIUS, MAX_RADIUS)
        id = get_unique_id()
        
        disk = (lat, long, radius, id)
        disks.append(disk)
        
    return disks


# The other General API function
# This is the 'naive' solution
# because it simply loops through
# all the disks and doesn't attempt
# any optimizations
    
def query(disks, lat, long):
    
    results = list()
    
    for disk in disks:
        if contains_point(disk, lat, long):
            results.append([disk, lat, long])
            
    return results


def main():
    
    # use random integers for the coordinates
    # of the point that is or is not
    # contained in disks.
    lat = randint(MIN_LAT, MAX_LAT)
    long = randint(MIN_LONG, MAX_LONG)
    
    # create the disks
    disks = batch_create()
    
    # get the disks that contain our point
    results = query(disks, lat, long)
    
    # print the results:
    # disk lat, disk long, disk radius, disk id, point x, point y
    for result in results:
        print(result)

if __name__ == '__main__':
    
    cProfile.run('main()')
