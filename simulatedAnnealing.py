import random
import math

def simulatedAnnealing(problem, T):
    state = problem.initialState()
    while T > 0:
        actions = problem.actions(state)
        action = random.choice(actions)
        nextState = problem.result(state, action)
        delata = problem.fitness(nextState)-problem.fitness(state)
        p = math.exp((-1*delata)/T)
        r = random.random()
        if(problem.fitness(nextState) > problem.fitness(state)):
            state = nextState
        elif(r <= p):
            state = nextState
        if(problem.goalTest(state) == True):
            return state
        T -= 1
    return 'temp = 0'
