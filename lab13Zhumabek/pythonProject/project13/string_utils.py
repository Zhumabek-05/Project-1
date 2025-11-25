# project13/string_utils.py

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

def count_letters(text):
    return sum(1 for char in text if char.isalpha())
