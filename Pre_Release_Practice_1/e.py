#i didnt use json here and it is bloat so basically it is as if i am a microsfot programer
import json

# defining the sack settings using a dictionary
sack_settings = {"contents":{"cement":{"min": 24.9, "max":25.1, "price": 3}, "sand":{"min":49.9, "max":50.1, "price": 2}, "gravel":{"min":49.9, "max":50.1, "price": 2}}}

"""
with open("configs.json", "w") as fi:
    json.dump(sack_settings, fi, indent=4)
    print("done")
"""



#my version of pyinputplus.inputMenu()
def inputMenu(options=[], prompt="Choose one of the following:"):
    if len(options) == 0:
        return
    while True:
        print(prompt)
        for opt in range(len(options)):
            print(f"[{opt}] {options[opt]}")

        response = input("> ")

        try:
            
            response = int(response)
            if response >= 0 and response <= (len(options)-1):
                return options[response]

            else:
                print("Please enter a number from the list")

        except:
            print("Enter a number please")




def inputFloat(prompt="Enter a number: "):
    while True:
        try:
            num = float(input(prompt))

            return num

        except:
            print("Please enter a number")


def inputInt(prompt="Enter a number: "):
    while True:
        try:
            num = int(input(prompt))

            return num

        except:
            print("Please enter a number")

    

def check_sack(weight, content):
    try:
        content = sack_settings["contents"][content]
        if content["min"] <= weight and content["max"] >= weight:
            return True
        else:
            return f"The content was above or below the maximum or minimum weight. (Inputed weight: {weight})"

    except:
        pass

    return f"There is no content with the name {content}"


if __name__ == "__main__":
    while True:
        todo = inputMenu(prompt="What would you like to do?", options=["Check and add a sack", "quit"])

        if todo == "quit":
            print("Data has been saved and the program has quit")
            break

        else:
            weight = inputFloat(prompt="Enter the weight of the sack: ")
            content = input("Enter the content of the sack: ")
            check = check_sack(weight, content)
            if check:
                print(f"The content ({content}) and weight ({weight}) of the sack is valid!")
            else:
                print(check)
