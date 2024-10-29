import math
import time
import os

from lcg import Linear_Congruencial_Generator
from miller_rabin import Miller_Rabin

class Blum_Blum_Shub:
    """A Blum Blum Shub pseudo-random numbers generator.
    As desribed in https://en.wikipedia.org/wiki/Blum_Blum_Shub.
    """    
    def __init__(self, p_size = 8, seed = None):
        """A constructor

        Args:
            p_size (int, optional): number of digits in a prime integer p. Defaults to 8.
            seed (int, optional): a seed for the generator. Defaults to None.
        """        
        rand = Linear_Congruencial_Generator()
        mr = Miller_Rabin()
        
        #If seed is not provided construct one from time since epoch and process id.   
        if seed == None:
            seed = int(time.time()) ^ os.getpid()
            
        #Generate two primes congruent to 3 mod 4.
        #TODO: implement Secure Primes!
        self.p = self.__gen_prime(p_size)
        while(self.p % 4 != 3):
            self.p = self.__gen_prime(p_size)
            
        self.q = self.__gen_prime(p_size)
        while(self.p % 4 != 3):
            self.q = self.__gen_prime(p_size)
        
        #Multiply to get M.
        self.M = self.p * self.q
        
        #Find random initial value co-prime to M based on seed.
        self.x = rand.rand() ^ seed
        while(self.x in [0, 1] or not self.__coprime(self.x, self.M)):
            self.x = rand.rand() ^ seed
            
    def rand(self):
        """Generates a pseudo-random number without restrictions.

        Returns:
            int: A pseudo random number.
        """        
        self.x = pow(self.x, 2, self.M)
        return self.x
    
    def __gen_prime(self, len : int, k = 4):
        """Generates a prime of a given length.

        Args:
            len (int): length of a prime.
            k (int, optional): a level of security in a Miller-Rabin test. Defaults to 4.

        Returns:
            int: A prime of length len.
        """        
        rand = Linear_Congruencial_Generator()
        mr = Miller_Rabin()
        
        p = rand.rand_bound(3, 10**len)
        
        while(not mr.is_prime(p, k)):
            p = rand.rand_bound(3, 10**len)
        
        return p

    def __coprime(self, x : int, y : int):
        """Checks, if two integers are co-prime.

        Args:
            x (int): first integer.
            y (int): second integer.

        Returns:
            boolean: x is coprime to y.
        """        
        return math.gcd(x, y) == 1