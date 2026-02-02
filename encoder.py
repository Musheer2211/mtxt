tree = ' eatoinshrdlcumwfgypbvkjxqz'

input_file = '1mb_cleaned.txt'
output_file = '1mb_cleaned.mtxt'

offset = 0

#     offset = offset + tree.index(char)
#     cur_byte += 1
#     cur_byte = cur_byte << tree.index(char)
#     char_tbw = None
#     if cur_byte > 255:
#         offset = offset%8
#         cur_byte
#         print('new byte')
#         while cur_byte>255:
#             char_tbw = chr(cur_byte&255)
#             cur_byte = cur_byte >> 8
#     return (cur_byte,char_tbw)

def add_0(x):
    output = []
    for i in range(x):
        output.append(0)
    output.append(1)
    
    return output

def not_add_0(l):
    s = 0
    for i in l:
        s = s << 1
        s += i
    return s


def encode_simple(string):
    encoded_list = []
    for i in string:
        encoded_list.extend(add_0(tree.index(i)))
    
    encoded_list.extend([1] * ((8-(len(encoded_list)%8))%8))
    
    bytes_tbw = []

    for i in range(0,len(encoded_list),8):
        bytes_tbw.append(not_add_0(encoded_list[i:i+8]))
    
    return bytes_tbw
def encode(char : str,cur_byte : int) -> tuple[int,str|None]:
    byte_tbw = bytearray()
    offset = offset + tree.index(char)
    
    cur_byte += 128
    byte_tbw.append([0]*offset//8)
    offset = offset % 8
    


def main():
    with open(input_file,'r') as readfile:
        with open(output_file,'wb') as writefile:
            # print(encode_simple(readfile.read()))
            writefile.write(bytes(encode_simple(readfile.read())))

main()