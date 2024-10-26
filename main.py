import time
import os
import threading

class Linear_Congruencial_Generator:
    """Pseudo-random number generator using linear congruencial algorithm.
    Parameters picked as in java.util.Random.
    """    
    
    def __init__(self, a = 25214903917, c = 11, m = 2**48, seed = None):
        if seed == None:
            seed = int(time.time()) ^ os.getpid()
        self.a = a
        self.c = c
        self.m = m
        self.x0 = seed
        
        self.x1 = (self.a * self.x0 + self.c) % self.m
        
    def rand(self):
        self.x1 = (self.a * self.x1 + self.c) % self.m
        return self.x1
    
    def randLen(self, size : int):
        self.x1 = (self.a * self.x1 + self.c) % self.m
        return self.x1 % (10**size)
    
    def randBound(self, low : int, up : int):
        self.x1 = (self.a * self.x1 + self.c) % self.m
        return (self.x1 % up) + low
    
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
