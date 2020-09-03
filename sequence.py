n = int(input("Enter the length of the sequence: ")) # Do not change this line

num_1 = 1
num_2 = 2
num_3 = 3

print(num_1)
print(num_2)
print(num_3)
for counter in range(1,n-2):
    sum_int = 0
    sum_int += num_1+num_2+num_3
    num_1=num_2
    num_2=num_3
    num_3=sum_int
    print(num_3)
