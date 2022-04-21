from random import  randint

tank_size = randint(10, 25)
miles_covered = randint(200, 400)
#
print("tank size:", tank_size)
print("miles covered:", miles_covered)
#
def calculate_mpg(tank_size, miles_covered):
    mpg = miles_covered / tank_size
    return mpg
#
def calculate_mpg_floor(tank_size, miles_covered):
    mpg = miles_covered // tank_size
    return mpg

print("This vehicle gets {} miles per gallon.".format(calculate_mpg(tank_size, miles_covered)))


