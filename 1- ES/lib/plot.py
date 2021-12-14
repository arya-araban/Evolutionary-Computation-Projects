# ackley multimodal function
from numpy import *
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


def plot_func(objective, bounds):
    """This function plots a 2 parameter (x,y) objective function
    'objective' is the objective function itself.
    'range' is the range for the X axis and Y axis - in the form of tuple ([x_begin,x_end], [y_begin,y_end])
    """

    # define range for input
    r_min1, r_max1 = bounds[0][0], bounds[0][1]
    r_min2, r_max2 = bounds[1][0], bounds[1][1]
    # sample input range uniformly at 0.1 increments
    xaxis = linspace(r_min1, r_max1)
    yaxis = linspace(r_min2, r_max2)
    # create a mesh from the axis, meshes are used to get all x,y combinations
    x, y = meshgrid(xaxis, yaxis)
    # compute targets
    results = objective([x, y])
    # create a surface plot with the jet color scheme
    figure = pyplot.figure()
    axis = figure.gca(projection='3d')
    axis.plot_surface(x, y, results, cmap='jet')
    # show the plot
    pyplot.show()
