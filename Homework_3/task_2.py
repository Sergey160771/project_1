text = open('text.txt').read()
delete = ".,!?;:-[]{}()="
new_dict = {}
for i in delete:
    text = text.replace(i, "")
text = text.lower().split()

for item in text:
    new_dict.setdefault(item, text.count(item))

for item in range(0,10):
    max_key = max(new_dict, key=new_dict.get)
    print(f'{max_key:>10}  =  {new_dict[max_key]}')
    new_dict.pop(max_key)


