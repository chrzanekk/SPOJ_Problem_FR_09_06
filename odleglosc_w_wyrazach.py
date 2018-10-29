import string
ile_wyrazow = int(input("Podaj ilosc wyrazow: "))
wyrazy = []
alpha = list(string.ascii_uppercase)
print(alpha)
print(len(alpha))
list_of_word_indexes = []
for i in range(ile_wyrazow):
    temp_wyraz = input("Podaj wyraz: ")
    wyrazy.append(temp_wyraz.upper())


for word in wyrazy:
    list_of_indexes = []
    for letter in word:
        if letter in alpha:
            list_of_indexes.append(alpha.index(letter))
    list_of_word_indexes.append(list_of_indexes)


for list in list_of_word_indexes:
    min_value = min(list)
    max_value = max(list)
    difference = max_value - min_value
    print(difference)


#min_value = min(list_of_indexes)
#max_value = max(list_of_indexes)
#difference = max_value - min_value
#print(min_value)
#print(max_value)
#print(difference)



            
    



