from collections import Counter

print("Welcome to the Frequency Analysis App")
non_letters =[';','(',')',' ','%','!','@','#','$','%','^','&','*','1','2','3','4','5','6','7','8','9','0','-','/''{','}','[',']','<','>','?',"'",'"']


phrase=input("\nEnter a word or phrase to count the occurence of each letter:")
for non_letters in non_letters:
    phrase = phrase.replace(non_letters,'')

total_occurance = len(phrase)

letter_count = Counter(phrase)
print("\nHere is the frequency analysis from key phrase 1:")
print("\n\tLetter\t\tOccurence\t\tPercentage")
for key,value in sorted(letter_count.items()):
    percentage = 100*value/total_occurance
    percentage = round(percentage,2)
    print(f"\t{key}\t\t\t{value}\t\t\t\t{percentage}")


order_letter_count = letter_count.most_common()
key_phrase_1_ordered_letter = []
for pair in order_letter_count:
    key_phrase_1_ordered_letter.append(pair[0])

print('Letters ordered from highest to the lowest:')
for letter in key_phrase_1_ordered_letter:
    print(letter,end ='')


# For Second Phrase


phrase_2=input("\nEnter a word or phrase to count the occurence of each letter:")
for non_letters in non_letters:
    phrase_2 = phrase_2.replace(non_letters,'')

total_occurance = len(phrase_2)

letter_count = Counter(phrase_2)
print("\nHere is the frequency analysis from key phrase 2:")
print("\n\tLetter\t\tOccurence\t\tPercentage")
for key,value in sorted(letter_count.items()):
    percentage = 100*value/total_occurance
    percentage = round(percentage,2)
    print(f"\t{key}\t\t\t{value}\t\t\t\t{percentage}")


order_letter_count = letter_count.most_common()
key_phrase_1_ordered_letter = []
for pair in order_letter_count:
    key_phrase_1_ordered_letter.append(pair[0])

print('Letters ordered from highest to the lowest:')
for letter in key_phrase_1_ordered_letter:
    print(letter,end ='')








