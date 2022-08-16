from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit

#
# 1.Declare the solver
#

# Create the linear solver with the GLOP backend.
solver = pywraplp.Solver.CreateSolver('GLOP')
if not solver:
    exit

#
# 2.Create the variables
#

# Create the variables x and y.
x = solver.NumVar(0, 1, 'x')
y = solver.NumVar(0, 2, 'y')

print('Number of variables =', solver.NumVariables())

#
# 3.Define the constraints.
#

# Create a linear constraint, 0 <= x + y <= 2.
ct = solver.Constraint(0, 2, 'ct')
ct.SetCoefficient(x, 1)
ct.SetCoefficient(y, 1)

print('Number of constraints =', solver.NumConstraints())

#
# 4.Define the objective function.
#

# Create the objective function, 3 * x + y.
objective = solver.Objective()
objective.SetCoefficient(x, 3)
objective.SetCoefficient(y, 1)
objective.SetMaximization()

#
# 5.Invoke the solver and display the results.
#

solver.Solve()
print('Solution:')
print('Objective value =', objective.Value())
print('x =', x.solution_value())
print('y =', y.solution_value())
