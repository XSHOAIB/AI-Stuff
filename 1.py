jugA = 0 #3
jugB = 0 #5

def main():
    while True:
        print('\nSelect Choice!')
        print('\n1. Fill jug A\n2. Fill jug B\n3. Empty jug A\n4. Empty jug B')
        print('5. Transfer A -> B\n6. Transfer B -> A\n')
        choice = int(input('Enter Choice : '))
        check(choice)

def check(choice):
    global jugB, jugA
    if choice == 1:
        jugA = 3
    if choice == 2:
        jugB = 5
    if choice == 3:
        jugA = 0
    if choice == 4:
        jugB = 0
    if choice == 5:
        if jugB == 5 or jugA == 0:
            print('Jug B is Full / Jug A is Empty')
        else:
            transfer = min(jugA, 5 - jugB)
            jugA -= transfer
            jugB += transfer
    if choice == 6:
        if jugA == 3 or jugB == 0:
            print('Jug A is Full / Jug B is Empty')
        else:
            transfer = min(jugB, 3 - jugA)
            jugB -= transfer
            jugA += transfer
    else: 
        print('\n***Invalid Choice\n')
    RealTimeData()

def RealTimeData():
    print(f'Jug A : {jugA}')
    print(f'Jug B : {jugB}')


main()
