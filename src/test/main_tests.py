import unittest
from main import get_config
import os


class MainTest_get_config(unittest.TestCase):
    def test_should_return_correct_value_from_os_environ(self):
        # prepare
        os.environ['test_config'] = 'test_value'

        # run
        result = get_config('test_config')

        # assert
        self.assertEqual(result, 'test_value')
