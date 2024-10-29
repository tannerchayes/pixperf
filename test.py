
message_for_the_user = "Hello World! It's nice to meet you."
number_of_coffees = 2.0
days_per_week = 5.0
coffees_per_week = number_of_coffees * days_per_week

print(message_for_the_user)
print('Cups per week: ', coffees_per_week)

fruits = [
    'apple',
    'pear',
    'peach',
]

for fruit in fruits:
    print('Fruit that I like: ', fruit)
    print('------------')

car = {
    'wheels': 4,
    'doors': 2,
    'glass': 10,
}

print('Number of wheels', car['wheels'])
print('Number of seats', car.get('seats', 'no seats found'))


def color_mix(red=None, blue=None, green=None):

    # Cool comment

    return '#' + red + blue + green


print(color_mix(red='EB', green='33', blue='CB'))


class JamesBondCar(object):

    def vroom(self):
        pass

    def stop(self):
        pass

    def eject(self):
        pass


bond_car = JamesBondCar()
