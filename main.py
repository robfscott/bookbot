book = "books/frankenstein.txt"

def sort_on_count(dict):
    return dict['count']

def create_dict_list(dict):
    list = []
    for x in dict:
        if x.isalpha():
            entry = {}
            entry['letter'] = x
            entry['count'] = dict[x]
            list.append(entry)
    return list

def order_dict_list(dict_list):
    dict_list.sort(reverse=True, key=sort_on_count)
    return dict_list

def create_report(num_words, num_letters):
    dict_list = create_dict_list(num_letters)
    ordered_dict_list = order_dict_list(dict_list)

    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document")
    print()
    for x in ordered_dict_list:
        print(f"The '{x['letter']}' character was found {x['count']} times")
    print(f"--- End report ---")

def count_letters(file_contents):
    letter_count = {}
    lc_str = file_contents.lower()
    for i in range(len(lc_str)):
        if lc_str[i] in letter_count:
            letter_count[lc_str[i]] += 1
        else:
            letter_count[lc_str[i]] = 1

    return letter_count

def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def main():
    with open(book) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        num_letters = count_letters(file_contents)

        create_report(num_words, num_letters)

main()
