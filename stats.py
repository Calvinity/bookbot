def count_words(text):
    words = text.split()
    return len(words)

def character_numbers(text):
    low_text = text.lower()
    character_dictionary = {}
    for character in low_text:
        if character not in character_dictionary:
            character_dictionary[character] = 0
        character_dictionary[character] += 1
        
    return character_dictionary

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    list_dictionary = []
    for key in dictionary:
        list_dictionary.append({"char":key, "num": dictionary[key]})
    list_dictionary.sort(reverse=True, key=sort_on)
    
    return list_dictionary