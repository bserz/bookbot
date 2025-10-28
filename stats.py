def get_book_word_cnt(file_contents):
    counter = 0
    split_words = file_contents.split()

    for i in range(0, len(split_words)):
        counter += 1
    return counter

def get_char_occur_cnt(file_contents):
    char_dict = {}

    for char in file_contents:
            lower_case = char.lower()
            if lower_case in char_dict:
                char_dict[lower_case] += 1
            else:
                char_dict[lower_case]= 1
    return char_dict

def get_sorted_dict(char_dict):
    sorted_list = []
    for key in char_dict:
        if key.isalpha():
            sorted_list.append({"char": key, "num": char_dict[key]})
        else:
            continue
    sorted_list.sort(reverse=True, key=sort_list_chars)
    return sorted_list

def sort_list_chars(list):
    return list["num"]