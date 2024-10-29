from lcg import Linear_Congruencial_Generator

class Miller_Rabin:
    """ A Miller_Rabin primality testing algorithm.
    As desribed in https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test.
    """    
    def __init__(self):
        pass
    
    def is_prime(self, n : int, k = 4):
        """Tests if a given integer is prime.

        Args:
            n (int): integer to check
            k (int, optional): a level of security in a Miller-Rabin test. Defaults to 4.

        Returns:
            boolean: n is prime.
        """        
        #LCG generator for random integers.
        rand = Linear_Congruencial_Generator()
        
        #Trivial cases.
        if (n == 2):
            return True
        if (n % 2 == 0):
            return False
        
        #Factoring powers of 2 out of n - 1
        r, s = 0, n - 1
        while (s % 2 == 0):
            r += 1
            s //= 2
        
        #Perform k tests.
        for _ in range(k):
            a = rand.rand_bound(2, n - 1)
            x = pow(a, s, n)
            if (x == 1 or x == n - 1):
                continue
            
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if (x == n - 1):
                    break
            else:
                #Non-trivial square root of 1 modulo n - composite
                return False
        return True