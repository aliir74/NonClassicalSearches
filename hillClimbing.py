import random
from random import shuffle

def simpleHillClimbing(problem):
    state = problem.initialState()
    while True:
        actions = problem.actions(state)
        nextState = state
        for idx,a in enumerate(actions):
            neighbour = problem.result(state, a)
            if(problem.fitness(neighbour) > problem.fitness(nextState)):
                nextState = neighbour

        if(state == nextState):
            return state
        state = nextState

def stochasticHillClimbing(problem):
    state = problem.initialState()
    while True:
        actions = problem.actions(state)
        betterNeighbours = []
        for idx, a in enumerate(actions):
            neighbour = problem.result(state, a)
            if (problem.fitness(neighbour) > problem.fitness(state)):
                betterNeighbours.append(neighbour)
        if(len(betterNeighbours) == 0):
            return state
        state = random.choice(betterNeighbours)

def firstChoiceHillClimbing(problem):
    state = problem.initialState()
    while True:
        actions = problem.actions(state)
        randoms = [i for i in len(actions)]
        shuffle(randoms)
        nextState = state
        for r in randoms:
            action = actions[r]
            neighbour = problem.result(state, action)
            if (problem.fitness(neighbour) > problem.fitness(state)):
                nextState = neighbour
                break
        if(nextState == state):
            return state

def randomRestartHillClimbing(problem):
    state = problem.initialState()
    while True:
        actions = problem.actions(state)
        nextState = state
        for idx,a in enumerate(actions):
            neighbour = problem.result(state, a)
            if(problem.fitness(neighbour) > problem.fitness(nextState)):
                nextState = neighbour

        if(state == nextState):
            if(problem.goalTest(state) == True):
                return state
            else:
                nextState = problem.randomStart()
        state = nextState