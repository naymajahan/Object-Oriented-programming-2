### inheritance help methods and isinstance and issubclass methods

class robot:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def move_forward(self):
        print(f'{self.name} is moving forward')

    def move_backward(self):
        print(f'{self.name} is moving backword')

    def move_right(self):
        print(f'{self.name}, is moving right')

    def move_left(self):
        print(f'{self.name}, is moving left')



### class inheritance using


class HouseBot(robot):
    def __init__(self, name, version, area_coverd):
        super().__init__(name, version)
        self.area_coverd = area_coverd


    def clean(self):
        if self.area_coverd > 0:
            print(f'{self.name}, is cleaning the house')
            self.area_coverd -= 30

            if self.area_coverd < 0:
                self.area_coverd = 0


        else:
            print('CANNOT CLEAN! PLEASE RESET THE AREA COVERED PARAMETER')

    def set_coverd_area(self, area):
        if self.area_coverd == 0:
            self.area_coverd = area

        else:
            print('I CAN STILL CLEAN MORE AREA')


    @staticmethod
    def halt():
        print('I AM HALTING')


    # ## method overwriting the forward method
    def move_forward(self):
        print('THIS IS IN HOUSEBOT CLASS!')
        super().move_forward()




#hBot = HouseBot('hBot', 1.1, 40)
#print(hBot.name)
#hBot.move_forward()


houseBot = HouseBot('Bob', 1.2, 50)
robo = robot('Stan Lee', 1.5)
"""
print(houseBot.name)
print(houseBot.version)
houseBot.move_forward()
houseBot.move_right()
houseBot.clean()
houseBot.clean()
houseBot.clean()
print(houseBot.area_coverd)
houseBot.set_coverd_area(58)
houseBot.clean()

"""

print(help(robot))
print(help(HouseBot))

print(issubclass(HouseBot, robot))

print(issubclass(robot, HouseBot))
print(issubclass(robot, object))
print(issubclass(HouseBot, object))


print(isinstance(houseBot, robot))
print(isinstance(houseBot, HouseBot))
print(isinstance(houseBot, object))

print(isinstance(robo, object))

