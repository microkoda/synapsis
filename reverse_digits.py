def reverse_digits(N: int) -> int:
    """
    Function returns inverted integer (digits in reverse order) when it is in range of values
    for 32-bit integer (- 2**31, 2**31 - 1) otherwise returns 0
    
    Parameters:
        N(int):The integer which is to be reversed.

    Returns:
        N_inv(int):The integer which gets reversed or 0.
        
    Examples:
    
    >>> reverse_digits(123)
    321
    
    >>> reverse_digits(987654321)
    123456789
    
    >>> reverse_digits(8463847411)
    1147483648
    
    >>> reverse_digits(8463847412)
    0
    
    >>> reverse_digits(-8463847412)
    -2147483648
    
    >>> reverse_digits(-8463847413)
    0
    """
    if not isinstance(N, int):
        raise TypeError('N must be integer')
    else:
        N = int(N)
        N_inv = -int(str(abs(N))[::-1]) if N < 0 else int(str(N)[::-1])
        return N_inv if N_inv in range(-2**31, 2**31) else 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()