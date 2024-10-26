import time
import os
import threading
from lcg import Linear_Congruencial_Generator

def print_random(thraed_id : int):
    """ A thread function print three different random numbers.

    Args:
        thraed_id (int): thread id used in naming
    """    
    r = Linear_Congruencial_Generator(seed=threading.get_ident() ^int(time.time()))
    
    for i in range(3):
        print("Thread {}: number #{}: {}".format(thraed_id, i, r.rand()))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_random, args=(1,))
    t2 = threading.Thread(target=print_random, args=(2,))
    
    t1.start(); t2.start()
    
    t1.join(); t2.join()
    
    print("--\nok\n--")