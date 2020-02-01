import xlrd

def medianSalary(salarys):
    salarys.sort()
    if len(salarys) % 2 == 0:
        return ( salarys[len(salarys)//2] + salarys[len(salarys)//2 + 1] ) / 2
    else:
        return salarys[len(salarys)//2]

def max_region_medianSalary(salaries):
    print("-------------------------")

    region_medianSalary = {}

    for i in range(1,salaries.nrows):
        region = salaries.row_values(i)[0]
        salarys = salaries.row_values(i)[1:]
        region_medianSalary[medianSalary(salarys)] = region

    for key in region_medianSalary:
        print("{} => {}".format(key,region_medianSalary[key]))

    print(">>> max {}".format(region_medianSalary[max(region_medianSalary)]))

def sum_salary(salaries,this_col):
    sum = 0

    for i in range(1,salaries.nrows):
        salary = salaries.row_values(i)[this_col]
        sum += salary

    return sum

def max_prof_salary(salaries):
    print("----------------")

    num_regions = salaries.nrows - 1
    salary_prof = {}
    for i in range(1,salaries.ncols):
        prof = salaries.col_values(i)[0]
        salary_prof[sum_salary(salaries,i) / num_regions] = prof

    for salary in salary_prof:
        print("{} => {}".format(salary,salary_prof[salary]))
    print(">>> max {} ".format(salary_prof[max(salary_prof)]))

wb = xlrd.open_workbook('salaries.xlsx')
salaries = wb.sheet_by_index(0)

max_region_medianSalary(salaries)
max_prof_salary(salaries)




