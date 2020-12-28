import unittest
from main import *

class TestSolution(unittest.TestCase):
  def test_solution_1(self):
    self.assertEqual(solution(1), solution_facile(1))

  def test_solution_2(self):
    self.assertEqual(solution(2), solution_facile(2))

  def test_solution_3(self):
    self.assertEqual(solution(3), solution_facile(3))

  def test_solution_4(self):
    self.assertEqual(solution(4), solution_facile(4))

  def test_solution_100(self):
    self.assertEqual(solution(100), solution_facile(100))

class TestSolutionFacile(unittest.TestCase):
  def test_solution_facile_1(self):
    self.assertEqual(solution_facile(1), 1)

  def test_solution_facile_2(self):
    self.assertEqual(solution_facile(2), 7)

  def test_solution_facile_3(self):
    self.assertEqual(solution_facile(3), 28)

  def test_solution_facile_4(self):
    self.assertEqual(solution_facile(4), 72)

  def test_solution_facile_5(self):
    self.assertEqual(solution_facile(5), 177)

  def test_solution_facile_6(self):
    self.assertEqual(solution_facile(6), 303)

class TestPPCM(unittest.TestCase):
  def test_6_4(self):
    self.assertEqual(ppcm(6, 4), 12)

class TestFactor(unittest.TestCase):

  def test_1(self):
    self.assertEqual(factor(1), {1: 1})

  def test_2(self):
    self.assertEqual(factor(2), {2: 1})

  def test_3(self):
    self.assertEqual(factor(3), {3: 1})

  def test_4(self):
    self.assertEqual(factor(4), {2: 2})

  def test_5(self):
    self.assertEqual(factor(5), {5: 1})

  def test_6(self):
    self.assertEqual(factor(6), {2: 1, 3: 1})

  def test_7(self):
    self.assertEqual(factor(7), {7: 1})

  def test_8(self):
    self.assertEqual(factor(8), {2: 3})

  def test_10000000000000(self):
    self.assertEqual(factor(10000000000000), {2: 13, 5: 13})

class TestDivisors(unittest.TestCase):
  def test_divisors_12(self):
    self.assertEqual(list(divisors(12)), [1, 2, 4, 3, 6, 12])

class TestPhi(unittest.TestCase):
  def test_phi_1(self):
    self.assertEqual(phi(1), 1)

  def test_phi_2(self):
    self.assertEqual(phi(2), 1)

  def test_phi_3(self):
    self.assertEqual(phi(3), 2)

  def test_phi_4(self):
    self.assertEqual(phi(4), 2)

  def test_phi_5(self):
    self.assertEqual(phi(5), 4)

  def test_phi_6(self):
    self.assertEqual(phi(6), 2)

class TestLCMSum(unittest.TestCase):
  def test_lcmsum_1(self):
    self.assertEqual(lcmsum(1), 1)

  def test_lcmsum_2(self):
    self.assertEqual(lcmsum(2), 4)

  def test_lcmsum_5(self):
    self.assertEqual(lcmsum(5), 55)


if __name__ == "__main__":
  unittest.main()
