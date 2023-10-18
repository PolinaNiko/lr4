import time


class ConsoleColors:
    RESET = "\033[0m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"


class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        while True:
            if self.__color == "red":
                print(ConsoleColors.RED + "Красный свет. Стойте!" + ConsoleColors.RESET)
                time.sleep(7)
                self.__color = "yellow"
            elif self.__color == "yellow":
                print(ConsoleColors.YELLOW + "Желтый свет. Приготовьтесь!" + ConsoleColors.RESET)
                time.sleep(2)
                self.__color = "green"
            elif self.__color == "green":
                print(ConsoleColors.GREEN + "Зеленый свет. Идите!" + ConsoleColors.RESET)
                time.sleep(5)
                self.__color = "red"


traffic_light = TrafficLight()
traffic_light.running()
