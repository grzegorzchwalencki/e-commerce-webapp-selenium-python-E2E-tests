import unittest
from tests.create_account_test import CreateAccountTest
from tests.sign_in_test import SignInTest
# Load tests to run
create_account_tests = unittest.TestLoader().loadTestsFromTestCase(CreateAccountTest)
sign_in_tests = unittest.TestLoader().loadTestsFromTestCase(SignInTest)

# List of tests to run
tests_to_run = [
    #create_account_tests,
    sign_in_tests
    # ... next test
]

# Create Test Suite - join tests
test_suite = unittest.TestSuite(tests_to_run)

# Run tests
unittest.TextTestRunner().run(test_suite)