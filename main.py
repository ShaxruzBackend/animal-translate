
animals = {
    'wolf': 'Buri',
    'shark':"akula",
    "elephan":'fil',
    'monkey':'maymun',
    "bird":"qush",
    "sparrow":"chumchuq",
    "lion ":"yolbars",
    "bear":"ayiq",
    "tutle":"toshbaqa",
    "rabbit ":'quyon',
    "cat":'mushuk',
    'cow':"sigir",
    'horse':'ot',
    'hen':'tovuq',
    'rooster':"xo'roz",
    'fish':'baliq',
    "sheep":'qoy',
    'crocodile':'timsox',
    'jiraffa':'jirafa',
    'snake':"ilon"

}
animal = input("Eng xayvon kiriting: ").lower()
x = 0
try:
    print(animals[animal])
    x += 1
except KeyError:
    animals_list = []

    for i in animals.values():
        animals_list.append(i.lower())

    if animal in animals_list:
        x += 2
        for key, value in animals.items():
            if value == animal:
                print(key)

    else:
        print("Bunaqa hayvon mavjud emaas! ")
finally:
    if x == 1:
        print("Translated ENG -> UZB")
    elif x == 2:
        print("Translated UZB -> ENG")
