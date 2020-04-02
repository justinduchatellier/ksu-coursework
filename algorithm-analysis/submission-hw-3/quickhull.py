"""
Programmer: Justin Duchatellier
Class: Algorithm Analysis
Prof: Kretlow, Betty
Date created: March 7, 2020
Date modified: March 7, 2020
An implementation of quickhull using Jarvis' method
"""
import matplotlib.pyplot as plt

input_array = [(1, 6), (4, 15),  (7, 7), (10, 13), (11, 6),
               (11, 18), (11, 21), (12, 10), (15, 18),
               (16, 6), (18, 3), (18, 12), (19, 15), (22, 19)]

"""
Gets the farthest left point, if two points are equally far,
get the one farthest down
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
    # get farthest left point
    left = get_left_point(array)

    # create empty list to output the convex hull
    convex_hull = []

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


plot_array_x = []
plot_array_y = []
for x, y in input_array:
    plot_array_x.append(x)
    plot_array_y.append(y)
plt.plot(plot_array_x, plot_array_y, 'go')
print("Below is the list of coordinates used")
print(input_array)
quick_hull(input_array)
plt.savefig("plot_from_hard_coded.png")
plt.show()
