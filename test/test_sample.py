#!/usr/bin/env python

import unittest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
