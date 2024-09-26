

def get_book_text(book_path):
    with open(book_path) as file:
        
        return file.read()


def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    words = text.split()
    lower_text = text.lower()
    text_report(count_words = len(words),letters = count_each_letter(lower_text))
    
    

def count_each_letter(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count


def text_report(count_words,letters):  
    print(f"{count_words} words was found in the text")
    
    for key,value in letters.items() :
        print(f"we found in the text the letter {key} {value} times")
    print("end of the report")
        
main()