import unittest
from app. import Source

class SourceTest(unittest.TestCase):
   def setUp(self):
       '''
       test_source checks that new news source objects are created
       '''
       self.new_source = Source('one','two','three','four','five',)

   def test_instance(self):
       self.assertTrue(isinstance(self.new_source,Source))