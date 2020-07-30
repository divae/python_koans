#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *


def triangle(a, b, c):
    if sides_less_than_one(a, b, c) or sum_of_any_two_sides_less_than_the_third(a, b, c):
        raise TriangleError("My Message")
    elif all_slides_equals(a, b, c):
        return 'equilateral'
    elif two_slides_equals(a, b, c):
        return 'isosceles'
    else:
        return 'scalene'

def all_slides_equals(a, b, c):
    if a == b == c:
        return True

def two_slides_equals(a, b, c):
    if a == b or b == c or c == a:
        return True

def sides_less_than_one(a, b, c):
    if a < 1 or b < 1 or c < 1:
        return True

def sum_of_any_two_sides_less_than_the_third(a, b, c):
    if ((a + b) > c) or ((b + c) > a) or ((c + a) > b):
        return True

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


