def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words_count = count_words(file_contents)
        chars_count = count_characters(file_contents)
        print_report(words_count, chars_count)

def count_words(text):
    return len(text.split())

def count_characters(text):
    lower_text = text.lower()
    chars = {}

    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def print_report(words_count, characters_count):
    chars = parse_characters(characters_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    print()

    for char in chars:
        print(f"The '{char["name"]}' character was found {char["count"]} times")
    print("--- End report ---")

def parse_characters(characters):
    char_list = []

    for char in characters:
        char_list.append({"name": char, "count": characters[char]})
    
    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list


main()
