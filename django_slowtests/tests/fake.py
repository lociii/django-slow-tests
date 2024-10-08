import time

from django.test import TestCase
from freezegun import freeze_time
import time_machine


class FakeTestCase(TestCase):
    _setupClassRan = False

    @classmethod
    def setUpClass(cls):
        super(FakeTestCase, cls).setUpClass()
        cls._setupClassRan = True

    def test_slow_thing(self):
        time.sleep(1)

    def test_setup_class_was_run(self):
        self.assertTrue(self._setupClassRan)


@freeze_time('2016-02-03 12:34:56')
class FakeFreezegunTravelToPastTestCase(TestCase):
    def test_this_should_not_have_a_negative_duration(self):
        self.assertTrue(True)


@freeze_time('3017-02-03 12:34:56')
class FakeFreezegunTravelToFutureTestCase(TestCase):
    def test_this_should_not_have_very_long_duration(self):
        self.assertTrue(True)


@time_machine.travel('2016-02-03 12:34:56')
class FakeTimeMachineTravelToPastTestCase(TestCase):
    def test_this_should_not_have_a_negative_duration(self):
        self.assertTrue(True)


@time_machine.travel('3017-02-03 12:34:56')
class FakeTimeMachineTravelToFutureTestCase(TestCase):
    def test_this_should_not_have_very_long_duration(self):
        self.assertTrue(True)
