hobbit=['bilbo','frodo','sam','merry','pippin']
print(hobbit)
hobbit[0]='sackville'
print(hobbit)
hobbit.append('bilbo')
print(hobbit)
hobbit.insert(1,'Gandalf')
print(hobbit)
del hobbit[1]
print(hobbit)
popped_hobbit=hobbit.pop()
print(hobbit)
print(popped_hobbit)
unwanted_hobbit=hobbit.pop(0)
print(hobbit)
print(unwanted_hobbit)
no_baggins_zone=hobbit.remove('frodo')
print(hobbit)