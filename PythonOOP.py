x = [1, 2, 3]
a = [x, x, x]
print(a)
a[1][2] = 100
print(a)

class Gods:
    pass

thanatass = Gods()
mars = Gods()
venera = Gods()
print(venera)

x = [1, 2, 3]
y = [x, x, x]
y[1][2]=120
print(x)

# class Cats:
#     def __init__(self, name_of_the_cat, age_of_the_cat):
#         self.name = name_of_the_cat
#         self.age = age_of 

# murka = Cats()
# barsik = Cats()
# valera = Cats()

# print(murka.age)
# print(barsik.age)
# print(valera.age)


# class Cats:
#     def __init__(self, name_of_the_cat, age_of_the_cat, power_of_the_cat, eyes_color_of_the_cat):
#         self.name = name_of_the_cat
#         self.age = age_of_the_cat
#         self.power = power_of_the_cat
#         self.eyes = eyes_color_of_the_cat

# murka = Cats(name_of_the_cat = 'Murka', age_of_the_cat = 8, power_of_the_cat = 88, eyes_color_of_the_cat = 'blue')
# barsik = Cats(name_of_the_cat = 'Barsik', age_of_the_cat = 9, power_of_the_cat = 99, eyes_color_of_the_cat = 'green')
# pushok = Cats(name_of_the_cat = 'Pushok', age_of_the_cat = 7, power_of_the_cat = 77, eyes_color_of_the_cat = 'yellow')

# our_cats = [murka, barsik, pushok]

# for cat in our_cats:
#     print('This is', cat.name)

class Cats:
    def __init__(self, name, age, health, hit_power, lives, eyes, color):
        self.name = name
        self.age = age
        self.health = health
        self.hit_power = hit_power
        self.eyes = eyes
        self.color = color
        self.lives = lives

    def meow(self):
        print(f'{self.name}', 'is saying meow')

    def greeting(self):
        print('Hi, my name is: ',f'{self.name}', 'I\'m ', f'{self.age}')

    def hit(self, other):
        other.health -= self.hit_power
    
    def is_dead(self):
        return self.health <= 0




murka = Cats(name = 'Murka', age = 8, health = 88, hit_power = 80, life = 8, eyes = 'blue', color = 'black')
barsik = Cats(name = 'Barsik', age = 9, health = 99, hit_power = 9, life = 9, eyes = 'green', color = 'white')
pushok = Cats(name = 'Pushok', age = 7, health = 77, hit_power = 1, life = 2, eyes = 'yellow', color = 'redish')

our_cats = [murka, barsik, pushok]

for cat in our_cats:
    cat.meow()
    cat.greeting()

murka.hit(barsik)
print('Murka hit the Barsik. Barsik\'s health:', f'{barsik.health}')
if barsik.is_dead():
    print('RIP Barsik')


murka.hit(pushok)
print('Murka hit the Pushok. Pushok\'s health:', f'{pushok.health}')
if pushok.is_dead():
    print('RIP Pushok')




    