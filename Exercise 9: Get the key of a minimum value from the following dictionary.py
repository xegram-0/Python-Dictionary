# Exercise 9: Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# Expected output:

# Math

def main():
    sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
    }
    # This results in lowest in terms of alphabet
    #print(min(sample_dict))
    print(min(sample_dict, key=sample_dict.get))
if __name__=="__main__":
    main()