import sys
import time

time.sleep(2)
print('''
Welcome to the ocean !
''')
time.sleep(2)
print('''
You were split from your group
due to sudden rough waves
and now find yourself stranded... 
''')
time.sleep(3)
print('''
You are on a boat,
All you have is a torn map,
some food and water that will 
last 2 days....
''')
time.sleep(3)
print('''
who knows, the map may or may not help you,
but remember that the ocean is unpredictable !!!
''')
time.sleep(2)
print('''
You can type the name of the object in the inventory,
and type in the direction you want to head in..
May you live !!
''')
print("what do you do next ? ")
#map = input()
while True:
    map = input()
    if('map' in map):
        print('''the map appears torn in places, so you may not get a 
        full idea of which direction to head in....oops..''')
        direction = input('''enter the direction , you wish to go to: ''')
        break
    elif(map == ('north') or map == ('south') or map ==('east') or map==('west')):
        print("Shouldn't you open the map first ?")
    else:
        print('''i dont understand what you are trying to do ...''')
        continue

while True:
    if direction == 'north':
        print('''You find yourself circled by sharks, before you can turn
                 the boat topples and they devour you ....this means you are dead !''')
        break
    elif direction == 'south':
        print('''You see an unkempt ship at some distance
        the markings indicate that it belongs to the pirates''')
        time.sleep(2)
        choice = input('''it is up to you to go TO them or AWAY from them
        That said, move ahead ?(yes/no) :  ''')

        if choice == 'yes':
            print('''You are captured by the pirates, you are now their slave
            Game Over for you my friend''')
            break
        else:
            direction = input("Turning away was a good choice, what direction to now ? : ")
    elif direction == 'west':
        print('''Sailing west...you see a small island at a distance,
        coconut trees, is it really there or just a mirage ?....''')
        time.sleep(1)
        choice = input('take a chance ?(yes/no): ')
        if choice == 'yes':
            print('''IT IS REAL , THE ISLAND IS FREAKING REAL
            whats more you see the rest of your friends there too
            You live after all.....dont forget to thank me when you 
            get famous from this .....off you go ..''')
            break
        else:
            final_choice = input('''So......going east ?(yes/no) ...''')
            if final_choice == 'yes':
                direction = 'east'
            else:
                print('''why dont you sit and wait for someone to come rescue you
                in probably a million years......i'm out''')
                sys.exit()
    elif direction == 'east':
        print('''You end up rowing for what feels like hours''')
        time.sleep(2)
        print("about to give up......")
        time.sleep(3)
        print('''Hey wait....do you see that.....''')
        time.sleep(3.5)
        print("That is the damn NAVY.....how far in are we !")
        time.sleep(5)
        print('''Well, you have saved yourself indeed !....
        Don't forget to mention me when you are all famous bud !''')
        sys.exit()

    else:
        direction = input("You need to mention a simple direction bud.. i haven't evolved as much as you yet : ")
        continue
