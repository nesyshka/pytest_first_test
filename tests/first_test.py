from unittest import TestCase
import pytest
from app.calculator import Calculator

class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_failed(self):
       assert self.calc.multiply(self, 2, 2) == 5

    def test_devision_calculate_correctly(self):
        assert self.calc.devision(self, 4, 2) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 6, 2) == 4

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 6, 2) == 8

