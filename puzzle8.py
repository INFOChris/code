import random
import numpy as np

# create goal state
goalState =np.array([[1,2,3],[8,0,4],[7,6,5]])


# create random playgraound
# current_state = np.arange(9).reshape((3,3))


current_state =np.array([[2,8,3],[1,6,4],[7,0,5]])
# get position of  the 0
x, y= np.where(current_state == 0)

x =int(x)
y =int(y)


pos = (x, y)

print(current_state)
current_state = np.random.permutation(current_state)
print(current_state)




current_state = goalState


def move_current_state(current_state, dir,pos):
    # up:= 0 right:= 1 down:=2 left:= 3
    if
    pass





print(np.array_equal(current_state, goalState))


def check_goal(current_state):
    ''' args: current_state (numpyarray)
        return bool (if the two arrays are the same True
    '''
    if np.array_equal(current_state,goalState):
        return True
    return False









