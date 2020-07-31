#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.sides = [self.a, self.b, self.c]

    def type(self):
        self.__invalid_sides()
        number_equal_sides = self.__number_of_equal_sides()
        if number_equal_sides == 1:
            return 'equilateral'
        elif number_equal_sides == 2:
            return 'isosceles'
        else:
            return 'scalene'

    def __number_of_equal_sides(self):
        return len(set(self.sides))

    def __invalid_sides(self):
        if self.__side_less_than_one():
            raise TriangleError("All sides should be greater than 0")
        if self.__sum_two_sides_less_than_the_other():
            raise TriangleError("The sum of any two sides should be greater than the third one")

    def __side_less_than_one(self):
        for side in self.sides:
            if side < 1:
                return True
        return False

    def __sum_two_sides_less_than_the_other(self):
        if self.c > (self.a + self.b) or self.a > (self.b + self.c) or self.b > (self.a + self.c):
            return True
        return False


def triangle(a, b, c):
    triangle = Triangle(a, b, c)
    return triangle.type()


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
