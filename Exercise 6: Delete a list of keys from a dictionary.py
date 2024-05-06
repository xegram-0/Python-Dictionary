# Exercise 6: Delete a list of keys from a dictionary
# Given:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

# Expected output:

# {'city': 'New york', 'age': 25}
def main():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

    # Keys to remove
    keys = ["name", "salary"]
    for key in keys:
        if key in sample_dict:
            sample_dict.pop(key)
    print(sample_dict)
    #sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
if __name__=="__main__":
    main()