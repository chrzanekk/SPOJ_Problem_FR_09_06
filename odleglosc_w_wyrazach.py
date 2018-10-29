import string

words = []
alpha = list(string.ascii_uppercase)
how_many_words = int(input())
for i in range(how_many_words):
    word = str(input())
    word = word.upper()
    list_of_indexes = []
    for letter in word:
        if letter in alpha:
            letter_index = alpha.index(letter)
            list_of_indexes.append(letter_index)
    difference = max(list_of_indexes) - min(list_of_indexes)
    print(difference)


    
    

