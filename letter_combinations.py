from itertools import product
from string import digits
def letter_combinations(numbers: str) -> list:
    """
    Function calculates all the possible letter combinations for number typed on numeric keypad where 
    each number represents one of possible characters:
    1: [''], 2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z'], 0: ['+']
    
    Parameters:
        numbers(str): set of digits to calculate letter combinations

    Returns:
        result(list):list of possible character combinations or empty list (if numbers is empty string).
        
    Examples:
    
    >>> letter_combinations('46')
    ['GM', 'GN', 'GO', 'HM', 'HN', 'HO', 'IM', 'IN', 'IO']
    
    >>> letter_combinations('2')
    ['A', 'B', 'C']
    
    >>> letter_combinations('')
    []
    
    >>> letter_combinations('730')
    ['PD+', 'PE+', 'PF+', 'QD+', 'QE+', 'QF+', 'RD+', 'RE+', 'RF+', 'SD+', 'SE+', 'SF+']

    >>> letter_combinations('319')
    ['DW', 'DX', 'DY', 'DZ', 'EW', 'EX', 'EY', 'EZ', 'FW', 'FX', 'FY', 'FZ']

    >>> letter_combinations(1)
    Traceback (most recent call last):
        ...
    TypeError: input value must be string
    
    >>> letter_combinations('4A')
    Traceback (most recent call last):
        ...
    ValueError: input value must be digits (0-9)
    """
    
    if isinstance(numbers, str):
        if all(number in digits for number in numbers):
            def tuple_to_str(tpl: tuple) -> str:
                result = ''
                for _ in tpl:
                    result += str(_)
                return result

            dial = {1: [''], 2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
            5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
            8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z'], 0: ['+']}

            chr_lst = []
            for number in numbers:
                chr_lst.append(dial[int(number)])
            result = [tuple_to_str(cp) for cp in product(*chr_lst)]
            return result if len(numbers) > 0 else []
        else:
            raise ValueError('input value must be digits (0-9)')
    else:
        raise TypeError('input value must be string')
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()