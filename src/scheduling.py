"""
scheduling.py

This script solves a simple scheduling problem for teacher playground duties.
The constraints of this problem are:
  - The available days of each teacher
  - The permitted duties of each teacher
  - The number of duties that can be performed by each teacher
  - The number of teachers required for each duty
"""
from pyscipopt import Model, quicksum, multidict

def flp(numstaff, numdays, numduties, workdays, dutiesperweek, staffperduty):
    model = Model("dutyroster")

    x = {} # a set of binary variables to indicate whether a member of staff is working a given duty on a given day.
    # The x variables are of dimension numduties*numdays*numstaff
    for i in range(numstaff):
        for j in range(numdays):
            for k in range(numduties):
                x[i, j, k] = model.addVar(vtype="B", name="x_%s_%s_%s"%(i, j, k))

    # The constraint for enforcing that the correct number of staff are allocated to each duty
    for j in range(numdays):
        for k in range(numduties):
           model.addCons(quicksum(workdays[i,j]*x[i,j,k] for i in range(numstaff)) == staffperduty[k], "DutyCover(%s,%s)"%(j,k))

    for i in range(numstaff):
        for k in range(numduties):
            model.addCons(quicksum(x[i,j,k] for k in range(numdays)) < dutiesperweek[i,k], "MaxDuties(%s,%s)"%(i,k))

    model.setObjective(quicksum(x[i, j, k] for i in range(numstaff) for j in range(numdays) for k in range(numduties)),
        "minimize")
    model.data = x

    return model


def read_data():
    numdays = 5
    numduties = 6
    numstaff = 23
    workdays = {}
    dutiesperweek = {}
    staffperduty = {}



if __name__ == "__main__":
    I,J,d,M,f,c = make_data()
    model = flp(I,J,d,M,f,c)
    model.optimize()

    EPS = 1.e-6
    x,y = model.data
    edges = [(i,j) for (i,j) in x if model.getVal(x[i,j]) > EPS]
    facilities = [j for j in y if model.getVal(y[j]) > EPS]

    print("Optimal value:", model.getObjVal())
    print("Facilities at nodes:", facilities)
    print("Edges:", edges)

    try: # plot the result using networkx and matplotlib
        import networkx as NX
        import matplotlib.pyplot as P
        P.clf()
        G = NX.Graph()

        other = [j for j in y if j not in facilities]
        customers = ["c%s"%i for i in d]
        G.add_nodes_from(facilities)
        G.add_nodes_from(other)
        G.add_nodes_from(customers)
        for (i,j) in edges:
            G.add_edge("c%s"%i,j)

        position = NX.drawing.layout.spring_layout(G)
        NX.draw(G,position,node_color="y",nodelist=facilities)
        NX.draw(G,position,node_color="g",nodelist=other)
        NX.draw(G,position,node_color="b",nodelist=customers)
        P.show()
    except ImportError:
        print("install 'networkx' and 'matplotlib' for plotting")
