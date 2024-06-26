# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# Expected output:

# {'name': 'Kelly', 'salary': 8000}
def main():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]

    newDict:dict = dict()
    for key in keys:
        if key in sample_dict:
            newDict.update({key: sample_dict[key]})
    print(newDict)
    #newDict = {k: sampleDict[k] for k in keys}


if __name__=="__main__":
    main()