
import pyjokes as pj
import os

###Q.1 -> Write a Twinkle Twinkle Little Stars Poem in Python

#Use triple single quotes at the beginnering and at the end to print longer statements.

print('''
    
      
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.

''')

###Q.2 -> USE REPL AND Print the table of 5 using it
print(5*1)
print(5*2)
print(5*3)
print(5*4)
print(5*5)
print(5*6)
print(5*7)
print(5*8)
print(5*9)
print(5*10)

###Q.3 -> Install an External Module and use it to perform an operation of your interest
joke = pj.get_jokes()

#Python Module to print jokes
print(joke, " ", "\n")


####Q.4 -> Write a python program to print the contents of a directory using the os module. 
# Get the directory path (current directory)
directory_path = "."

# List all files and folders in the directory
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)

