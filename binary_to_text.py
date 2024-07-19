bin_in = input()

bin_in = bin_in.replace(" ","")

#print('Input:', bin_in)

def split_bin(bin_in, n):
    while bin_in:
        yield str(bin_in[:n])
        bin_in = bin_in[n:]

x = list(split_bin(bin_in, 8))

#print('Split binary:', x)

file1 = open('binary_128.txt', 'r')
bin_128 = file1.read()
bin_128 = str(bin_128)

file2 = open('hex_128.txt')
hex_128 = file2.read()
hex_128 = str(hex_128)

bin_128 = bin_128.split("\n")
hex_128 = hex_128.split("\n")

dictionarybh = {}

dictionarybh  = dict(zip(bin_128, hex_128))

def hex_out(x):
    for split in x:
        yield(dictionarybh[split])

ho = list(hex_out(x))

print("Hexadecimal:", ''.join(ho))

# --- read in file containing first 128 characters in ASCII table ---
file3 = open('char_128.txt')
char_128 = file3.read()
char_128 = str(char_128)
# --- split characters by new line
char_128 = char_128.split("\n")

#print(char_128)

# --- assign char_128 and hex_128 characters to dictionary
dictionaryhc = {}

dictionaryhc  = dict(zip(hex_128, char_128))

# --- convert hexadecimal output to alphanumeric characters
def char_out(ho):
    for h in ho:
        yield(dictionaryhc[h])

char = list(char_out(ho))

print("Alphanumeric:", ''.join(char))
