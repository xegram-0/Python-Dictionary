# Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def merge2dict(dict1:dict,dict2:dict):
    #print(dict1,dict2)

    # dict1.update(dict2)
    # print(dict1)
    # update() method needs seperate line for it 
    # before printing the result
    mergeDict:dict = dict1 | dict2
    print(mergeDict)

def main():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    merge2dict(dict1,dict2)
if __name__=="__main__":
    main()