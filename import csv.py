import csv
import unittest

class RomanNumerals:
    roman_numeral_map = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
                         ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                         ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))

    def to_roman(self, num):
        """Convert decimal number to Roman numeral."""
        if not (0 < num < 4000):
            raise ValueError("Number must be between 1 and 3999")
        result = ""
        for numeral, integer in self.roman_numeral_map:
            while num >= integer:
                result += numeral
                num -= integer
        return result

    def from_roman(self, s):
        """Convert Roman numeral to decimal number."""
        result = 0
        index = 0
        for numeral, integer in self.roman_numeral_map:
            while s[index:index + len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        return result

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

class RomanDecimalConverter(RomanNumerals):
    def __init__(self, file_name='conversion.csv'):
        self.file_name = file_name

    def save_to_file(self, data):
        """Save data to a CSV file."""
        with FileManager(self.file_name, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def load_from_file(self):
        """Load data from a CSV file."""
        with FileManager(self.file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

class TestRomanNumerals(unittest.TestCase):
    def setUp(self):
        self.converter = RomanDecimalConverter()

    def test_to_roman(self):
        self.assertEqual(self.converter.to_roman(1), 'I')
        self.assertEqual(self.converter.to_roman(3999), 'MMMCMXCIX')

    def test_from_roman(self):
        self.assertEqual(self.converter.from_roman('I'), 1)
        self.assertEqual(self.converter.from_roman('MMMCMXCIX'), 3999)

if __name__ == '__main__':
    unittest.main()