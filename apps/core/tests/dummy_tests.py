# add dummy passing and failing django tests

from django.test import TestCase


class DummyPassingTest(TestCase):
    def test_passing(self):
        self.assertEqual(1, 1)


class DummyFailingTest(TestCase):
    def test_failing(self):
        self.assertNotEqual(1, 2)
