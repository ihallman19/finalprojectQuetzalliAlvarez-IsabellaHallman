#By Isabella
from menuDef import MenuItem
import functions
import unittest
data = [MenuItem("cheeseburger", "Brunch", 550, False, False, False),
            MenuItem("turkey taco bowl", "Balance Cafe", 335, True, True, True),
            MenuItem("classic grilled cheese", "Mingle", 467, False, True, False),
            MenuItem("marinated ahi bowl", "NOSH", 0, False, False, False),
            MenuItem("spicy italian", "Subway", 790, False, False, False),
            MenuItem("cheddar cheese egg sandwich", "Einstein Bros. Bagels", 430, False, True, False),
            MenuItem("bean and cheese burrito", "Picos", 460, False, True, False),
            MenuItem("blackened salmon salad", "Streats", 0, False, False, True),
            MenuItem("Ceasar Salad", "Hearth", 0, False, True, False),
            MenuItem("chicken alfredo", "Noodles", 0, False, False, False),
            MenuItem("plain bagel", "Starbucks", 240, True, True, False),
            MenuItem("mango-a-go-go", "Jamba", 240, False, True, True),
            MenuItem("hot hunny bagel", "Julians", 775, False, False, False),
            MenuItem("house milk tea", "Sequel Tea", 340, False, True, False),
            MenuItem("kale and sweet potato salad", "Red Radish", 315, False, False, False),
            MenuItem("basic wrap", "Pom and Hunny", 230, False, False, False),
            MenuItem("glass noodles", "Poly Choice", 170, False, False, False),
            MenuItem("chick fill a nuggets", "Chick Fill A", 250, False, False, False),
            MenuItem("southwestern grilled chicken salad", "Balance Cafe", 250, False, False, True),
            MenuItem("garlic fries", "Balance Cafe", 0, True, True, True)]

class TestCases(unittest.TestCase):
    def test_healthy1(self):
        input = data
        input2 = 80
        result = functions.healthy(input, input2)
        expected = []
        self.assertEqual(result,expected)
    def test_healthy2(self):
        input = data
        input2 = 170
        result = functions.healthy(input, input2)
        expected = ["glass noodles"]
        self.assertEqual(result,expected)
    def test_restaurant1(self):
        input = data
        input2 = 'Balance Cafe'
        input3 = 400
        result = functions.restaurant(input, input2, input3)
        expected = ['turkey taco bowl', 'southwestern grilled chicken salad']
        self.assertEqual(result,expected)
    def test_restaurant2(self):
        input = data
        input2 = 'Julians'
        input3 = 800
        result = functions.restaurant(input, input2, input3)
        expected = ["hot hunny bagel"]
        self.assertEqual(result,expected)
    def test_vegan1(self):
        input = data
        input2 = 'Brunch'
        result = functions.vegan(input, input2)
        expected = []
        self.assertEqual(result,expected)
    def test_vegan2(self):
        input = data
        input2 = 'Starbucks'
        result = functions.vegan(input, input2)
        expected = ["plain bagel"]
        self.assertEqual(result,expected)
    def test_vegetarian1(self):
        input = [MenuItem("cheeseburger", "Brunch", 550, False, False, False), MenuItem("classic grilled cheese", "Mingle", 467, False, True, False)]
        result = functions.vegetarian(input)
        expected = ["classic grilled cheese"]
        self.assertEqual(result,expected)
    def test_vegetarian2(self):
        input = [MenuItem("plain bagel", "Starbucks", 240, True, True, False), MenuItem("mango-a-go-go", "Jamba", 240, False, True, True)]
        result = functions.vegetarian(input)
        expected = ['plain bagel', 'mango-a-go-go']
        self.assertEqual(result,expected)
    def test_gluten_free1(self):
        input = [MenuItem("classic grilled cheese", "Mingle", 467, False, True, False), MenuItem("marinated ahi bowl", "NOSH", 0, False, False, False)]
        result = functions.gluten_free(input)
        expected = ['classic grilled cheese']
        self.assertEqual(result,expected)
    def test_gluten_free2(self):
        input = [MenuItem("plain bagel", "Starbucks", 240, True, True, False), MenuItem("mango-a-go-go", "Jamba", 240, False, True, True)]
        result = functions.gluten_free(input)
        expected = ['plain bagel', 'mango-a-go-go']
        self.assertEqual(result,expected)
    def test_missing_cals1(self):
        input = [MenuItem("marinated ahi bowl", "NOSH", 0, False, False, False)]
        result = functions.missing_cals(input)
        expected = ['marinated ahi bowl']
        self.assertEqual(result,expected)
    def test_missing_cals2(self):
        input = [MenuItem("southwestern grilled chicken salad", "Balance Cafe", 250, False, False, True)]
        result = functions.missing_cals(input)
        expected = []
        self.assertEqual(result,expected)
    def test_healthy_location1(self):
        input = data
        result = functions.healthy_location(input)
        expected = {'Brunch': 550, 'Balance Cafe': 585, 'Mingle': 467, 'NOSH': 0, 'Subway': 790, 'Einstein Bros. Bagels': 430, 'Picos': 460, 'Streats': 0, 'Hearth': 0, 'Noodles': 0, 'Starbucks': 240, 'Jamba': 240, 'Julians': 775, 'Sequel Tea': 340, 'Red Radish': 315, 'Pom and Hunny': 230, 'Poly Choice': 170, 'Chick Fill A': 250}
        self.assertEqual(result,expected)
    def test_healthy_location2(self):
        input = [MenuItem("ham and cheese croissant","Scouts",3000, False, False, True)]
        result = functions.healthy_location(input)
        expected = {"Scouts": 3000}
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()