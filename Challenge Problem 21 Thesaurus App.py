print("Welcome to The Thesarus App!")
print("\nChoose a word from the thesaurus and I will give you a synonym.")

thesarus = {
    'hot': ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    'cold': ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    'happy': ['content', 'cherry', 'merry', 'jovial', 'jocular'],
    'sad': ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}
print("Here are the words in the thesaurus:")
for key in thesarus.keys():
    print(f"\t-{key}")

choose = str(input('What word would you like a synonym for: '))

for key,value in thesarus.items():
    if choose == key:
        print(f'A synonym for {choose} is {value[0]}')
    else:
        print('I am sorry the word is not currently in thesaurus')

choice = str(input('\nWould you like to see the whole thesarus y/n')).lower()
if choice == 'y':
    for key,value in thesarus.items():
        print(f"{key} synonym are:")
        for v in value:
            print(f"\t-{v}")

else:
    print('I hope you enjoyed the program. Thankyou!')




