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

class MenuProduct():
    def __init__(self,name,weight):
        self.name = name 
        self.weight = weight

def calc_product_attributes(product,weight,weight_standard = 100):
    calories = (product.calories*weight )/weight_standard
    protein = (product.protein*weight )/weight_standard
    fats = (product.fats*weight )/weight_standard
    carbohydrate = (product.carbohydrate*weight )/weight_standard

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

def get_dict_days_menu(wd):
    trekking = wb.sheet_by_index(1)
    dict_days_menu = {}
    for row in range(1,trekking.nrows):

        day = trekking.row_values(row)[0]
        name = trekking.row_values(row)[1]
        weight = trekking.row_values(row)[2]

        if day not in dict_days_menu:
            dict_days_menu[day] = []

        dict_days_menu[day].append( MenuProduct(name,weight) )
    return dict_days_menu

def get_sum_products_attributes(list_menu,dict_products):
    sum_products_attributes = Product()
    for product in list_menu:
        if product.name in dict_products:
            sum_products_attributes += calc_product_attributes(dict_products[product.name],product.weight)
    sum_products_attributes.floor_attributes()

    return  sum_products_attributes

wb = xlrd.open_workbook('trekking3.xlsx')

dict_products = get_dict_product(wb)
dict_days_menu = get_dict_days_menu(wb)

day_sumAtrimutes = {}
for day in dict_days_menu:
    day_sumAtrimutes[day] = get_sum_products_attributes(dict_days_menu[day],dict_products)

for sumAtrimutes in day_sumAtrimutes.values():
    print("{} {} {} {}".format(sumAtrimutes.calories,
                            sumAtrimutes.protein,
                            sumAtrimutes.fats,
                            sumAtrimutes.carbohydrate))
