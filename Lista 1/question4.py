def is_prime(n):
    for i in range(n):
        if i != 0 and i != 1:
            if n % i == 0:
                return False
    
    return True
