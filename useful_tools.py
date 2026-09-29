import random

feet_in_mile = 5200
metres_in_kilometre = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "ingo Star"]


def get_file_exit(filname):
    return filname[filname.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)
