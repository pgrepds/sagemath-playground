from sage.all import *
    
def main():
    G = AlternatingGroup(4)
    graph=G.cayley_graph()
    graph.show()
    print(G.orbits())
    
if __name__ == '__main__':
    main()