#!/usr/bin/python3
"""This is a base model testing file"""


import unittest
from datetime import datetime, date


from models.base_model import BaseModel


class Test_Base_Model(unittest.TestCase):
    """This tests the methods in the class BaseModel"""

    def setUp(self):
        """The initial setup function"""

        self.Base1 = BaseModel()
        self.assertEqual(self.Base1.updated_at, self.Base1.created_at)

    def test_save(self):
        """Test the save method of the class BaseModel"""

        x = self.Base1.updated_at
        self.Base1.save()
        y = self.Base1.updated_at
        self.assertFalse(x == y)


if __name__ == "__main__":
    unittest.main()
