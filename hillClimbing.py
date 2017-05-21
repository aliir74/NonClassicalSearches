import random

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