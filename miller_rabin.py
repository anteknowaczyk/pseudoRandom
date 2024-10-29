from lcg import Linear_Congruencial_Generator

class miller_rabin:
    def __init__(self):
        pass
    
    def isPrime(n : int, k : int):
        #LCG generator for random integers.
        rand = Linear_Congruencial_Generator()
        
        if (n < 3 or n % 2 == 0):
            raise Exception("x too small or even")
        
        #Factoring powers of 2 out of n - 1
        s, d = 0, 0
        p = n - 1
        while (p % 2 == 0):
            s += 1
            p //= 2
        d = p
        
        for i in range(k):
            a = rand.randBound(2, n - 2)
            x = (a**d) % n
            
            for j in range(s):
                y = x**2 % n
                #Non-trivial square root of 1 modulo n - composite
                if (y == 1 and x != 1 and x != n - 1):
                    return False
                x = y
            
            if y != 1:
                return False

        return True