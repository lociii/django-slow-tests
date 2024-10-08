from unittest.mock import patch
from unittest import TestResult

from django.test import TestCase

from django_slowtests.testrunner import TimingSuite


class TimingSuiteTests(TestCase):
    def test_add_a_test(self):
        from .fake import FakeTestCase
        suite = TimingSuite()
        result = TestResult()
        suite.addTest(FakeTestCase('test_slow_thing'))
        suite.addTest(FakeTestCase('test_setup_class_was_run'))
        with patch.object(suite, 'save_test_time') as mock:
            suite.run(result)
        self.assertEqual(len(suite._tests), 2)
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(mock.call_count, 2)

    def test_timing_is_correct_when_freezegun_sets_time_in_past(self):
        from .fake import FakeFreezegunTravelToPastTestCase
        suite = TimingSuite()
        result = TestResult()
        suite.addTest(FakeFreezegunTravelToPastTestCase(
            'test_this_should_not_have_a_negative_duration'
        ))
        with patch.object(suite, 'save_test_time') as mock:
            suite.run(result)
        test_name = str(suite._tests[0])
        mock.assert_called_once()
        self.assertEqual(mock.call_args_list[0][0][0], test_name)
        self.assertTrue(mock.call_args_list[0][0][1] > 0)
        self.assertTrue(mock.call_args_list[0][0][1] < 1)

    def test_timing_is_correct_when_timemachine_sets_time_in_past(self):
        from .fake import FakeTimeMachineTravelToPastTestCase
        suite = TimingSuite()
        result = TestResult()
        suite.addTest(FakeTimeMachineTravelToPastTestCase(
            'test_this_should_not_have_a_negative_duration'
        ))
        with patch.object(suite, 'save_test_time') as mock:
            suite.run(result)
        test_name = str(suite._tests[0])
        mock.assert_called_once()
        self.assertEqual(mock.call_args_list[0][0][0], test_name)
        self.assertTrue(mock.call_args_list[0][0][1] > 0)
        self.assertTrue(mock.call_args_list[0][0][1] < 1)

    def test_timing_is_correct_when_freezegun_sets_time_in_future(self):
        from .fake import FakeFreezegunTravelToFutureTestCase
        suite = TimingSuite()
        result = TestResult()
        suite.addTest(FakeFreezegunTravelToFutureTestCase(
            'test_this_should_not_have_very_long_duration'
        ))
        with patch.object(suite, 'save_test_time') as mock:
            suite.run(result)
        test_name = str(suite._tests[0])
        self.assertEqual(mock.call_args_list[0][0][0], test_name)
        self.assertTrue(mock.call_args_list[0][0][1] > 0)
        self.assertTrue(mock.call_args_list[0][0][1] < 1)

    def test_timing_is_correct_when_timemachine_sets_time_in_future(self):
        from .fake import FakeTimeMachineTravelToFutureTestCase
        suite = TimingSuite()
        result = TestResult()
        suite.addTest(FakeTimeMachineTravelToFutureTestCase(
            'test_this_should_not_have_very_long_duration'
        ))
        with patch.object(suite, 'save_test_time') as mock:
            suite.run(result)
        test_name = str(suite._tests[0])
        self.assertEqual(mock.call_args_list[0][0][0], test_name)
        self.assertTrue(mock.call_args_list[0][0][1] > 0)
        self.assertTrue(mock.call_args_list[0][0][1] < 1)
