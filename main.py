def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()  
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")

    chars_count = sorted_chars_dict(count_chars(file_contents))
    for c in chars_count: 
        if not c["char"].isalpha():
            continue
        print(f"The '{c["char"]}' character was found {c["num"]} times")

    print("--- End report ---")

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_dict = {}
    
    for c in text:
        lowered = c.lower()
        char_dict[lowered] = char_dict.get(lowered,0) + 1

    return char_dict

def sorted_chars_dict(chars_num_dict):
    res = []
    for c in chars_num_dict:
        res.append({"char":c, "num":chars_num_dict[c]})
    res.sort(reverse=True, key=lambda x: x["num"])
    return res


if __name__ == "__main__":
    main()
