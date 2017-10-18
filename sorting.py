from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ":" + str(self.user_id)

users = [
    User('Bucky', 4),
    User('Sally', 12),
    User('Alice', 33),
    User('Bob', 23),
    User('Mia', 13),
]

for user in users:
    print(user)

print('........')

for user in sorted(users, key=attrgetter('user_id')):
    print(user)