

def check_docstring(func):
    """
    This function checks whether the passed function has doc string present 
    or not and then it checks whether the doc string has minimum of 50 characters.
    """
    characters = 0
    def inner():
        nonlocal characters
        s = ""
        charaters = len(s.join((func.__doc__).split()))
        if charaters > 50:
            return True , charaters
        else:
            return False , 0
    return inner()

def fib():
    """
    This is a closure function which returns fibonacci numbers.
    This retruns one fibonacci number at a time .
    """
    a = 0
    b = 0
    f = 0
    def inner():
        nonlocal a
        nonlocal b 
        nonlocal f
        if b == 0:
            b = 1
            return a
        else:
            f = a + b
            a = b
            b = f
        return a
    return inner

g_dict = {}
def count_function(func):
    """
    This is a closure function which counts the number of times the 
    particular function is executed .
    This also access the global variable 'g_dict' which is the dictionary
    where the counts are stored wrt the function names. 
    """
    global g_dict
    fun_name = func.__name__
    g_dict[fun_name] = 0
    def inner(*arg , **kwargs):
        g_dict[fun_name] += 1
        func(*arg , **kwargs)
    return inner


def add(a,b):
    """
    This function performs addition
    """
    return a+b
def mul(a,b):
    """
    This function perforns multiplication
    """
    return a*b
def div(a,b):
    """
    This Funtion performs Division
    """
    return a/b 

add_dict = {}
div_dict = {}
mul_dict = {}

def individual_count_function(func):
    """
    This is a closure function which counts the number of times the 
    particular function is executed .
    This also access the global variable which is the dictionary
    where the counts are stored wrt the function names. 
    """
    global add_dict,div_dict, mul_dict 
    func_name = func.__name__
    exec(f"{func_name}_dict['count'] = 0")
    def inner(*arg , **kwargs):
        exec(f"{func_name}_dict['count'] += 1")
        print(func_name , exec(f"{func_name}_dict['count']"))
        func(*arg , **kwargs)
    return inner