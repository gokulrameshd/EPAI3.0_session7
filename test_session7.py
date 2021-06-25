import pytest
from session7 import *

def test_docstring_1():
    assert check_docstring(check_docstring)[0] == True  ,"This function's doc string does not have 50 characters !!"

def test_docstring_2():
    assert check_docstring(fib)[0] == True  ,"This function's doc string does not have 50 characters !!"

def test_docstring_3():
    assert check_docstring(count_function)[0] == True  ,"This function's doc string does not have 50 characters !!"

def test_docstring_4():
    assert check_docstring(add)[0] == False  ,"This function's doc string have more than 50 characters !!"

def test_fib_1():
    fibo = fib()
    f1 = fibo()
    assert f1 == 0 , "Returned output is not the expected fibonacci number!!"

def test_fib_2():
    f_list = []
    fibo = fib()
    for i in range(5):
        f1 = fibo()
        f_list.append(f1)

    assert f_list == [0,1,1,2,3] , "Not fibonacci series"

def test_count_function_1():
    count_add = count_function(add)
    x = count_add(3,6)
    assert g_dict["add"] == 1 , "The count is not correct"

def test_count_function_2():
    count_mul = count_function(mul)
    x = count_mul(3,6)
    assert g_dict["mul"] == 1 , "The count is not correct"

def test_count_function_3():
    count_div = count_function(div)
    
    x = count_div(3,6)
    assert g_dict["div"] == 1 , "The count is not correct"

def test_count_function_4():
    count_add = count_function(add)
    for i in range(6):
        x = count_add(3,6)
    assert g_dict["add"] == 6 , "The count is not correct"

def test_count_function_5():
    count_mul = count_function(mul)
    for i in range(10):
        x = count_mul(3,6)
    assert g_dict["mul"] == 10 , "The count is not correct"

def test_count_function_6():
    count_div = count_function(div)
    for i in range(5):
        x = count_div(3,6)
    assert g_dict["div"] == 5 , "The count is not correct"

def test_individual_count_function_1():
    count_add = individual_count_function(add)
    x = count_add(3,6)
    assert add_dict["count"] == 1 , "The count is not correct"

def test_individual_count_function_2():
    count_mul = individual_count_function(mul)
    x = count_mul(3,6)
    assert mul_dict["count"] == 1 , "The count is not correct"

def test_individual_count_function_3():
    count_div = individual_count_function(div)
    x = count_div(3,6)
    assert div_dict["count"] == 1 , "The count is not correct"

def test_individual_count_function_4():
    count_add = individual_count_function(add)
    for i in range(5):
        x = count_add(3,6)
    assert add_dict["count"] == 5 , "The count is not correct"

def test_individual_count_function_5():
    count_mul = individual_count_function(mul)
    for i in range(10):
        x = count_mul(3,6)
    assert mul_dict["count"] == 10 , "The count is not correct"

def test_individual_count_function_6():
    count_div = individual_count_function(div)
    for i in range(50):
        x = count_div(3,6)
    assert div_dict["count"] == 50 , "The count is not correct"
