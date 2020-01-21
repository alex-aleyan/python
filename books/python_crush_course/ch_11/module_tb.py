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

    def setUp(self):
        question="What language did you first learn to speak?"
        self.my_survey=dut.AnonSurvey(question)
        self.responses=['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        "\"Test that a single response is stored properly\""
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        "\"Test that three individual responses are stored properly.\""

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        

#unittest.main()
if __name__ == "__main__":
    unittest.main()
