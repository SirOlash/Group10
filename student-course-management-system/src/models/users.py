from typing import Optional
import bcrypt


class PasswordHasher:
    """Handles password hashing and verification operations"""
    ENCODING = 'utf-8'

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using bcrypt"""
        return bcrypt.hashpw(
            password.encode(PasswordHasher.ENCODING),
            bcrypt.gensalt()
        ).decode(PasswordHasher.ENCODING)

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """Verify a password against its hash"""
        return bcrypt.checkpw(
            password.encode(PasswordHasher.ENCODING),
            hashed.encode(PasswordHasher.ENCODING)
        )


class User:
    """Base user class with authentication capabilities"""

    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        """Initialize a new user"""
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.password: str = PasswordHasher.hash_password(password)

    def verify_password(self, password: str) -> bool:
        """Verify if provided password matches stored hash"""
        return PasswordHasher.verify_password(password, self.password)

    def __str__(self) -> str:
        """String representation of user"""
        return f"{self.first_name},{self.last_name},{self.email},{self.password}"


class Student(User):
    """Student user type"""
    pass


class Facilitator(User):
    """Facilitator user type"""
    pass
