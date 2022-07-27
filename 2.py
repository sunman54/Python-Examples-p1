class Fruits:
    def __init__(self, ID, Fruit_Name, Fruit_Color, Quantity):
        self.ID = ID
        self.Fruit_Name = Fruit_Name
        self.Fruit_Color = Fruit_Color
        self.Quantity = Quantity

Fruit_Basket = [Fruits(1,'Banana', 'Yellow', 5),
                Fruits(2,'Apple', 'Red', 4),
                Fruits(3,'Lemon', 'Yellow', 7),
                Fruits(4,'Strawberry', 'Red', 2),
                Fruits(5,'Watermelon', 'Green', 8),
                Fruits(6,'Lime', 'Green', 10)]

result = 0
 
 
for fruits in Fruit_Basket:
    if fruits.Fruit_Color == 'Green':
        result += fruits.Quantity

print('Number of  Green fruits is :', result)