class Iterator:
    def __init__(self, options):
        self.options = options
        self.current = 0
        self.lennn = len(options)

    def __next__(self):
        if shop.command == 'products':
            if self.current < self.lennn:
                exettt = (self.options[self.current][0], self.options[self.current][1],
                          f'index {self.options[self.current][3]}')
                self.current += 1
                print(self.current)
                return exettt

            raise StopIteration
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
                print(i)
        if gnr == 4:
            for i in self.assortement_VN:
                assortements.append(i)
                print(i)
        if gnr == 1:
            for i in self.assortement_shooter:
                assortements.append(i)
                print(i)
        if gnr == 5:
            for i in self.assortement_sandbox:
                assortements.append(i)
                print(i)
        if gnr == 3:
            for i in self.assortement_RPG:
                assortements.append(i)
                print(i)
        print('Ассортимент:', assortements)
        index = int(input('Введите индекс: '))
        index -= 1

        if gnr == 2:
            for i in self.assortement_strategic:
                if i[3] == index:
                    self.byed.append(assortements[i])
                    self.assortement_strategic.pop(a)
                    a += 1
        a = 0
        if gnr == 4:
            for i in self.assortement_strategic:
                print(i[3])
                if i[3] == index:

                    self.byed.append(assortements[i])
                    self.assortement_strategic.pop(a)
                    a += 1
        if gnr == 1:
            for i in self.assortement_strategic:
                if i[3] == index:
                    self.byed.append(assortements[i])
                    self.assortement_strategic.pop(a)
                    a += 1
        if gnr == 5:
            for i in self.assortement_strategic:
                if i[3] == index:
                    self.byed.append(assortements[i])
                    self.assortement_strategic.pop(a)
                    a += 1
        if gnr == 3:
            for i in self.assortement_strategic:
                if i[3] == index:
                    self.byed.append(assortements[i])
                    self.assortement_strategic.pop(a)
                    a += 1





    def __iter__(self):
        gnr = int(input('введите жанр (Шутер 1, Стратегия 2, РПГ 3, Визуальная новелла 4, Песочница 5) '))
        itrt = []
        if gnr == 1:
            itrt = self.assortement_shooter
        if gnr == 2:
            itrt = self.assortement_strategic
        if gnr == 3:
            itrt = self.assortement_RPG
        if gnr == 4:
            itrt = self.assortement_VN
        if gnr == 5:
            itrt = self.assortement_sandbox
        return Iterator(itrt)



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
                print(i)
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


