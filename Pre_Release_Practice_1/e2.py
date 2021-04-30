
from e import *
import json



if __name__ == "__main__":
    while True:
        todo = inputMenu(prompt="What would you like to do?", options=["Check and add a sack", "Check a list of sacks", "quit"])

        if todo == "quit":
            print("Data has been saved and the program has quit")
            break

        elif todo == "Check and add a sack":
            weight = inputFloat(prompt="Enter the weight of the sack: ")
            content = input("Enter the content of the sack: ")
            check = check_sack(weight, content)
            if check == True:
                print(f"The content ({content}) and weight ({weight}) of the sack is valid!")
            else:
                print(check)
            

        else:
            sack_count = inputInt(prompt="Enter the amount of sacks you would like to check: ")
            sack_order = {"cement":0, "sand":0, "gravel":0}
            rejects = 0
            for i in range(sack_count):
                while True: 
                    weight = inputFloat(prompt="Enter the weight of the sack: ")
                    content = input("Enter the content of the sack: ")
                    check = check_sack(weight, content)
                    if check == True    :
                        print(f"The content ({content}) and weight ({weight}) of the sack has been registered!")
                        sack_order[content] = sack_order[content] + 1
                        break
                    else:
                        rejects += 1
                        print(check)

            for el in sack_order:
                print(f"{el} summary:")
                print(f"Amount: {sack_order[el]}")
                print(f"Weight: {sack_settings['contents'][el]['min']*sack_order[el]}")
                print(f"cost: {sack_settings['contents'][el]['price']*sack_order[el]}")
                print("="*10)
                print()
            print(f"Total rejected: {rejects}")
