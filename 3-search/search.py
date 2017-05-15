# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print( "Start:", problem.getStartState() )
    print( "Is the start a goal?", problem.isGoalState(problem.getStartState()) )
    print( "Start's successors:", problem.getSuccessors(problem.getStartState()) )
    """
    path = [problem.getStartState()]
    actions = []
    successors = []
    visitedStates = [problem.getStartState()]
    currentState = path[-1]
    while not problem.isGoalState(currentState):
        successors=problem.getSuccessors(currentState)
        index = 0
        for x in successors:
            if visitedStates.__contains__(x[0]):
                index = index + 1
            else:
                break
        if index == len(successors):
            path.pop()
            actions.pop()
            currentState = path[-1]
        else:
            path.append(successors[index][0])
            actions.append(successors[index][1])
            visitedStates.append(successors[index][0])
            currentState = path[-1]
    return actions


    #util.raiseNotDefined()


def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"
    actions = []
    queue = []
    successors = problem.getSuccessors(problem.getStartState())
    for x in successors:
        queue.append(x[0])
        actions.append([x[1]])
    visited = [problem.getStartState]
    while queue:
        state = queue.pop(0)
        path = actions.pop(0)
        if problem.isGoalState(state):
            return path
        elif state not in visited:
            visited.append(state)
            successors=problem.getSuccessors(state)
            for successor in successors:
                new_path=[]
                for x in path:
                    new_path.append(x)
                new_path.append(successor[1])
                actions.append(new_path)
                queue.append(successor[0])
    #util.raiseNotDefined()


def uniformCostSearch(problem):
    actions = []
    explored = []
    currentState = [problem.getStartState(),None,0]
    while not problem.isGoalState(currentState):
        successors=problem.getSuccessors(currentState[0])
        if problem.isGoalState(currentState[0]):
            return currentState[1]
        lowestcost = 99999
        cheapestState = None
        new_cost = currentState[2]
        for state in successors:
            if state[2] <= lowestcost:
                if state not in explored:
                    lowestcost = state[2]
                    cheapestState = state
                    explored.append(state)
                    new_cost = currentState[2] + cheapestState[2]
        if lowestcost == 99999:
            return []
        currentState = [cheapestState[0],[currentState[1],cheapestState[1]],new_cost]

    #util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    "Bonus assignment: Adjust the getSuccessors() method in CrossroadSearchAgent class"
    "in searchAgents.py and test with:"
    "python run.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic,prob=CrossroadSearchProblem"

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
