my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(f'Lista elemente: {my_list}')

new_list_asc = my_list.copy() #copy initial list in new_list_asc
new_list_asc.sort() #sort new_list_asc without modify the initial list
print(f'Lista ordonata ascendent: {new_list_asc}')

new_list_des=my_list.copy()  #copy initial list in new_list_des
new_list_des.sort(reverse=True) #sort new_list_des without modify the initial list
print(f'Lista ordonata descendent: {new_list_des}')

my_list_even = new_list_asc[1::2] #select even number index from new_list_asc list 
print(f'Lista numere pare din lista ordonat: {my_list_even}')

my_list_odd = new_list_asc[::2] #select odd number index from new_list_asc list
print(f'Lista numere impare din lista ordonat: {my_list_odd}')

my_list_mul = new_list_asc[2::3] #select multiply by 3 numbers from new_list_asc list
print(f'Lista numere multiplu de 3 din lista ordonata: {my_list_mul}')

#vs1- de test
multiply_list=[x for x in my_list if x%3==0]
print (f'Lista numere multiplu de 3 din lista initiala: {multiply_list}')