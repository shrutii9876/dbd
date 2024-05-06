import re

def repeated_nonrepeated_paragraph(paragraph):
    # Remove punctuation using regular expression
    paragraph = re.sub(r'[^\w\s]', '', paragraph)
    # Convert to lowercase
    paragraph = paragraph.lower()

    words = paragraph.split()
    word_count = {}

    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    repeated_words = []
    non_repeated_words = []

    # Separate repeated and non-repeated words
    for word, count in word_count.items():
        if count > 1:
            repeated_words.append(word)
        else:
            non_repeated_words.append(word)
    
    return repeated_words, non_repeated_words

paragraph = input("Enter paragraph: ")
repeated, non_repeated = repeated_nonrepeated_paragraph(paragraph)
print("Non-repeated words:", non_repeated)
print("Repeated words:", repeated)
