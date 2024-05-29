def reverse_iterative(word):
    arr=[]
    for i in range(len(word),0,-1):
        arr.append(word[i-1])
    return "".join(arr)



def reverse_recursive(word):
    if word == "":
        return ""
    return reverse_recursive(word[1:]) + word[0]


if __name__ == '__main__':
    print(reverse_iterative('yoyo master'))
    print(reverse_recursive('yoyo master'))