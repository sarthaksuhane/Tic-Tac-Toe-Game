ch='y'
while(ch=='Y' or ch=='y'):    
    def sum(a, b ,c):
        return a+b+c

    def instboard():
        zero = 'X' if xState[0] else ('O' if zState[0] else 0)
        one = 'X' if xState[1] else ('O' if zState[1] else 1)
        two = 'X' if xState[2] else ('O' if zState[2] else 2)
        three = 'X' if xState[3] else ('O' if zState[3] else 3)
        four = 'X' if xState[4] else ('O' if zState[4] else 4)
        five = 'X' if xState[5] else ('O' if zState[5] else 5)
        six = 'X' if xState[6] else ('O' if zState[6] else 6)
        seven = 'X' if xState[7] else ('O' if zState[7] else 7)
        eight = 'X' if xState[8] else ('O' if zState[8] else 8)
        nine = 'X' if xState[9] else ('O' if zState[9] else 9)
        print(f"  {one} | {two} | {three} ")
        print(f"----|---|----")
        print(f"  {four} | {five} | {six} ")
        print(f"----|---|----")
        print(f"  {seven} | {eight} | {nine} ")

    def printboard(xState, zState):
        zero = 'X' if xState[0] else ('O' if zState[0] else ' ')
        one = 'X' if xState[1] else ('O' if zState[1] else ' ')
        two = 'X' if xState[2] else ('O' if zState[2] else ' ')
        three = 'X' if xState[3] else ('O' if zState[3] else ' ')
        four = 'X' if xState[4] else ('O' if zState[4] else ' ')
        five = 'X' if xState[5] else ('O' if zState[5] else ' ')
        six = 'X' if xState[6] else ('O' if zState[6] else ' ')
        seven = 'X' if xState[7] else ('O' if zState[7] else ' ')
        eight = 'X' if xState[8] else ('O' if zState[8] else ' ')
        nine = 'X' if xState[9] else ('O' if zState[9] else ' ')
        print(f"  {one} | {two} | {three} ")
        print(f"----|---|----")
        print(f"  {four} | {five} | {six} ")
        print(f"----|---|----")
        print(f"  {seven} | {eight} | {nine} ")

    def checkwin(xState, zState):
        wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 6, 9], [1, 4, 7], [2, 5, 8], [1, 5, 9], [3, 5, 7]]
        for win in wins:
            if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
                print("\nX Wins the Game")
                return 1
            if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
                print("\nO Wins the Game")
                return 0
        return -1

    if __name__ == "__main__":
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        zState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1 #1 is for X and 0 is for O
        print("\nWelcome to Tic Tac Game\n")
        instboard()
        count = 0
        print("\n")
        while(True):
            if count==9:
                print("\nIt's a Tie!\n")
                break
            printboard(xState, zState)
            if turn == 1:
                print("\nX's Chance\n")
                value = int(input("Enter a number: "))
                if((xState[value] == 0) and (zState[value] == 1) or xState[value] == 1):
                    print("\nINVALID INPUT!\n")
                    continue
                xState[value] = 1
                count=count+1
            else:
                print("\nO's Chance\n")
                value = int(input("Enter a number: "))
                if((zState[value] == 0) and (xState[value] == 1) or zState[value] == 1):
                    print("\nINVALID INPUT!\n")
                    continue
                zState[value] = 1
                count=count+1
            cwin = checkwin(xState, zState)
            if(cwin!=-1):
                print("\nMatch Over!")
                break
            turn = 1 - turn
    ch = input("Want to play again?(Y/y) ")

    