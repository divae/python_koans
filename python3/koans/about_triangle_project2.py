#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *


class Triangle:
    def __init__(self, a, b, c):
        self.sides = sorted([a, b, c])

    def type(self):
        self.__invalid_sides()
        equal_sides = self.__get_equal_sides()
        if self.__is_equilateral(equal_sides):
            return 'equilateral'
        elif self.__is_isosceles(equal_sides):
            return 'isosceles'
        else:
            return 'scalene'

    def __invalid_sides(self):
        if self.__side_less_than_one():
            raise TriangleError("All sides should be greater than 0")
        if self.__sum_two_sides_less_than_the_other():
            raise TriangleError("The sum of any two sides should be greater than the third one")
        
    def __get_equal_sides(self):
        return len(set(self.sides))

    def __side_less_than_one(self):
        return True in [side < 1 for side in self.sides]

    def __sum_two_sides_less_than_the_other(self):
        return self.sides[0] + self.sides[1] < self.sides[2]
    
    def __is_equilateral(self, equal_sides):
        return equal_sides == 1
    
    def __is_isosceles(self, equal_sides):
        return equal_sides == 2

def triangle(a, b, c):
    return Triangle(a, b, c).type()


class AboutTriangleProject2(Koan):

    # The first assignment did not talk about how to handle errors.
    # Let's handle that part now.
    def test_illegal_triangles_throw_exceptions(self):
        # All sides should be greater than 0
        with self.assertRaises(TriangleError):
            triangle(0, 0, 0)
        with self.assertRaises(TriangleError):
            triangle(3, 4, -5)

        # The sum of any two sides should be greater than the third one
        with self.assertRaises(TriangleError):
            triangle(1, 1, 3)
        with self.assertRaises(TriangleError):
            triangle(2, 5, 2)
