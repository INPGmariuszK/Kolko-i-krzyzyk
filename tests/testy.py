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
        
    def test_false_move(self)
        self.assertEqual("To pole jest zajęte", false_move())

 
class HumanMoveTest(unittest.TestCase):
    def test(self):
        self.assertEqual("Jaki będzie Twój ruch? (0 - 8):", human_move(10, human))
        self.assertEqual(4, human_move(4, human)
