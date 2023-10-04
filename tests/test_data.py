from faker import Faker
fake = Faker()


class TestData:
    def __init__(self):
        self.lastname = fake.last_name()
        self.firstname = fake.first_name()
        self.email = fake.ascii_email()
        self.password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
        self.too_short_password = fake.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)
        self.only_two_char_type_password = fake.password(length=8, special_chars=False, digits=True, upper_case=False, lower_case=True)

    
data = TestData()