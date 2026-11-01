# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O(input/output) bound tasks like reading files or fetching data from APIS
#                  threading.Thread(target=my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}.")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# walk_dog()
# take_out_trash()
# get_mail()

# The above three tasks will perform in order, one at a time

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo")) # ',' here is necessary even without
#                                                                        the second parameter
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)

# With these thread methods, we can do tasks simultaneously

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join() # This will help the print function to wait until all the chores are finished

print("All chores are completed!")