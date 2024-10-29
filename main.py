import time
import os
import threading
from lcg import Linear_Congruencial_Generator
from blum_blum_shub import Blum_Blum_Shub
from miller_rabin import Miller_Rabin

def print_random_lcg(thraed_id : int):
    """ A thread function printing five different random numbers using LCG.

    Args:
        thraed_id (int): thread id used in naming
    """    
    r = Linear_Congruencial_Generator(seed=threading.get_ident() ^ int(time.time()))
    
    for i in range(5):
        print("Thread {}: number #{}: {}".format(thraed_id, i, r.rand()))
        
def print_random_bbs(thraed_id : int):
    """ A thread function printing five different random numbers using BBS.

    Args:
        thraed_id (int): thread id used in naming
    """    
    r = Blum_Blum_Shub(seed=threading.get_ident() ^ int(time.time()))
    
    for i in range(5):
        print("Thread {}: number #{}: {}".format(thraed_id, i, r.rand()))
        
if __name__ == "__main__":

    t1 = threading.Thread(target=print_random_bbs, args=(1,))
    t2 = threading.Thread(target=print_random_bbs, args=(2,))
    
    t1.start(); t2.start()
    
    t1.join(); t2.join()
    
    print("--\nok\n--")