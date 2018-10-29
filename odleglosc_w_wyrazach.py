import string

wyrazy = []
alpha = list(string.ascii_uppercase)
list_of_word_indexes = []
ile_wyrazow = int(input("Podaj ilosc wyrazow: "))
#print(alpha)
#print(len(alpha))
for i in range(ile_wyrazow):
    temp_wyraz = input("Podaj wyraz: ")
    if len(temp_wyraz)>=2 and len(temp_wyraz)<= 1000:
        wyrazy.append(temp_wyraz.upper())
    else:
        continue


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



            
    



