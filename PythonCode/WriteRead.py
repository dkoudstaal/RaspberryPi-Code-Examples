# Demonstration how to read, write and append data in text files.
# Introduction of the for loop
# Program based on the book Python in Easy Steps.


poem = 'I never saw a man who looked\n'
poem += 'With such a wistfull eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

file = open('poem.txt','w')
file.write(poem)
file.close()

print('Open the text file poem.txt in notepad\
\nand check if the poem was written to the file')
input("\nPress Enter to continue......")

print('\nWe now add the author at the end of the poem/n')

file = open('poem.txt','a')
file.write('(Oscar Wilde)')
file.close()

print('Open the text file poem.txt in notepad\
\nand check if the author was added to the poem in the file')
input("\nPress Enter to continue......")

print('\nRead the file and print the content on the screen\n')

file = open('poem.txt','r')
for line in file:
    print(line, end='')
file.close()

input("\n\nPress Enter to exit......")
