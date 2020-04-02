"""
Programmer: Justin Duchatellier
Class: Algorithm Analysis
Prof: Kretlow, Betty
Date created: March 7, 2020
Date modified: March 7, 2020
An implementation of quickhull using Jarvis' method
***Uses randomly selected integers for the x, y coordinates
"""
import matplotlib.pyplot as plt
import random

"""
Gets the farthest left point, if two points are equally far,
get the one farthest up
"""


def get_left_point(array):
    min_x_point = 0
    for i in range(len(array)):
        if array[i][0] < array[min_x_point][0]:
            min_x_point = i
        elif array[i][0] == array[min_x_point][0]:
            if array[i][1] < array[min_x_point][1]:
                min_x_point = i
    return min_x_point


'''
Determines if orientation of three points in order
(start, mid, end) is in counterclockwise pattern.
'''


def pattern(start, mid, end):
    """
    Return a value indicating if counterclockwise
    1: counterclockwise
    0: not counterclockwise
    """
    direction = (mid[1] - start[1]) * (end[0] - mid[0]) - \
                (mid[0] - start[0]) * (end[1] - mid[1])
    if direction < 0:
        return 1
    else:
        return 0


"""
Create the convex hull
"""


def quick_hull(array):
    # Return if the figure has less than 3 points (figure < 3 sides)
    if len(array) < 3:
        print("You only have 2 points\nNothing printed")
        return
    # get farthest left point
    left = get_left_point(array)

    # create empty list to output the convex hull
    convex_hull = []

    # this is the first point in list for convex_hull
    convex_start = left

    while True:
        # append convex hull with farthest left point
        convex_hull.append(convex_start)

        # end point becomes the index after convex start
        end_point = (convex_start + 1) % len(array)

        for i in range(len(array)):
            if pattern(array[convex_start],
                       array[i], array[end_point]) == 1:
                end_point = i

        """
        Since the leftmost point was chosen, we find the
        most counterclockwise point to the first point
        of the convex hull. Had the rightmost point been
        chosen, the most clockwise point would be used.
        Then this new point is assigned to the next point
        of the convex hull after being given the value of
        "end_point".
        """
        convex_start = end_point

        """
        When the first point of the convex point is
        reached, break the loop.
        """
        """print("convex_start = ", convex_start, "left = ",
              left, "end_point = ", end_point)"""
        if convex_start == left:
            break

    # Connect endpoints of convex hull
    line_plot_x = []
    line_plot_y = []
    for i in convex_hull:
        line_plot_x.append(array[i][0])
        line_plot_y.append(array[i][1])
    line_plot_x.append(line_plot_x[0])
    line_plot_y.append(line_plot_y[0])
    plt.plot(line_plot_x, line_plot_y)

    # Display the points of the convex hull
    print("The points of the convex hull, starting",
          "from the farthest left point are:")
    for convex_point in convex_hull:
        print("(", array[convex_point][0], ",",
              array[convex_point][1], ")", sep="")


input_points = []
plot_array_x = []
plot_array_y = []
# randomly choose an integer between 1 and 50
num = random.randrange(1, 51)
# use the above random number and fill in this many number
# of random x and y coordinates
for n in range(num):
    plot_array_x.append(random.randrange(51))
    plot_array_y.append(random.randrange(51))
    input_points.append((plot_array_x[n], plot_array_y[n]))
plt.plot(plot_array_x, plot_array_y, 'go')
print("Below is the list of coordinates used")
print(input_points)
quick_hull(input_points)
plt.savefig("plot_from_random.png")
plt.show()
