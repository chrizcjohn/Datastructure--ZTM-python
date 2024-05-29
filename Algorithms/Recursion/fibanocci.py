def fibanocci_iterative(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        # a, b = 0, 1
        # for _ in range(2, n+1):
        #     a, b = b, a+b
        # return b

        arr = [0,1]
        for i in range(2,n+1):
            arr.append(arr[i-1]+arr[i-2])
        return arr[n]


def fibanocci_recursive(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibanocci_recursive(n-1) + fibanocci_recursive(n-2)


if __name__ == '__main__':
    print(fibanocci_iterative(30))
    print(fibanocci_recursive(35))