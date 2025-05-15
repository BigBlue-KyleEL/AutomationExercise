from dataclasses import dataclass


@dataclass
class UserInfo:
    name: str
    email: str
    password: str
    first_name: str
    last_name: str
    company: str
    address: str
    state: str
    city: str
    zipcode: str
    mobile_number: str