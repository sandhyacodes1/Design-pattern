
#This is a simple food ordering system pattern created as a software enginnering project part
class Pizza:
    def prepare(self):
     print("Pizza is prepared")
class Burger:
     def prepare(self):
        print("Burger is prepared")

class Pasta:
    def prepare(self):
        print("Pasta is prepared")
class Food:
      @staticmethod
      def Food_type(food_name):
        if food_name == "pizza":
            print ("Pizza found")
        elif food_name == "burger":
          print("burger found")
        elif food_name == "pasta":
            print("Pasta found")
        else:
          print("Error")
object = Food.Food_type("burger") 
object.prepare()
