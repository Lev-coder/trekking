import xlrd
import math

class Product():
    def __init__(self,calories=0,protein=0,fats=0,carbohydrate=0):
        self.calories = calories
        self.protein = protein
        self.fats = fats
        self.carbohydrate = carbohydrate
    
    def __add__(self, other):
        self.calories += other.calories
        self.protein += other.protein
        self.fats += other.fats
        self.carbohydrate += other.carbohydrate
        return self

    def floor_attributes(self):
        self.calories = math.floor(self.calories)
        self.carbohydrate = math.floor(self.carbohydrate)
        self.protein = math.floor(self.protein)
        self.fats = math.floor(self.fats)
        return self

def calc_product_attributes(product,weight):
    calories = (product.calories*weight )/100
    protein = (product.protein*weight )/100
    fats = (product.fats*weight )/100
    carbohydrate = (product.carbohydrate*weight )/100

    return Product(calories,protein,fats,carbohydrate)

def clean_attribute(attribute):
    if attribute == '':
        return 0
    return attribute
        
def get_dict_product(wb):
    trekking = wb.sheet_by_index(0)
    dict_products = {}
    for row in range(1,trekking.nrows):

        name = trekking.row_values(row)[0]
        calories = clean_attribute(trekking.row_values(row)[1])
        protein = clean_attribute(trekking.row_values(row)[2])
        fats= clean_attribute(trekking.row_values(row)[3])
        carbohydrate = clean_attribute(trekking.row_values(row)[4])

        dict_products[name] = Product(calories,protein,fats,carbohydrate)
    return dict_products

def get_dict_menu(wd):
    trekking = wb.sheet_by_index(1)
    dict_menu = {}
    for row in range(1,trekking.nrows):

        name = trekking.row_values(row)[0]
        weight = trekking.row_values(row)[1]

        dict_menu[name] = weight
    return dict_menu

wb = xlrd.open_workbook('trekking2.xlsx')

dict_products = get_dict_product(wb)
dict_menu = get_dict_menu(wb)

sum_product = Product()
for product in dict_products:
    if product in dict_menu:
        sum_product += calc_product_attributes(dict_products[product],dict_menu[product])
    
sum_product.floor_attributes()

print("{} {} {} {}".format(sum_product.calories,
                        sum_product.protein,
                        sum_product.fats,
                        sum_product.carbohydrate))
