from dataclasses import dataclass
from datetime import datetime, timedelta

# time threshold: 24h
TIME_THRESHOLD = timedelta(hours=24)
# retry time: 3 times
RETRY_TIME = 3


@dataclass
class User:
    display_name: str
    email: str
    password: str
    last_login: datetime = datetime.min

    def check_credential(self):
        # check if last login time is more than 1 hour ago
        if self.last_login < datetime.now() - TIME_THRESHOLD:
            self.login()
        else:
            print("you are already logged in")

    def login(self):
        for _ in range(RETRY_TIME):
            password = input("type your password and press ENTER\n")
            if password == self.password:
                self.last_login = datetime.now()
                print("login successful")
                return
            else:
                print("login failed")
