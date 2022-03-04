#1 function with undifined numbers of parameteres and the sum of integer and real numbers
def my_function(*args,**keyargs):
#    print(args)
#    print(keyargs)
    x = 0
    for i in args:
        if type(i) == int or type(i) == float: #verify type of parameteres
            x += i
    return x

print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4,'abc', param_1=2)) #for this used **

#2

def suma(n):
    if n == 0:
        return 0
    return n + suma(n-1)
print(suma(5))

def suma_ev(n_ev):
    s_ev = 0
    if n_ev == 0:
        return 0
    if n_ev % 2 == 0:
        s_ev += n_ev
    
    return s_ev + suma_ev(n_ev-1)
print(suma_ev(5))

def suma_od(n_od):
    s_od = 0
    if n_od == 0:
        return 0
    if n_od % 2 != 0:
        s_od += n_od
    
    return s_od + suma_od(n_od-1)
print(suma_od(7))


#3 input function and return the value if it is an integer number

def function_input():
    function_input=input('Introduceti un numar: ')
    try:
        function_input = int(function_input)
        print(f'Numarul introdus {function_input} este intreg')
    except ValueError as s:
        print("0")

function_input()