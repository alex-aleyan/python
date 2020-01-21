import unittest
import module_dut as dut

# unittest.TestCase ASSERTS:
'''
assertEqual(a,b)
assertNotEqual(a,b)

assertTrue(x)
assertFalse(x)

assertIs(a,b)
assertIsNot(a,b)
assertIsNone(x)
assertIsNotNone(x)

assertIn(a,b)
assertNotIn(a,b)

assertIsInstance(a,b)
assertNotIsInstance(a,b)
'''

class NamesTestCase(unittest.TestCase):
    "\"Test for name_function.py\""
    
    def test_first_last_name(self):
        "\"Do names like Janis Joplin work?\""
        formatted_name = dut.get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        "\"Do names like Wolfgang Amadeus Mozart work?\""
        formatted_name = dut.get_formatted_name('Wolfgang','Mozart','Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

class TestAnonSurvey(unittest.TestCase):
    "\"Tests for the class AnonSurvey\""

    def test_store_single_response(self):
        "\"Test that a single response is stored properly\""
        question="What language did you first learn to speak?"
        my_survey=dut.AnonSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

#unittest.main()
if __name__ == "__main__":
    unittest.main()
