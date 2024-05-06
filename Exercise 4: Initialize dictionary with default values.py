# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

# Given:

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# Expected output:

# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
def main():
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    newDict:dict = dict.fromkeys(employees,defaults)
    print(newDict)
if __name__=="__main__":
    main()