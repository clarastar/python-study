from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname': 'Robert'},
    {'fname': 'Clara', 'lname': 'Wang'},
    {'fname': 'Alice', 'lname': 'Biu'},
    {'fname': 'Alice', 'lname': 'Liu'},
    {'fname': 'Alice', 'lname': 'Miu'},
    {'fname': 'Bob', 'lname': 'Lan'},
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('.........')

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)