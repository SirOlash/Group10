class User:
    def __init__(self, first_name, last_name, email, password):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password


    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    def verify_password(self, password):
        return self._password == password