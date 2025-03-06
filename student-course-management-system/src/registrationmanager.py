import os

class RegistrationManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def read_file(self, path):
        if not os.path.exists(path):
            return []
        with open(path, 'r') as f:
            return f.read().splitlines()

    def write_file(self, path, data):
        with open(path, 'a' if os.path.exists(path) else 'w') as f:
            f.write('\n'.join(data) + '\n')


