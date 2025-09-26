'''
Copiar uma lista
Você não pode copiar uma lista simplesmente digitando list2 = list1, porque: list2será apenas uma referência a list1, e as alterações feitas em list1serão feitas automaticamente também em list2.

Use o método copy()
Você pode usar o método List integrado copy()para copiar uma lista.
'''

# Faça uma cópia de uma lista com o copy()método:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
