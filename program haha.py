'''
from Bejarlibrary
'''

def translate(text1,dict1):
    list_text = text1.split()
    new_text = []
    for word in list_text:
        translation = dict1.get(word)
        new_text.append(translation if translation else word)
    return ' '.join(new_text)

text =  "The fox jumped high in the air to catch the grapes in his mouth , but he missed. He tried again and missed again." \
        "the fox decided to go home all the while muttering, ‘I’m sure the grapes were sour anyway’."
list_text = text.split()



#build a dictionary
mydictionary = {'high': input ("Anything"),'mouth': input ("Anything"),
                'home': input ("Whereever"),'sour': input ("Anything")}

print(translate(text, mydictionary))
