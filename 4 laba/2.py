class Country:
    def __init__(self, name, capital, area, population):
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population

    def __str__(self):
        return f"{self.name} (Столица: {self.capital}, Площадь: {self.area} км², Население: {self.population} чел.)"


countries = [
    Country("Россия", "Москва", 17098242, 146599183),
    Country("Канада", "Оттава", 9976140, 37664517),
    Country("Китай", "Пекин", 9596961, 1439323776),
    Country("Бразилия", "Бразилиа", 8515767, 213993437),
    Country("Австралия", "Канберра", 7692024, 25550683),
]


def print_countries(sorted_countries, characteristic):
    print(f"Список стран по {characteristic}:\n")
    for country in sorted_countries:
        print(country)
    print("\n")


2
countries_by_area = sorted(countries, key=lambda x: x.area)
print_countries(countries_by_area, "площади")


countries_by_population = sorted(countries, key=lambda x: x.population)
print_countries(countries_by_population, "численности населения")
