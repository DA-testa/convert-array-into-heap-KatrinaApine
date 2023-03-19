# python3

def heaps(data, n, i, swaps):
    chl = 2*i + 1
    chr = 2*i + 2

    s = i
    if chl < n and data[chl] < data[s]:
        s = chl
    if chr < n and data[chr] < data[s]:
        s = chr
    if s != i:
        swaps.append((i, s))
        data[i], data[s] = data[s], data[i]
        heaps(data, n, s, swaps)

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    n = len(data)
    for i in range (n// 2 -1, -1, -1):
        heaps(data, n, i, swaps)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    while True:

        #print("input from keyboard or file (I or F)")
        try:
            inp = input()
        except EOFError:
            return
        if 'I' in inp:
    # input from keyboard
            n = int(input())
            data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
            assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
            swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
            print(len(swaps))
            for i, j in swaps:
                print(i, j)

        if 'F' in inp:
            files = "tests/" + input()

            if 'a' in files:
                #print("file can not contain letter a")
                return 

            try:
                with open(files) as F:

                    n = int(F.readline())
                    # n = int(input())
                    data = list(map(int, F.readline().split()))
                    assert len(data) == n

                    swaps = build_heap(data)
                
                    print(len(swaps))
                    for i, j in swaps:
                       print(i, j)
                    

            except FileNotFoundError:
                print("file is not found")
                return

if __name__ == "__main__":
    main()
