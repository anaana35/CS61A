""" Optional problems for Lab 6 """


## Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    "*** YOUR CODE HERE ***"
    location = 0
    length = len(snacks)

    def func():
        nonlocal location
        result = snacks[location]
        location = (location + 1) % length
        return result
    return func
