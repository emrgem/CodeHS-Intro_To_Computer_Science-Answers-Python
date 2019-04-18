# Write code here...
def max_int_in_list(str):
    k = 0
    for i in str:
        if k<int(i):
            k = int(i)
    return k
        




my_list = [5, 2, -5, 10, 23,-21]
biggest_int = max_int_in_list(my_list)
print biggest_int