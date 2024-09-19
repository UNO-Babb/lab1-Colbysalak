#FirstProgram.py
#Name: Colby Salak
#Date:9/1/24
#Assignment: FirstProgram.py

def main():
  print("First Program")
  #Say hello
  print("Hello")
  #Ask for the user's name
uname = input("What is your name")
  #Use the user's name in the program.
print(uname + "is smart")
  #Ask the user for their age.
age = int(input("What is your age"))
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
year = (2024-age)

print(uname + "is born in year " + str(year))

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
