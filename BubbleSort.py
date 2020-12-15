def BubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            # Ascending list
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    return list

def main():
    list = []
    lenList = int(input('Enter the length of list: '))

    for i in range(lenList):
       n = int(input())
       list.append(n)
    print(list)
    print(BubbleSort(list))


main()