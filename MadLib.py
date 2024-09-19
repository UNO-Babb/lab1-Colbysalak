#MadLib.py
#Name: Colby Salak
#Date:9/1/24
#Assignment: MadLib.py

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("Give me a noun 1: ")
noun2 = input("Give me a noun 2: ")
verb1 = input("Give me a verb 1: ")
verb2 = input("Give me a verb 2": )
adjective = input("Give me an adjective 1: ")
adjective = input("Give me an adjective 2: ")
  #Print the story with the user supplied words.
print(noun1 + "goes to the park with" + noun2 + ". " +noun1 " "+ verb1 + " to the store with" + noun2 ".")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
