places_to_vist=['switzerland','malaysia','indonesia','italy','kazakhstan']

#printing in original order
print(places_to_vist)

#sorting list temporarily
print('\nIn alphabitical order:')
print(sorted(places_to_vist))

#prints unchanged original list
print('\n The original list is still unchanged as shown below:')
print(places_to_vist)

#prints list in reverse order temporarily
print('\nThis is a reversly sorted list: ')
sorted_list=sorted(places_to_vist)
sorted_list.reverse()
print(sorted_list)

#prints original unchanged list
print('\nThe original list is still unchanges:')
print(places_to_vist)  

#prints permanently changed list
places_to_vist.sort()
print('\nList has been sorted permanently')
print(places_to_vist)

#prints list in reverse order permanently
places_to_vist.sort(reverse=True)
print('\n reversed order, cahnged permanently')
print(places_to_vist)

#prints number of places to visit
no_of_places_to_visit=len(places_to_vist)
print('\n So total number of places I wish to visit is '+str(no_of_places_to_visit))
