import unittest
import cafeteria

class CafeteriaTesting(unittest.TestCase):
    def testBeverageNameSizeLimit(self):
        # Should return false if the name exceds 2-15 chars
        test1 = "A"
        test2 = "LongestBeverageName"

        result1 = cafeteria.checkBeverageName(test1)
        result2 = cafeteria.checkBeverageName(test2)

        self.assertFalse(result1)
        self.assertFalse(result2)

    def testMinimunAndMaximunLengths(self):
        # Should return True for both maximun and minimun names lengths
        test1 = "Hi"
        test2 = "AAAAAAAAAAAA"

        result1 = cafeteria.checkBeverageName(test1)
        result2 = cafeteria.checkBeverageName(test2)

        self.assertTrue(result1)
        self.assertTrue(result2)

    def testNameInsideRange(self):
        # Should return true for names inside the given length range
        test1 = "CocaCola"

        result1 = cafeteria.checkBeverageName(test1)

        self.assertTrue(result1)

    def testValidBeverageName(self):
        # The name should only have alphabetical characters
        test1 = "Coca10"
        test2 = " "
        test3 = "1 "
        test4 = "Coca Cola"
        test5 = ""

        result1 = cafeteria.checkBeverageName(test1)
        result2 = cafeteria.checkBeverageName(test2)
        result3 = cafeteria.checkBeverageName(test3)
        result4 = cafeteria.checkBeverageName(test4)
        result5 = cafeteria.checkBeverageName(test5)

        self.assertFalse(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)
        self.assertFalse(result4)
        self.assertFalse(result5)

    def testSizesAreOrdered(self):
        # Should return true if sizes are ordered
        test1 = ["2", "3", "4", '10']

        result1 = cafeteria.checkSizes(test1)

        self.assertTrue(result1)

        # Should return false if sizes are unordered
        test2 = ["3", "2", "4", "10"]

        result2 = cafeteria.checkSizes(test2)

        self.assertFalse(result2)

    def testExcedSizesLengthRanges(self):
        # Should return false if the maximun quantity of sizes is exceded
        test1 = ["2", "3", "4", "5", "6", "10"]

        result1 = cafeteria.checkSizes(test1)

        self.assertFalse(result1)

        # Should return false if the no size is added
        test2 = []

        result2 = cafeteria.checkSizes(test2)

        self.assertFalse(result2)

    def testExcedSizesGivenRange(self):
        # Should return false if the maximun range is exceded
        test1 = ["49"]

        result1 = cafeteria.checkSizes(test1)

        self.assertFalse(result1)

        # Should return false if the minimun range is exceded
        test2 = ["0"]

        result2 = cafeteria.checkSizes(test2)

        self.assertFalse(result2)


    def testSizesIsNotADigit(self):
        # Should return false if sizes has a non-digit character
        test1 = ["2", "a", "b"]
        test2 = ["a"]
        test3 = ["1", "2", "3", "4", "a"]

        result1 = cafeteria.checkSizes(test1)
        result2 = cafeteria.checkSizes(test2)
        result3 = cafeteria.checkSizes(test3)

        self.assertFalse(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)

    def testSizesAreRepeated(self):
        # Should return false if sizes are repeated
        test1 = ["2", "2"]
        test2 = ["2", "2", "3", "5", "5"]

        result1 = cafeteria.checkSizes(test1)
        result2 = cafeteria.checkSizes(test2)

        self.assertFalse(result1)
        self.assertFalse(result2)

    def testAddMaximunAndMinimumSizes(self):
        # Should return true if sizes length is the maximun or minimum allowed
        test1 = ["1"]
        test2 = ["1", "2", "3", "4", "5"]

        result1 = cafeteria.checkSizes(test1)
        result2 = cafeteria.checkSizes(test2)

        self.assertTrue(result1)
        self.assertTrue(result2)

    def testAddSizesInsideTheGivenLengthRange(self):
        # Shoould return true if sizes does not exced the given limits
        test1 = ["1", "2"]
        test2 = ["1", "2", "3"]
        test3 = ["1", "2", "3", "4"]

        result1 = cafeteria.checkSizes(test1)
        result2 = cafeteria.checkSizes(test2)
        result3 = cafeteria.checkSizes(test2)

        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertTrue(result3)

    def testValidateGeneralFormat(self):
        # Should return false if values are not separated by a comma
        test1 = "beverage123"
        formatedTest1 = cafeteria.formatData(test1)

        result1 = cafeteria.checkData(formatedTest1)

        self.assertFalse(result1)

        # Should return true if values are separated by a comma
        test2 = "beverage, 1, 2, 3, 4"
        formatedTest2 = cafeteria.formatData(test2)

        result2 = cafeteria.checkData(formatedTest2)

        self.assertTrue(result2)

        # Should ignore white spaces
        test3 = "beverage,     1,2,  3,    4"
        formatedTest3 = cafeteria.formatData(test3)

        result3 = cafeteria.checkData(formatedTest3)

        self.assertTrue(result3)


if __name__ == '__main__':
    unittest.main()