import defs
import unittest
class fTestCase (unittest.TestCase):
    def test_f_1(self):
        n=3
        mymas=[3,2,1]
        pyz(mymas)

        self.assertEguals(mymas,[1,2,3])

    def test_f_2(self):
        n = 3
        mymas = [3, 2, 1]
        vstav(mymas)

        self.assertEguals(mymas, [1, 2, 3])

    def test_f_3(self):
        n = 3
        mymas = [3, 2, 1]
        minmax(mymas)

        self.assertEguals(mymas, [1, 2, 3])

    def test_f_4(self):
        n = 3
        mymas = [3, 2, 1]
        sli(mymas)

        self.assertEguals(mymas, [1, 2, 3])

if __name__ == '__main__':
    unittest.main
