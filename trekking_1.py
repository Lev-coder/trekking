import xlrd

class Product():
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

def swap(product_list,i,j):
    tmp = product_list[i]
    product_list[i] = product_list[j]
    product_list[j] = tmp
    
def sort_product(product_calories):
    product_list = []
    for product_name,calories in product_calories.items():
        product_list.append( Product(product_name,calories) )

    for i in range(len(product_list)):
        for j in range( i+1,len(product_list) ):
            product_a = product_list[i]
            product_b = product_list[j]

            if product_a.calories < product_b.calories:
                swap(product_list,i,j)
            elif product_a.calories == product_b.calories:
                if product_a.name > product_b.name:
                    swap(product_list,i,j)

    return product_list

wb = xlrd.open_workbook('trekking1.xlsx')
trekking = wb.sheet_by_index(0)

product_calories = {}
for row in range(1,trekking.nrows):
    product_name = trekking.row_values(row)[0]
    calories = trekking.row_values(row)[1]
    product_calories[product_name] = calories
    
for product in sort_product(product_calories):
    print( product.name )