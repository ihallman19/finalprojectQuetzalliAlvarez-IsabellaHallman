class MenuItem: #By Quetzalli
    def __init__(self, name:str, location:str, calories:int, vegan:bool, vegetarian:bool, gluten_free:bool):
        self.name = name
        self.location = location
        self.calories = calories
        self.vegan = vegan
        self.vegetarian = vegetarian
        self.gluten_free = gluten_free

data = [MenuItem("cheeseburger", "Brunch", 550, False, False, False),
            MenuItem("turkey taco bowl", "Balance Cafe", 335, True, True, True),
            MenuItem("classic grilled cheese", "Mingle", 467, False, True, False),
            MenuItem("marinated ahi bowl", "NOSH", 740, False, False, False),
            MenuItem("spicy italian", "Subway", 790, False, False, False),
            MenuItem("cheddar cheese egg sandwich", "Einstein Bros. Bagels", 430, False, True, False),
            MenuItem("bean and cheese burrito", "Picos", 460, False, True, False),
            MenuItem("blackened salmon salad", "Streats", 640, False, False, True),
            MenuItem("Ceasar Salad", "Hearth", 240, False, True, False),
            MenuItem("chicken alfredo", "Noodles", 740, False, False, False),
            MenuItem("plain bagel", "Starbucks", 240, True, True, False),
            MenuItem("mango-a-go-go", "Jamba", 240, False, True, True),
            MenuItem("hot hunny bagel", "Julians", 775, False, False, False),
            MenuItem("house milk tea", "Sequel Tea", 340, False, True, False),
            MenuItem("kale and sweet potato salad", "Red Radish", 315, False, False, False),
            MenuItem("basic wrap", "Pom and Hunny", 230, False, False, False),
            MenuItem("glass noodles", "Poly Choice", 170, False, False, False),
            MenuItem("chick fill a nuggets", "Chick Fill A", 250, False, False, False),
            MenuItem("southwestern grilled chicken salad", "Balance Cafe", 250, False, False, True),
            MenuItem("garlic fries", "Balance Cafe", 80, True, True, True)] #By Quetzalli