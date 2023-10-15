try:
    class Player:

        def __init__(self,name):
            self.maxhp = 100
            self.name = name
            self.Health = 100
            self.score = 0


        def show_info(self):
            print(f'Name:{self.name}\nHealth: {self.Health}\nscore: {self.score}')

        def set_name(self,new_name):
            self.name = new_name

        def set_Health(self,new_hp):
            if new_hp <= 100:
                self.Health = new_hp

        def set_score(self, new_score):
            if new_score >= 0:
                self.score = new_score

        def player_alive(self):
            return self.Health > 0
    player = Player('no name')
    player.set_name(input('set name\n'))
    player.set_Health(int(input('set Health, <= 100 and > 0\n')))
    player.show_info()

    from random import randint
    from time import sleep

    while player.player_alive():
        num = randint(1, 2)
        sleep(1)
        print('             ',num)
        if num == 1:
            player.set_Health(player.Health - 10)
            print(player.Health)
        if num == 2:
            if player.Health > 20:
                player.set_score(player.score + 1)
                print('     ',player.score)
            else:
                player.Health = player.Health + 20
                print(player.Health)
    print("player's dead")
except:
    print('code break')