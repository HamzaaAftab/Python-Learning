
### Q.1: Write a python to display a user entered name followed by Good Afternon
# KEYPOINT: If you specify f before the quotes in string, f'', you can simpley use {} to inject variables into your string,
name = input("Enter your Name: ")
print(f'Good Afternoon {name}')

### Q.2: Write a python program fill the letters in the program

letter = ''' Dear <|NAME|>, You are selected, Your Interview is scheduled at <|DATE|>'''

print(letter.replace('<|NAME|>', 'Hamza').replace('<|DATE|>', '22th Feb, 25'))