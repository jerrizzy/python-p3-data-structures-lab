spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    arr = []
    for obj in spicy_foods:
        arr.append(obj["name"])
    return arr

print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    arr = []
    for obj in spicy_foods:
        if obj["heat_level"] > 5:
            arr.append(obj)
    return arr

print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    for obj in spicy_foods:
        print(f'{obj["name"]} ({obj["cuisine"]}) | Heat Level: {obj["heat_level"] * "🌶"}')

print(print_spicy_foods(spicy_foods))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    total = 0
    for food_dict in spicy_foods:
        total += food_dict['heat_level']
    return total / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
