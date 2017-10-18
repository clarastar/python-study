# class Clara:
#     def __init__(self):
#         print('Blablablabla')
#
#     def swim(self):
#         print('I am swimming')
#
#
# flipper = Clara()
# flipper.swim()


class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)


jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()
