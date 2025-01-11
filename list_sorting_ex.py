hobbit=['frodo','bilbo','sam']

#sorting list alphabetically(permanent)
hobbit.sort()
print(hobbit)

#sorting list alphabrtically in reverse order(permanent)
hobbit.sort(reverse=True)
print(hobbit)

#list of members in fellowhip
fellowsip_of_the_ring=['frodo','aragon','gimli','legolas','gandalf','sam']
print('The origin fellowship contains')
print(fellowsip_of_the_ring)

#sorting the list alphabeticaly (temporarily)
sorted_fellowship=sorted(fellowsip_of_the_ring)
print('\nThis is the sorted list')
print(sorted_fellowship)

#unchaged original fellowsip
print('\nHowever original fellowshipis still unchanged')
print(fellowsip_of_the_ring)

#reversing the order of current list not alaphabitically but permanently
fellowsip_of_the_ring.reverse()
print('\nReverse of fellowship list, but not alphabetically')
print(fellowsip_of_the_ring)

#length of the list
print('\nSo the length of the list is: ')
print(len(fellowsip_of_the_ring))