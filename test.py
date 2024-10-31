
# Basic Python

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

# Reading files

with open('index.html', "r") as test_file:
    # Read it
    template = test_file.read()

    context = {
        'heading': "SURF & PADDLE CO. BLOG",
        'blog_posts': """
            <div class="group relative h-[300px] w-[270px]">
                <img class="absolute inset-0 object-cover w-full h-full" src="img/Surf-Ad.jpeg">
                <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                <div class="relative">
                <h2 class="text-gray-600 text-lg align-text-bottom">Another Cool Post</h2>
                </div>
            </div>
    
            <div class="group relative h-[300px] w-[270px]">
                <img class="absolute inset-0 object-cover w-full h-full" src="img/Surf-Ad.jpeg">
                <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                <div class="relative">
                <h2 class="text-gray-600 text-lg">Post Title</h2>
                </div>
            </div>
    
            <div class="group relative h-[300px] w-[270px]">
                <img class="absolute inset-0 object-cover w-full h-full" src="img/Surf-Ad.jpeg">
                <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                <div class="relative">
                <h2 class="text-gray-600 text-lg">Another Longer Post Title</h2>
                </div>
            </div>
    
            <div class="group relative h-[300px] w-[270px]">
                <img class="absolute inset-0 object-cover w-full h-full" src="img/Surf-Ad.jpeg">
                <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                <div class="relative">
                <h2 class="text-gray-600 text-lg">Oh Cool, A Post!</h2>
                </div>
            </div>
        """,
        'nav_links': """
            <a href="#" class="text-white mr-10">ABOUT</a>
            <a href="#" class="text-white mr-5">SEARCH</a>
        """,
    }

    processed_template = template
    for ctx_variable in context.keys():
        processed_template = processed_template.replace('{{ ' + ctx_variable + ' }}', context.get(ctx_variable))

    # print
    print(processed_template)
