import msvcrt,sys

print ("enter diary")

inputlol = input("Enter your diray mateirl")
while True:
    lol = input('')
    if msvcrt.kbhit == 'Enter' and lol[-5:] != 'quit':
        pass
    elif msvcrt.kbhit == 'Enter' and lol[-5:] == 'quit':
        sys.exit()
    else:
        pass
