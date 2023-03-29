# define the S-box as a dictionary
sbox = {
    0: [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    1: [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    2: [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    3: [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
}
​
# take 6-bit input from user
num = input("Enter a 6-bit number: ")
​
# convert binary string to integer
num = int(num, 2)
​
# extract row and column numbers
row = int(str(num >> 5) + str(num & 1), 2)
col = (num >> 1) & 0b1111
​
# look up value in S-box and print in decimal
output = sbox[row][col]
print("Output in decimal: ", output)
