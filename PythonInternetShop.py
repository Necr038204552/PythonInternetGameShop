import random
class Iterator:
    def __init__(self, options):
        self.options = options
        self.current = 0
        self.lennn = len(options)

    def __next__(self):
        if shop.command == 'products':
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        else:
            if self.current < len(shop.byed):
                exettt = shop.byed[self.current][2] + f' ключь к {shop.byed[self.current][0]}'
                self.current += 1
                print(self.current)
                return exettt
            raise StopIteration




class Shop():
    def __init__(self):
        self.assortement_VN = []
        self.assortement_strategic = []
        self.assortement_shooter = []
        self.assortement_RPG = []
        self.assortement_sandbox = []
        self.command = 'products'
        self.byed = []
    def pluss_game(self, otions, list):
        if list == 'Стратегия':
            self.assortement_strategic.append(otions)
        elif list == 'Визуальная новелла':
            self.assortement_VN.append(otions)
        elif list == 'Шутер':
            self.assortement_shooter.append(otions)
        elif list == 'РПГ':
            self.assortement_RPG.append(otions)
        elif list == 'Песочница':
            self.assortement_sandbox.append(otions)

    def stop_shopping(self):
        self.command = 'key'
    def buy_game(self):
        assortements = []
        gnr = int(input('введите жанр (Шутер 1, Стратегия 2, РПГ 3, Визуальная новелла 4, Песочница 5) '))
        if gnr == 2:
            for i in self.assortement_strategic:
                assortements.append(i)
                print(i[0], i[1], 'index', i[3])
        if gnr == 4:
            for i in self.assortement_VN:
                assortements.append(i)
                print(i[0], i[1], 'index', i[3])
        if gnr == 1:
            for i in self.assortement_shooter:
                assortements.append(i)
                print(i[0], i[1], 'index', i[3])
        if gnr == 5:
            for i in self.assortement_sandbox:
                assortements.append(i)
                print(i[0], i[1], 'index', i[3])
        if gnr == 3:
            for i in self.assortement_RPG:
                assortements.append(i)
                print(i[0], i[1], 'index', i[3])
        index = int(input('Введите индекс: '))



        a = 0
        if gnr == 2:
            for i in self.assortement_strategic:
                if i[3] == index:
                    self.byed.append((assortements[a][0], assortements[a][1], f'index {assortements[a][3]}'))
                    self.assortement_strategic.pop(a)
                    a += 1
        if gnr == 4:
            for i in self.assortement_VN:
                print(i[3])
                if i[3] == index:
                    self.byed.append(assortements[a])
                    self.assortement_VN.pop(a)
                    a += 1
        if gnr == 1:
            for i in self.assortement_shooter:
                if i[3] == index:
                    self.byed.append(assortements[a])
                    self.assortement_shooter.pop(a)
                    a += 1
        if gnr == 5:
            for i in self.assortement_sandbox:
                if i[3] == index:
                    self.byed.append(assortements[a])
                    self.assortement_sandbox.pop(a)
                    a += 1
        if gnr == 3:
            for i in self.assortement_RPG:
                if i[3] == index:
                    self.byed.append(assortements[a])
                    self.assortement_RPG.pop(a)
                    a += 1





    def __iter__(self):




        return Iterator(self.byed)



class newGames:
    def __init__(self, name, genre, key, number):
        self.name = name
        self.genre = genre
        self.key = key
        self.number = number
        self.list = [name, genre, key, number]


def generator2():
    while 1:
        a = 20
        key = ''
        while a > 0:
            a -= 1
            key += str(random.randint(0, 9))
        yield key
def generator():
    number = 1
    while 1:
        name = random.choice(['Борьба за котлету', 'Поход в степи', 'Весть о Николасе', 'Шторм'])
        genre = random.choice(['Шутер', 'Стратегия', 'РПГ', 'Визуальная новелла', 'Песочница'])
        key = next(gen2)
        neworder = newGames(name, genre, key, number)
        number += 1


        shop.pluss_game(neworder.list, genre)
        yield neworder


gen2 = generator2()
gen = generator()
ngames = int(input('Введите колличество игр '))
onoff = True
shop = Shop()


for i in range(ngames):
    next(gen)
while onoff:

    actions = input('купить / список купленных / завершить покупки ')
    if actions == 'купить':
        shop.buy_game()
    elif actions == 'список купленных' or actions == 'список':
        if shop.byed == []:
            print('Корзина пуста')
        else:
            for i in shop.byed:
                print(i[0], i[1], 'index', i[3])
            answer = input('Хотите что то убрать из корзины? ')
            if answer == 'yes' or answer == 'да' or answer == 'yes':
                ind = int(input('Введите индекс: '))
                tumbler = True
                count = 0
                for i in shop.byed:
                    if i[3] == ind:
                        tumbler = False
                        shop.assortement.append(i)
                        shop.byed.pop(count)
                        break
                    count += 1
                if tumbler:
                    print('Данной игры в корзине не найдено.')
    else:
        shop.stop_shopping()
        onoff = False
        for i in shop:
            print(i)
        print('Спасибо за покупки! )')
