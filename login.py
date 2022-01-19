from Validators import EmptyValidator
from PyInquirer import prompt
import requests
from loadings import loadingSignIn
from config import update
from styles import style


def signIn():
    accountInfo = [
        {
            "type": "input",
            "name": "username",
            "message": "Enter Username:",
            "validate": EmptyValidator,
        },
        {
            "type": "password",
            "name": "password",
            "message": "Enter Password:",
            "validate": EmptyValidator,
        },
    ]
    ans = prompt(accountInfo, style=style)
    if "#" in ans["password"]:
        ans["password"] = ans["password"].replace("#", "%23")
    req = requests.get(
        "http://api.ssubdownloader.ir/login.php?username={}&password={}".format(
            ans["username"], ans["password"]
        )
    ).json()
    if req["message"] == "Username or password is wrong":
        loadingSignIn("Username or password is wrong")
        return "Username or password is wrong"
    else:
        update(newkey="True", obj="account", key="USERINFO")
        update(newkey=req["info"][0]["username"], obj="username", key="USERINFO")
        update(newkey=req["info"][0]["name"], obj="name", key="USERINFO")
        update(newkey=req["info"][0]["email"], obj="email", key="USERINFO")
        loadingSignIn("succeed")
