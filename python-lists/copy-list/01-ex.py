'''
Copiar uma lista
Você não pode copiar uma lista simplesmente digitando list2 = list1, porque: list2será apenas uma referência a list1, e as alterações feitas em list1 serão feitas automaticamente também em list2.

Use o copy()
Você pode usar o List integrado copy() para copiar uma lista.
'''

# Faça uma cópia de uma lista com o copy():

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
