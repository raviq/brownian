import numpy
from pylab import plot, show, grid, xlabel, ylabel
from brownian import brownian


def main():

    # The Wiener process parameter.
    delta = 2
    # Total time.
    T = 40.0
    # Number of steps.
    N = 1000
    # Time step size
    dt = T/N
    # Number of realizations to generate.
    m = 3
    # Create an empty array to store the realizations.
    x = numpy.empty((m,N+1))
    # Initial values of x.
    x[:, 0] = 50

    brownian(x[:,0], N, dt, delta, out=x[:,1:])

    t = numpy.linspace(0.0, N*dt, N+1)
    for k in range(m):
        plot(t, x[k])
        
    xlabel('t', fontsize=16)
    ylabel('x', fontsize=16)
    grid(True)
    show()


if __name__ == "__main__":
    main()
    
    