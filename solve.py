import sys
import ast
from phcpy.solver import solve


syst = ast.literal_eval(sys.argv[1])
pref = sys.argv[2]

with open('tmp/'+pref+'solve.txt','w') as file:
    sol = solve(syst, verbose=0, tasks=2)

    file.write(str(sol))
