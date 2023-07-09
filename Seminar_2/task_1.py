# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

a: int = 10
b: str = "New string"
c: bool = False

print(type(a))
print(type(b))
print(type(c))

if type(c) == str:
    print("OK")
else:
    print("NOT A STRING")

print(isinstance(c, bool))
