#Case 4: IF super class and Sub class contains same method name with signature.
#Answer: If super class and sub class contains same method name with signature in this case the sub class method hides the super class method.

class CapitalCity:
    def show_city(self, cityname):
        print("The Capital City name is ",cityname)

 
class MetropolitanCity(CapitalCity):
    def __init__(self, cityname):
        super().show_city(cityname)
 
    def show_city(self, cityname):
        print("The Metropolitan City name is ",cityname)
 
 
obj=MetropolitanCity("Bangalore")
obj.show_city("Delhi")