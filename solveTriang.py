import sys
import numpy as np
from timeit import default_timer as timer

def solveTriang(A, b, upperFlag=False, verbose=False):
    
    N = A.shape[0]
    x = np.zeros(N)

    outerLoopRange = range(N)
    if upperFlag:
        outerLoopRange = range(N-1,-1,-1)

    if verbose:
        print("Matriz A:")
        print(A)
        print("\nVetor b:")
        print(b)
        start = timer()

    for i in outerLoopRange:
        partialSum = 0
        innerLoopRange = range(i)
        if upperFlag:
            innerLoopRange = range(i+1,N)
        for j in innerLoopRange:
            partialSum += A[i,j]*x[j]
        x[i] = (b[0,i] - partialSum)/A[i,i]

    if verbose:
        end = timer()

        print("\nTempo de execução total aproximado: %e segundos" % (end - start))
        print("Tempo aproximado por iteração: %e segundos" % ((end - start)/N))

        print("\nSolução encontrada:")
        print(x[:,None])

        print("\nVetor de resíduos:")
        print(b - A @ x)

    return x

if __name__ == "__main__":
    solveTriang(A=np.array(np.mat(sys.argv[1]),dtype=float),
            b=np.array(np.mat(sys.argv[2]),dtype=float),
            upperFlag=str(sys.argv[3]).lower() == "u",
            verbose=True)
