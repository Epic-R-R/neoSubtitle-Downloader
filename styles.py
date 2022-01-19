from PyInquirer import Token, style_from_dict

# create style for terminal
style = style_from_dict(
    {
        Token.QuestionMark: "#fac731 bold",
        Token.Answer: "#4688f1 bold",
        Token.Instruction: "",  # default
        Token.Separator: "#cc5454",
        Token.Selected: "#0abf5b",  # default
        Token.Pointer: "#673ab7 bold",
        Token.Question: "",
    }
)


# create class for terminal color
class bcolors:
    GREEN = "\033[32m"
    HEADER = "\033[95m"
    MAGENTA = "\033[35m"
    OKBLUE = "\033[94m"
    BLUE = "\033[34m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
