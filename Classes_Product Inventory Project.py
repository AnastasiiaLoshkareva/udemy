# CLASSES
# Product Inventory Project
# Create an application which manages an inventory of products. 
# Create a product class which has a price, id, and quantity on hand. 
# Then create an inventory class which keeps track of various products and can sum up the inventory value.

# Create a new object Product
class Product():
    # Special method to initialize the attributes of an object
    def __init__(self, product_name,product_id, price, quantity):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f'Product {self.product_name} has id={self.product_id}, the price={self.price},quantity={self.quantity}'

#Create a new object Inventory 
class Inventory():
    # to keep track of various products - create a dictionary of products
    dic = {}
  
    def __init__(self):
        pass
    
    #to delete product from dictionary
    def withdraw_product(self,product):
        self.dic.pop(product.product_id)
        print(f'product {product.product_name} was deleted')
        
    #to decrease quantity of product in stock
    def decrease_quantity(self,product,subtract_value):
        self.dic[product.product_id] = self.dic[product.product_id] - subtract_value
        print(f'The quantity of the product {product.product_name} was decreased')
        
    #method that sums up inventory value
    def sum_up(self,product):
        self.dic[product.product_id] = product.quantity * product.price
        print(f'product {product.product_name} was added')
        
    def __str__(self):
        return f'inventory is: {self.dic}'
        
    
# Create an instance of Product = computer
computer = Product(product_name='Computer',product_id=1, price=100, quantity=10)
print(computer)

# Create an instance of Product = phone
phone = Product(product_name='Phone',product_id=2, price=50, quantity=5)
print(phone)

#Create an instance of Inventory
new_stock = Inventory()

#add sum up for a product=computer into inventory(new_stovk instance)
new_stock.sum_up(computer)

#add sum up for a product=phone into inventory(new_stovk instance)
new_stock.sum_up(phone)

#check the inventory
print(new_stock)

#Decrease the quantity of the product in inventory
new_stock.decrease_quantity(computer,800)

#check the inventory
print(new_stock)

#delete product from the inventory
new_stock.withdraw_product(computer)

#check the inventory
print(new_stock)

if __name__ == '__main__':
    main()
