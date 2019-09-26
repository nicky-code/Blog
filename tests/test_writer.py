import unittest
from app.models import Writer

class WriterTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Writer class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_writer = Writer()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_writer,Writer))


if __name__ == '__main__':
    unittest.main()