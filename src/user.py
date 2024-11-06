from dataclasses import dataclass


@dataclass
class User:
    display_name: str
    email: str
    password: str
