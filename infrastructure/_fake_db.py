import uuid


class FakeDB:
    _users = [
        {
            'id': uuid.uuid4(),
            'first_name': 'Taro',
            'last_name': 'Tanaka',
            'age': 20,
        },
        {
            'id': uuid.uuid4(),
            'first_name': 'Hanako',
            'last_name': 'Yamada',
            'age': 18,
        },
        {
            'id': uuid.uuid4(),
            'first_name': 'Jiro',
            'last_name': 'Suzuki',
            'age': 16,
        },
    ]

    @classmethod
    def find_all(cls):
        return cls._users
