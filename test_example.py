import unittest
from example import get_greeting, other_example

class HelloworldTests(unittest.TestCase):
    
    def test_get_greeting(self):
        self.assertEqual(get_greeting(), 'Hello World!')

    def test_other_example(self):
        self.assertEqual(other_example(), 'Tested response')

if __name__ == '__main__':
    unittest.main()