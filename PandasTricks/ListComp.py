# my_fav_numbers = [1, 2, 3, 5, 8, 13]
#
# new_list = [2 * n
#             for n in my_fav_numbers
#             if n % 2 == 1]


# using for loop
def get_vowel_names(names):  # return names that start with a vowel
    vowel_name = []
    for name in names:
        if name[0].upper() in "AEIOU":
            vowel_name.append(name)
    return vowel_name


names_list = ['Alice', 'Ben', 'Charlotte', 'Oliver']


# list comp

def list_comp_names(names):
    return [name for name in names if name[0].upper() in "AEIOU"]


if __name__ == '__main__':
    print(list_comp_names(names_list))
