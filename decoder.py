tree = ' eatoinshrdlcumwfgypbvkjxqz'

input_file = 'test.mtxt'
output_file = 'testm.txt'

def binary(x):
    output = []
    for i in range(8):
        output.append(x&1)
        x >>= 1
    return output[::-1]


def decode_simple(bytes_list):
    result = ''
    encoded_list = []
    for i in bytes_list:
        
        encoded_list.extend(binary(i))

    idx = 0
    
    for i in encoded_list:
        if i == 0:
            idx += 1
        elif i == 1:
            result += tree[idx]
            idx = 0
    
    return result

def main():
    with open(input_file,'rb') as readfile:
        with open(output_file,'w') as writefile:
            writefile.write(decode_simple(readfile.read()))

main()
    