# def cls(lines=100):

# import os

# 	if os.name == "posix":
# 		os.system("clear")


# 	elif os.name in ("nt", "dos", "ce"):
# 		os.system("CLS")

# 	else:
# 		print('\n' * lines)

def yesOrNo(prompt=" (Y/N) "):
    while 1:
        answer = raw_input(prompt)
        answer = answer.strip()
        answer = answer.lower()

        yes = ["yes", "y", "ye"]
        no = ["no", "n", "nope"]

        if answer in yes:
            return True
        elif answer in no:
            return False
        else:
            continue
    return False


def nameInput(prompt):
    name = raw_input(prompt)
    return name.strip()


def getName():
    tempName = ""

    while 1:
        tempName = nameInput("What is your name? ")
        if len(tempName) < 1:
            continue
        yes = yesOrNo(tempName + ", is that your name? ")

        if yes:
            return tempName
        else:
            continue
