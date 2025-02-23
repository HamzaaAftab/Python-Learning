#List is like an array, 
#Unlike strings, Lists are mutable, meaning we can change lists...
friends = ['Apple', 'Orange', 5, 3.45, True, 'Hamza', 'Ahmed']
print(friends[1])

#Append basicaly adds something to add.
friends.append('Khalid')

#Insert adds something at a specific index.
friends.insert(2, 'Ali')
print(friends)

#Remove removes the first occurrence of a specific value.
friends.remove('Ali')
print(friends)

#Pop removes the last element from the list.
friends.pop()
print(friends)

#pop also gives the flexiblity to remove the element at certain index
friends.pop(4)
print(friends)

#Clear removes all elements from the list.
friends.clear()