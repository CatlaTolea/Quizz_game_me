# create a quizzgame with admin and players. A user has to login, if player then we can play,
# if admin we can add questions.
import json


def add_user(player_id: str, all_players: dict, path: str = "users.json") -> dict:
    full_name = input("Introdu numele tau (optional): ")
    full_name = player_id if full_name == "" or not full_name.isalnum() else full_name
    passwd = ""
    confirm_passwd = " "

    while len(passwd) < 3:
        while passwd != confirm_passwd:
            passwd = input("Introdu parola ta: ")
            confim_passwd = input("confirma parola: ")
        if len(passwd) <3:
            passwd = ""
            confirm_passwd = " "
            print("parola e prea mica")

    new_user = {player_id: {"full_name": full_name, "high_score": 0, "password": passwd}}
    all_players.update(new_user)

    with open(path, "w") as f:
        f.write(json.dumps(all_players, indent=4))

    return new_user


def login(path: str = "users.json"):
    is_new_user = False
    new_user = {}
    user = input("logheaza-te: ")
    with open(path, "r") as f:
        users = json.loads(f.read())

    if user not in users:
        user_pick = input("Doresti sa te inscrii ca new user? Y/N ")
        if user_pick.lower == "y":
            new_user = add_user(player_id=user, all_players=users)
            is_new_user = True
        else:
            while user not in users:
                user = input("logheaza-te, utilizatorul nu exista. ")

    if not is_new_user:
        passwd = input("Introdu parola: ")
        counter = 0
        while passwd != users[user]["password"]:
            passwd = input("Parola gresita. Reintrodu parola: ")
            counter += 1
            if counter == 3:
                raise Exception("Parola a foit introdusa de prea multe ori")

    else:
        return new_user

    return {user: users[user]}


if __name__ == '__main__':
    welcome_msg = "Welcome to quizz game"
    print(f"{len(welcome_msg) * '='}{welcome_msg}{len(welcome_msg) * '='}")

    login()
