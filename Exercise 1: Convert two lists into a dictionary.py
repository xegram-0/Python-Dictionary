# Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

def main():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    theDict:dict = {key:value for (key,value) in zip(keys,values)}
    #res_dict = dict(zip(keys, values))
    print(theDict)
if __name__=="__main__":
    main()