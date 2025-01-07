def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    get_report(chars_dict , num_words) 

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_report(chars_dict , num_words):
    char_list = []
    for key,value in chars_dict.items():
        if key.isalpha():
            char_dict = {"char" : key , "num" : value}
            char_list.append(char_dict)
    
    char_list.sort(reverse = True , key = sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char_info in char_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")
    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

