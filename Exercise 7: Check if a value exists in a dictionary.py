# Exercise 7: Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

# Write a Python program to check if value 200 exists in the following dictionary.

# Given:

# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# Expected output:

# 200 present in a dict
def main():
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    valueList:list = sample_dict.values()
    if 200 in valueList:
        print("200 is in sample_dict")
    else:
        print("There is no value of 200.")
if __name__=="__main__":
    main()