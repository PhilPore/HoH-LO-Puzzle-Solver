import sys
import copy
from collections import deque
puz_mat =[[False for i in range(3)] for _ in range(3)]
alt_mat = [False for i in range(9)]

"""
0 1 2 
3 4 5
6 7 8


"""
class Node:
    def __init__(self, seq, board_state):
        #to do
        self.seq = list(seq)
        self.board_state = list(board_state)
    def __str__(self):
        #print(self.seq)
        stri = ""
        for i in range(3):
            for j in range(3):
                stri+=f"{self.board_state[i*3+j]} " 
            stri+="\n"
        return f"{self.seq}\n{stri}"
                   


def toggle(ind,mat):
    fake_mat = copy.deepcopy(mat)
    fake_mat[ind] = not fake_mat[ind]
    if ind%3-1 >= 0:
        #print(ind-1)
        fake_mat[ind-1] = not fake_mat[ind-1]
    if ind%3+1 < 3:
        #print(ind+1)
        fake_mat[ind+1] = not  fake_mat[ind+1] 
    if ind+3 < 9:
        #print(ind+3)
        fake_mat[ind+3] = not fake_mat[ind+3]
    if ind-3 >= 0:
        #print(ind-3)
        fake_mat[ind-3] = not fake_mat[ind-3]
    
    #for i in range(0,9):
    #    print(f"{i} {fake_mat[i]} ",end="")
    #    if (i+1)%3 == 0:
    #        print("\n")
    return fake_mat

def find_path(start_state):
    frontier = deque([start_state])
    explored = [] #we put the board states in here.
    #alt_explored = [] we can put the sequences in here

    while frontier:
        State = frontier.popleft()
        if State.board_state not in explored:
            complete = True
            for i in range(9):
                if State.board_state[i] == False:
                    complete = False
                    break
            if complete:
                return State
            else:
                temp_arr = list(State.seq)
                for i in range(9):
                    temp_arr.append(i)
                    frontier.append(Node(temp_arr,toggle(i,State.board_state)))
                    temp_arr.pop()
            explored.append(State.board_state)
        

    



    return None

#more tests need 2 be done
#x = toggle(0, alt_mat)
#for i in range(3):
#    for j in range(3):
#        print(x[i*3+j],end = " ")
#    print("\n")
#print(x)
fle = sys.argv[1]
toggles = open(fle)
readthru = toggles.readlines()
#print(readthru)
for i in range(len(readthru)):
    if readthru[i] == '\n':
        break
    alt_mat[int(readthru[i].strip())] = True


S = Node([],alt_mat)
print(S)
sol = find_path(S)
print(sol)
#x = alt_mat
#print(x)
#for i in sol.seq:
#    x = toggle(i,x)
#    for i in range(3):
#        for j in range(3):
#            print(x[i*3+j],end = " ")
#        print("\n")
#    print("---")


#x = toggle(7,x)
#print(x)
"""
x = toggle(4,alt_mat)
for i in range(3):
    for j in range(3):
        print(x[i+j],end=" ")
    print("\n")
print(x)
print(alt_mat)
#x[-1] = True
#print(x)
#print(alt_mat)
"""