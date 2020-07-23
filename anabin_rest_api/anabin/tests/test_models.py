
from django.test import TestCase
from anabin.models import Institutions

class InstitutionsTest(TestCase):
    """ Test module for Institutions model """

    def setUp(self):
        Institutions.objects.create(id=3, institution='test1')
        Institutions.objects.create(id=6, institution='test2')
    
    def test_institution_id(self):
        test1 = Institutions.objects.get(id=3)
        test2 = Institutions.objects.get(id=6)
        self.assertEqual(
            test1.get_institution(), "3 belongs to test1")
        self.assertEqual(
            test2.get_institution,(), "6 belongs to test2")