from user import User

def main():
    user_history = load_user_history()
    select_user(user_history)
    print("select a list from below:")

def load_user_history() -> list[str]:
    print("select a user from below: ")
    return []

def select_user(user_history: list[str]) -> User | None:
    pass

def login() -> User | None:
    return None

def select_list(user: User):
    pass

if __name__ == "__main__":
    main()
