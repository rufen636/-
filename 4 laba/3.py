class TransportVehicle:
    def __init__(self, name, speed, cost_per_km):
        self.name = name
        self.speed = speed
        self.cost_per_km = cost_per_km

    def move(self, distance):
        raise NotImplementedError("Метод должен быть переопределен в дочерних классах")


class Airplane(TransportVehicle):
    def __init__(self, name, speed, cost_per_km):
        super().__init__(name, speed, cost_per_km)

    def move(self, distance):
        travel_time = distance / self.speed
        travel_cost = distance * self.cost_per_km
        return travel_time, travel_cost


class Train(TransportVehicle):
    def __init__(self, name, speed, cost_per_km):
        super().__init__(name, speed, cost_per_km)

    def move(self, distance):
        travel_time = distance / self.speed
        travel_cost = distance * self.cost_per_km * 0.8
        return travel_time, travel_cost


class Car(TransportVehicle):
    def __init__(self, name, speed, cost_per_km):
        super().__init__(name, speed, cost_per_km)

    def move(self, distance):
        travel_time = distance / self.speed
        travel_cost = distance * self.cost_per_km * 1.2
        return travel_time, travel_cost


def find_optimal_travel_mode(distance, vehicles):
    fastest_vehicle = None
    cheapest_vehicle = None
    min_time = float("inf")
    min_cost = float("inf")

    for vehicle in vehicles:
        time, cost = vehicle.move(distance)

        if time < min_time:
            min_time = time
            fastest_vehicle = vehicle

        if cost < min_cost:
            min_cost = cost
            cheapest_vehicle = vehicle

    return fastest_vehicle, min_time, cheapest_vehicle, min_cost


airplane = Airplane("Самолет", 900, 5)
train = Train("Поезд", 120, 2)
car = Car("Автомобиль", 100, 8)

distance = 500

fastest, fastest_time, cheapest, cheapest_cost = find_optimal_travel_mode(
    distance, [airplane, train, car]
)

print(f"Наиболее быстрая поездка: {fastest.name}. Время: {fastest_time} часов.")
print(f"Наиболее экономичная поездка: {cheapest.name}. Стоимость: {cheapest_cost} у.е.")
