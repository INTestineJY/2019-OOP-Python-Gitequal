try:
    f = open('HelloPython.txt', 'r')
except FileNotFoundError:
    print('No file')

print('Next Code...')