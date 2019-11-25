import unittest

# This test file bootstraps the tests located at ./tests and runs ALL test files
# as long as the test file matches the regex `pattern` `*test*.py`

if __name__ == '__main__':
    suite = unittest.TestLoader().discover('tests', pattern='*test*.py')
    runner = unittest.TextTestRunner(verbosity=2).run(suite)