from sage.all import *
    
def main(argv):
    G = DihedralGroup(argv[0])
    print(G.cayley_table()) 
    
if __name__ == '__main__':
    main(sys.argv[1:])