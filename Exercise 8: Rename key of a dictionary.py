# Exercise 8: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.

# Given:

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# Expected output:

# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
def main():
    sample_dict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
    }
    sample_dict.pop("city")
    sample_dict.update(location="New york")
    #sample_dict['location'] = sample_dict.pop('city')
    print(sample_dict)
if __name__=="__main__":
    main()