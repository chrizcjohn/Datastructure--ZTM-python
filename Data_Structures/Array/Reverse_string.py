def reverse_string(string):
    if not string:
        return string
    reversed_string=""
    for i in range(len(string),0,-1):
        reversed_string+=string[i-1]
    return reversed_string

def reverse_string_array(string):
    if not string:
        return string
    reversed_string_array= []
    for i in range(len(string),0,-1):
        reversed_string_array.append(string[i-1])
    return "".join(reversed_string_array)




if __name__ == '__main__':
    string = 'Hello World'
    print(reverse_string(string))
    print(reverse_string_array(string))