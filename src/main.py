from user import User
import json


def main():
    user: User | None = None
    user_history = load_user_history()
    while user is None:
        user = select_user(user_history)
    print(f"select user {user.display_name}")


def load_user_history() -> list[str]:
    with open("./user_history.json", "r") as f:
        user_history = json.load(f)
    return user_history


def select_user(user_history: list[str]) -> User | None:
    print("select a user from below: ")
    display_user_history(user_history)
    while True:
        try:
            selection = int(input(f"type a number between 1 and {len(user_history)} and press ENTER to select a user\n"))
            if selection < 1 or selection > len(user_history):
                raise ValueError
            break
        except ValueError:
            continue
    return find_user(user_history[selection - 1])


def find_user(email: str) -> User | None:
    # TODO: find user from database by email
    if email == "tom@cat.com":
        return User(display_name="Tom", email=email, password="123")
    if email == "jerry@mouse.com":
        return User(display_name="Jerry", email=email, password="123")
    if email == "spike@dog.com":
        return User(display_name="Spike", email=email, password="123")


def display_user_history(user_history: list[str]):
    for i, uh in enumerate(user_history):
        print(f"{i + 1}. {uh}")


def login() -> User | None:
    return None


def select_list(user: User):
    pass


if __name__ == "__main__":
    main()
