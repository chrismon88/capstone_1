#create function for parsing user inptu
def parser(userInput):
    string_list = userInput.split()#splits string into individual elements in list

    new_list = [] # variable creating empty list used to store elements
    for e in string_list:
        new_list.append((e.title())) #capatalizing first letter of elements in list

    first_word = new_list[0].lower()
    new_list[0] = first_word

    j = "".join(new_list)
    return j

def main():
    user_txt = input("Enter the senetence you wish to parse:")
    print(parser(user_txt))
main()