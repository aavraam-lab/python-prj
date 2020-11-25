#Python script simulating a tictactoe game


table = [[0,0,0],[0,0,0],[0,0,0]]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def main():
    _firstPlaying = 0
    _currPlaying = 0

    while(_firstPlaying!=1 and _firstPlaying!=2):
        try:
            _firstPlaying = int(input('Which player is playing first [1/2]: '))
            _currPlaying = _firstPlaying
        except:
            continue
        
    while(True):
        print('\n--> Player',_currPlaying,'its your turn!')
        
        
        while(True):
            inList = []
            inList = input('Enter row and column: ').split()

            try:
                inList[0] = int(inList[0])
                inList[1] = int(inList[1])
            except:
                print(bcolors.WARNING+'--> Hmm that wasnt an expected set of numbers...'+bcolors.ENDC)
                continue
    
            if(checkPos(inList[0],inList[1])):
                print(bcolors.OKGREEN+ '--> Success | Position available...'+bcolors.ENDC)
                addMove(inList[0],inList[1],_currPlaying)
                printTable()
                break
            else:
                print(bcolors.FAIL+'--> Not available pos or out of bounds!, please give it another shot...'+bcolors.ENDC)

        winner = checkWinner()

        if(winner==1 or winner==2):
            print("WE HAVE A WINNER: PLAYER",winner)
            break

        if(_currPlaying == 1):
            _currPlaying = 2
            continue;
        else:
            _currPlaying = 1
            continue;



def checkPos(x,y):
    x = x-1
    y = y-1

    if(x>2 or x<0 or y>2 or y<0):
        return False
    else:
        if(table[x][y] == 0):
            return True
        else:
            return False

def addMove(x,y,p):
    table[x-1][y-1] = p

def printTable():
    for i in [0,1,2]:
        print(table[i])

def checkWinner():

   #Check elements of each row
   for i in [0,1,2]:
       if((table[i].count(1))==3):
           return 1
       if((table[i].count(2))==3):
           return 2 
#Unfinished....       

main()



