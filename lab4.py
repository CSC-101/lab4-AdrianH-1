import data
import math
# Write your functions for each part in the space below.

# Part 1
#PURPOSE OF THE FUNCTION
#The function gathers parameters from a list that can also be nested and determnines the output by first interger if the lenght of the list is morethan 0.
def first_element(nested_list: list[list[int]]) -> list[int]:
    return [lst[0] for lst in nested_list if len(lst) > 0]
# unit tests
def test_first_element():
    #test case 1
    input_data = [[1, 2, 3], [4, 5], [], [6, 7, 8]]
    expected_output = [1, 4, 6]
    assert first_element(
        input_data) == expected_output, f"Expected {expected_output}, but got {first_element(input_data)}"

    #test case 2
    input_data = [[], [], []]
    expected_output = []
    assert first_element(
        input_data) == expected_output, f"Expected {expected_output}, but got {first_element(input_data)}"

test_first_element()

# Part 2
#PURPOSE OF THE FUNCTION
#The point of this functino is to gatherate parameters of points and return the x-value of these points.
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def x_coordinates(points: list[Point]) -> list[int]:
    return [point.x for point in points]

# unit tests
def test_x_coordinates():
    # Test case 1: List of points with distinct coordinates
    points = [Point(1, 2), Point(3, 4), Point(5, 6)]
    expected_output = [1, 3, 5]
    assert x_coordinates(points) == expected_output, f"Expected {expected_output}, but got {x_coordinates(points)}"
test_x_coordinates()

# Part 3
#PURPOSE OF THE FUNCTION
#This function uses an input list that is randomly generated on a graph and keeps the points that are in the first quadrant (+ X & +Y)
def are_in_positive_quadrant(points: list[Point]) -> list[Point]:
    return [point for point in points if point.x > 0 and point.y > 0]

#unit test
def test_are_in_positive_quadrant():
    points = [Point(1, 2), Point(-3, 4), Point(5, 6), Point(0, 0)]
    expected_output = [points[0], points[2]]  # Points (1, 2) and (5, 6)
    assert are_in_positive_quadrant(
        points) == expected_output, f"Expected {expected_output}, but got {are_in_positive_quadrant(points)}"

    points = [Point(-1, 2), Point(0, 4), Point(-5, -6)]
    expected_output = []  # No points in the first quadrant
    assert are_in_positive_quadrant(
        points) == expected_output, f"Expected {expected_output}, but got {are_in_positive_quadrant(points)}"

test_are_in_positive_quadrant()

# Part 4
#PURPOSE OF THE FUNCTION
#This function gets the distance between two parameters by using the Euclidean distance which is essentialy the pythagorean theorem
def distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

#unit tests
def test_distance():
    #test case 1
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    expected_output = 5.0  # sqrt((3-0)^2 + (4-0)^2) = 5
    assert math.isclose(distance(p1, p2), expected_output,
                        rel_tol=1e-9), f"Expected {expected_output}, but got {distance(p1, p2)}"

    #etst case 2
    p1 = Point(-1, -1)
    p2 = Point(-4, -5)
    expected_output = 5.0  # sqrt((-4+1)^2 + (-5+1)^2) = 5
    assert math.isclose(distance(p1, p2), expected_output,
                        rel_tol=1e-9), f"Expected {expected_output}, but got {distance(p1, p2)}"

test_distance()

# Part 5
#PURPOSE OF THE FUNCTION
#gathers two points and determines the Manhattan distance between them on a grid path such as the layout of Manhattan.
def manhattan_distance(p1: Point, p2: Point) -> float:
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)

#unit test
def test_manhattan_distance():
    p1 = Point(1, 1)
    p2 = Point(4, 5)
    expected_output = 7.0  # |4 - 1| + |5 - 1| = 3 + 4 = 7
    assert manhattan_distance(p1,
                              p2) == expected_output, f"Expected {expected_output}, but got {manhattan_distance(p1, p2)}"

    #test case 2
    p1 = Point(-1, -1)
    p2 = Point(-4, -5)
    expected_output = 7.0  # |-4 + 1| + |-5 + 1| = 3 + 4 = 7
    assert manhattan_distance(p1,
                              p2) == expected_output, f"Expected {expected_output}, but got {manhattan_distance(p1, p2)}"

test_manhattan_distance()

# Part 6
#PURPOSE OF THE FUNCTION
    #The purpose of this function is to calculate the distance between the points and how far it is from the origin (0,0)
def distance(p1: Point, p2: Point) -> float:
    # Calculate the Euclidean distance between two points
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

def distance_all(points: list[Point]) -> list[float]:
    origin = Point(0, 0)  #define the origin point (0, 0)
    return [distance(origin, point) for point in points]
#unit tests
def test_distance_all():
    # tes case 1
    points = [Point(3, 4), Point(1, 1), Point(0, 0)]
    expected_output = [5.0, math.sqrt(2), 0.0]  # Distances: 5.0, sqrt(2), 0.0
    assert all(math.isclose(d, e, rel_tol=1e-9) for d, e in zip(distance_all(points),
                                                                expected_output)), f"Expected {expected_output}, but got {distance_all(points)}"

    #test case 2
    points = [Point(-3, -4), Point(-1, -1), Point(0, 0)]
    expected_output = [5.0, math.sqrt(2), 0.0]  # Distances: 5.0, sqrt(2), 0.0
    assert all(math.isclose(d, e, rel_tol=1e-9) for d, e in zip(distance_all(points),
                                                                expected_output)), f"Expected {expected_output}, but got {distance_all(points)}"

test_distance_all()

