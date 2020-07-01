import os
import sys
import pulp

def main():
    #線形計画の定義
    problem = pulp.LpProblem('problem', pulp.LpMaximize)

    #変数の定義
    x1 = pulp.LpVariable('x1', lowBound = 0) 
    x2 = pulp.LpVariable('x2', lowBound = 0)
    x3 = pulp.LpVariable('x3', lowBound = 0) 

    #目的関数の定義
    problem += x1 + x2 + x3

    #制約条件の定義
    problem += x1 - x2 + 3*x3 == 8
    problem += 2*x1 - 3*x2 - x3 == 1

    #解く
    status = problem.solve()
    print(pulp.LpStatus[status])

    #結果表示
    print("Result")
    print("x1:",x1.value())
    print("x2:",x2.value())
    print("x3:",x3.value())
    print("problem:",problem.objective.value())
    
if __name__ == "__main__":
    main()
