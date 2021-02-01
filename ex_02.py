class Road:

    def total_asphalt(self, length, width):
        self._lenght = length
        self._width = width
        asphalt_volume = length * width * 25 * 10
        print(f'{length}m * {width}m * 25kg * 10cm = {asphalt_volume}')


city_road = Road()
city_road.total_asphalt(34, 15)
#