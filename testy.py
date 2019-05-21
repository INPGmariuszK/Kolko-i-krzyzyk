#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from komputerboss_kolko_i_krzyzyk import *

class FirstTest(unittest.TestCase):
    def test(self):
        a = next_turn("X")
        self.assertEqual("O", a)

    def test_second_test(self):
        self.assertNotEqual("O", next_turn("O"))