#case 2: fixtures at class scope
#Example:
 
class TestProduct:
    def test_create_product(self,setup_class):
        print("The product demoProduct has created successfully!!")
 
    def test_modify_product(self,setup_class):
        print("The product demoProduct has modified successfully!!")
 
    def test_delete_product(self,setup_class):
        print("The product demoProduct has deleted successfully!!")