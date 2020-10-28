#Project #2 | Atharva Mainkar |
#
#Write a program which solves the given maze.
#
#
#1)Accept input file from the user
#2)Check if input file is valid or not
#3)If valid then, create the maze
#4)Search for the starting point 'S' and intialize
#5)Search up,down,left,right for blank spaces and according to relative position place character '^','v','<','>'
#6)If a dead end appears, traceback path till last intersection and take the other path
#7)Keep doing till end point 'E' is reached
#



def findStartI(puzzle): #Find the Y co-ordinate of start position
    try:
        rowlen=len(puzzle[1])
        colmlen=len(puzzle)
        #print(rowlen,colmlen)
        for o in range(0,colmlen):
            for p in range(0,rowlen):
                if(puzzle[o][p]=="S"):
                    #print(o,p)
                    i=int(o)
                    return i
                    break
                else:
                    continue
        x=-1
        print("Error: No start position found.")
        return x
    
    except:
        print("Error: No start position found.")
        x=-1
        return x

def findStartJ(puzzle): #Find the X co-ordinate of the start position
    try:
        rowlen=len(puzzle[1])
        colmlen=len(puzzle)
        #print(rowlen,colmlen)
        for o in range(0,colmlen):
            for p in range(0,rowlen):
                if(puzzle[o][p]=="S"):
                    #print(o,p)
                    j=int(p)
                    return j
                    break
                else:
                    continue
    except:
        print("Error: No start position found.")
        x=-1
        return x

def findE(puzzle): #Find if end exists or not
    try:
        rowlen=len(puzzle[1])
        colmlen=len(puzzle)
        #print(rowlen,colmlen)
        for o in range(0,colmlen):
            for p in range(0,rowlen):
                if(puzzle[o][p]=="E"):
                    #print(o,p)
                    j=int(p)
                    return j
                    break
                else:
                    continue
        x=-1
        print("Error: No end position found.")
        return x
        
    except:
        print("Error: No end position found.")



def corrinput(puzzle):#Check whether the input has invalid characters or not
    inval=[0,0,0]
    inval[0]=False
    z=0
    for x in puzzle:
        for y in x:
            if y!=" " and y!="S" and y!="E" and y!="#":
                inval[0]=True
                inval[1]=y
                inval[2]=z
        z+=1
    return inval

def printpuz(puzzle): #Print current iteration of the puzzle
    str1=""
    str3=""
    for i in puzzle:
        for j in i:
            str3=str3+str(j)
        str3=str3+"\n"
    print(str3)
    



def move1(i,j,puzzle): #Move the position of the pointer
    if  puzzle[i+1][j]==" ":
        i=i+1
    elif puzzle[i][j-1]==" ":
        j=j-1
    elif puzzle[i][j+1]==" ":
        j=j+1
    elif puzzle[i-1][j]==" ":
        i=i-1
           
    while True: #Main movement function section
        if i+1<len(puzzle) and (puzzle[i+1][j]==" " or puzzle[i+1][j]=="E"): #If down is space, replace with 'v'
            puzzle[i][j]="v"
            i=i+1
        elif j-1>-1 and (puzzle[i][j-1]==" " or puzzle[i][j-1]=="E"): #If left is space, replace with '<'
            puzzle[i][j]="<"
            j=j-1
        elif j+1<len(puzzle[i]) and (puzzle[i][j+1]==" " or puzzle[i][j+1]=="E"): #If right is space, replace with '>'
            puzzle[i][j]=">"
            j=j+1
        elif i-1>-1 and (puzzle[i-1][j]==" " or puzzle[i-1][j]=="E"): #If up is space, replace with '^'
            puzzle[i][j]="^"
            i=i-1
        elif puzzle[i][j]=="E":
            break
        else:#Backtracking section for dead ends
            if i-1 >= 0 and (puzzle[i-1][j] == "v" or puzzle[i-1][j] == "S") : #Backtracking section
                puzzle[i][j]="."
                i -= 1
            elif i+1 < len(puzzle) and (puzzle[i+1][j] == "^" or puzzle[i+1][j] == "S"):
                puzzle[i][j]= "."
                i += 1
            elif j+1 >= 0 and (puzzle[i][j-1] == ">" or puzzle[i][j-1] == "S"):
                puzzle[i][j] = "."
                j -=1 
            elif j-1 < len(puzzle[i]) and (puzzle[i][j+1] == "<" or puzzle[i][j+1] == "S"):
                puzzle[i][j] = "."
                j +=1 
        printpuz(puzzle) #Print puzzle iteration
        rand1=False
        rand2=False
        for a in puzzle: #Check if maze is solvable or not
            for b in a:
                if b=="<" or b==">" or b=="^" or b=="v":
                    rand2=True
        if rand2==False:
            print("Error: No route could be found from start to end. Maze unsolvable.")
            break
    #printpuz(puzzle) #Print puzzle iteration
    
    
    
def main():
    
    while True:
        try:
            filename=input("Please enter a file name: ")
            myfile=open(filename,'r')
            puzzle = []
            for line in myfile: #Defining dimensions of matrix
                puzzle.append(list(line))
                if puzzle[-1][-1]=="\n":
                    puzzle[-1].pop()
           
            myfile.close()
        except FileNotFoundError:#Exit if file isn't found
            print("Error: Specified file does not exist.")
            break
        if puzzle==[]:#Exit if maze is empty
            print("Error: Specified file contains no maze.")
            break
        #inval[0]=False
        inval=corrinput(puzzle)
        if inval[0]==True:
            print("Error: Maze contains invalid characters.","Line",inval[2],"contains invalid character","'%s'" % inval[1])
            break
        #print(puzzle)
                
        
        str1="" #Printing maze
        c=findE(puzzle)
        a=findStartI(puzzle)
        if a==-1 or c==-1: #Exit if start or end doesn't exist
            break
        b=findStartJ(puzzle)
        for i in range(0,len(puzzle)):
            print(str1.join(puzzle[i]))
        findE(puzzle)
        move1(a,b,puzzle)
        break

main()



