person = {'name': 'John', 'age': 30, 'gender': 'male'}

name = person.get('name')
print(name)

email = person.get('email')
print(email)

email = person.get('email', 'unknown')
print(email)
