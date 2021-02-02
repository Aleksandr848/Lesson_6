from time import sleep


class TrafficLight:
    __color = "Red"

    def running(self):
        while True:
            print(TrafficLight.__color)
            sleep(7)
            TrafficLight.__color = "Yellow"
            print(TrafficLight.__color)
            sleep(2)
            TrafficLight.__color = "Green"
            print(TrafficLight.__color)
            sleep(5)
            TrafficLight.__color = "Red"


light = TrafficLight()
light.running()
