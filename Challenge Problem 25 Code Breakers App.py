from collections import Counter

print("Welcome to the Code Breaker App")
non_letters =['-',',','.',';','(',')',' ','%','!','@','#','$','%','^','&','*','1','2','3','4','5','6','7','8','9','0','-','/''{','}','[',']','<','>','?',"'",'"']

phrase = """
Importance of Friendship Friendship is important in life because it teaches us a great deal about life. We learn so many lessons from friendship which we won’t find anywhere else. You learn to love someone other than your family. You know how to be yourself in front of friends.Friendship never leaves us in bad times. You learn how to understand people and trust others. Your real friends will always motivate you and cheer for you. They will take you on the right path and save you from any evil.Similarly, friendship also teaches you a lot about loyalty. It helps us to become loyal and get loyalty in return. There is no greater feeling in the world than having a friend who is loyal to you.Moreover, friendship makes us stronger. It tests us and helps us grow. For instance, we see how we fight with our friends yet come back together after setting aside our differences. This is what makes us strong and teaches us patience.Therefore, there is no doubt that best friends help us in our difficulties and bad times of life. They always try to save us in our dangers as well as offer timely advice. True friends are like the best assets of our life because they share our sorrow, sooth our pain and make us feel happy.
"""


phrase = phrase.lower()

#phrase=input("\nEnter a word or phrase to count the occurence of each letter:")
for non_letter in non_letters:
    phrase = phrase.replace(non_letter,'')

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

phrase_2= """
Our parents teach us some of the basic etiquette and ethics of life from a young age so that we can grow up into honest and responsible people. They shower their blessings and fund our education so that we can grow up as educated and well-mannered individuals. At times, they live in scarcity and teach us to face difficult situations in life gallantly Parents work hard so that they can provide us with all the basic resources which are helpful for our overall development. They provide mental, emotional and physical support and help us in taking crucial decisions in our life. They face tough hardships in their lives and protect us from the vices of society.The life without parents is a worst life ever. Parents are support and shade for us. The value of parents in our lives can never be ignored. They play a very great role in our lives.They protect us and give every sacrifice to make us happy and pleased. Parents are our true guardians. The are the real reasons of our success and happiness in this world.
"""

phrase_2 = phrase_2.lower()
#phrase_2=input("\nEnter a word or phrase to count the occurence of each letter:")
for non_letter in non_letters:
    phrase_2 = phrase_2.replace(non_letter,'')

total_occurance = len(phrase_2)

letter_count = Counter(phrase_2)
print("\nHere is the frequency analysis from key phrase 2:")
print("\n\tLetter\t\tOccurence\t\tPercentage")
for key,value in sorted(letter_count.items()):
    percentage = 100*value/total_occurance
    percentage = round(percentage,2)
    print(f"\t{key}\t\t\t{value}\t\t\t\t{percentage}")


order_letter_count = letter_count.most_common()
key_phrase_2_ordered_letter = []
for pair in order_letter_count:
    key_phrase_2_ordered_letter.append(pair[0])

print('Letters ordered from highest to the lowest:')
for letter in key_phrase_2_ordered_letter:
    print(letter,end ='')


#Let's encode or decode the phrase

choice = input("Would you like to encode or decode a message").lower()
phrase_user = input("What is the phrase:").lower()

for non_letter in non_letters:
    phrase_user = phrase_user.replace(non_letter,'')


if choice == 'encode':
    encoded_phrase = []
    for letter in phrase_user:
        index = key_phrase_1_ordered_letter.index(letter)
        letter = key_phrase_2_ordered_letter[index]
        encoded_phrase.append(letter)

    print("\n The encoded message is: ")
    for letter in encoded_phrase:
        print(letter,end='')

elif choice == 'decode':
    decoded_phrase = []
    for letter in phrase_user:
        index = key_phrase_2_ordered_letter.index(letter)
        letter = key_phrase_1_ordered_letter[index]
        decoded_phrase.append(letter)
    print("The decoded message is:")
    for letter in decoded_phrase:
        print(letter, end='')

else:
    print("Please type encode or decode. Try againa")






