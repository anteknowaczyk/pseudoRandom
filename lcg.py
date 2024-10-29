import time
import os
import math

class Linear_Congruencial_Generator:
    """Pseudo-random number generator using linear congruencial algorithm.
    As desribed in https://en.wikipedia.org/wiki/Linear_congruential_generator.
    Parameters picked as in java.util.Random.
    """    
    
    def __init__(self, a = 25214903917, c = 11, m = 2**48, seed = None):
        """ A construct.

        Args:
            a (int, optional): the multiplier. Defaults to 25214903917.
            c (int, optional): the increment. Defaults to 11.
            m (_type_, optional): the modulus. Defaults to 2**48.
            seed (_type_, optional): a seed value. Defaults to None.
        """     
        #If seed is not provided construct one from time since epoch and process id.   
        if seed == None:
            seed = int(time.time()) ^ os.getpid()
        self.a = a
        self.c = c
        self.m = m
        self.x0 = seed
        
        #First generated number.
        self.x1 = (self.a * self.x0 + self.c) % self.m
        
    def rand(self):
        """Generates a pseud-random number without restrictions.

        Returns:
            int: a pseudo-random number.
        """        
        self.x1 = (self.a * self.x1 + self.c) % self.m
        return self.x1
    
    def rand_len(self, size : int):
        """Generates a pseudo-random number of a given length.

        Args:
            size (int): number of digits.

        Raises:
            Exception: if given length is longer then the modulus.

        Returns:
            int: a pseudo-random number of length size.
        """
        #TODO: concatenate multiple random numbers to generate arbitrary length. 
        if (size > math.floor(math.log10(self.m))):
            raise Exception("Max length exceeded")
        
        self.x1 = (self.a * self.x1 + self.c) % self.m
        return self.x1 % (10**size)
    
    def rand_bound(self, low : int, up : int):
        """Generates a pseudo random number within given bounds (including!)

        Args:
            low (int): a lower bound.
            up (int): an upper bound.

        Raises:
            Exception: if upper bound is higher then modulus.

        Returns:
            int: pseudo random number n with low <= n <= up.
        """    
        #TODO: concatenate multiple random numbers to generate arbitrary length.     
        if (up > self.m):
            raise Exception("Max length exceeded")
        
        self.x1 = (self.a * self.x1 + self.c) % self.m
        return (self.x1 % (up - low)) + low
    