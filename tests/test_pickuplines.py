import unittest
from app.models import PICKUPLINES

class TestPickUpLines(unittest.TestCase):

    def setUp(self):
        self.new_pickuplines = PICKUPLINES('title for the pitch', 'pith information')

        def tearDown(self):
            PICKUPLINES.clear_pickuplines()

        def test_instance(self):
            self.assertTrue(isinstance(self.new_pickuplines, PICKUPLINES))

        def test_check_instance_variables(self):
            self.assertEquals(self.new_pickuplines.title,'title for the pitch')
            self.assertEquals(self.new_pickuplines.pitch,'pitch information')

        def test_save_pickuplines(self):
            self.new_pickuplines.test_save_pickuplines()
            self.assertTrue(len(PICKUPLINES.all_pickuplines)>0)