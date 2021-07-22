# Importing Translator package from translate
from translate import Translator

# Create instance of Translator class as translator
translator = Translator(to_lang="ja")
# printing the main purpose of the project
print("!!!Translating english into japanese!!!")
try:
    # Writing the content to the file with the name trans.txt and assigning as my_file
    with open("trans.txt", mode="w") as my_file:
        text1 = input("enter the sentence you want to translate: ")
        my_file.write(text1)
    # Opening the file and read the content and assigning the content to the variable text
    with open("trans.txt", mode="r") as my_file:
        text = my_file.read()
        # Translating the content of the file to the japanese with the translate method from Translator class
        translation = translator.translate(text)
        # printing the trnaslated content
        print(translation)
# Checking the FileNotFoundError Exception
except FileNotFoundError:
    print("Yor are not selected an existing file bro!!")
