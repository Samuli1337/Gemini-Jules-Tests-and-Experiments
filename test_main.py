import io
import sys
import unittest
from main import get_hello_message, main


class TestMain(unittest.TestCase):
    def test_get_hello_message(self):
        self.assertEqual(get_hello_message(), "Hello, World!")

    def test_main_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            main()
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
