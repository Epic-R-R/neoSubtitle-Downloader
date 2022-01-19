import requests
from PyInquirer import prompt
from Validators import EmptyValidator, EmailValidator, ValidatePassword
from styles import style
from loadings import loadingSignUp


def signUp():
    accountInfo = [
        {
            "type": "input",
            "name": "username",
            "message": "Enter Your Username :",
            "validate": EmptyValidator,
        },
        {
            "type": "password",
            "name": "password",
            "message": "Enter Your Password :",
            "validate": ValidatePassword,
        },
        {
            "type": "input",
            "name": "email",
            "message": "Enter Your Email    :",
            "validate": EmailValidator,
        },
        {
            "type": "input",
            "name": "name",
            "message": "Enter Your Name     :",
            "validate": EmptyValidator,
        },
    ]
    ans = prompt(accountInfo, style=style)
    if "#" in ans["password"]:
        ans["password"] = ans["password"].replace("#", "%23")
    req = requests.get(
        "http://api.ssubdownloader.ir/register.php?username={}&password={}&email={}&name={}&".format(
            ans["username"],
            ans["password"],
            ans["email"],
            ans["name"],
        )
    ).json()
    if req["message"] == "Registration was successful":
        loadingSignUp("Registration was successful")
        return "Registration was successful"
    elif req["message"] == "Username early exists":
        loadingSignUp("Username early exists")
        return "Username early exists"
    elif req["message"] == "SQL Error":
        loadingSignUp("SQL Error")
        return "SQL Error"