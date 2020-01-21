import unittest
import module_dut as dut

class NamesTestCase(unittest.TestCase):
    "\"Test for name_function.py\""
    
    def test_first_last_name(self):
        "\"Do names like Janis Joplin work?\""
        formatted_name = dut.get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

#unittest.main()
if __name__ == "__main__":
    unittest.main()
