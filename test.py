import re
import datetime
import sys


class Test:
    '''Testing class.
On initialization, parses the methods of the class for those that contain 'test'
Note that you will get an error message if you write methods that contain the word test but not a test number
Or if there are duplicate test method names
'''

    def __init__(self):
        self.tests = {}
        for name, method in self.__class__.__dict__.items():
            if callable(method) and "test" in name:
                try:
                    test_num = int(re.search(r'\d+', name).group())
                    if test_num in self.tests:
                        print(f'Duplicate test num {test_num}, exiting program')
                        sys.exit()
                    self.tests[test_num] = {'method': method, 'name': name.split('_', 2)[2].title()}
                except AttributeError:
                    print(f'''Failed to load test '{name}'.
If this is a unit test, make sure to include the test number.
Otherwise, remove 'test' from the method name so that it is not parsed as a unit test.
Exiting program.''')
                    sys.exit()

    def test_1_load_from_file(self):
        assert(True), "Fail text"

    def run(self):
        ''' Run all unit tests'''
        print("\nBeginning Unit Tests:\n")
        num_tests = len(self.tests)
        num_passed = 0
        start_time = datetime.datetime.now()
        for num, test in sorted(self.tests.items()):
            try:
                print(f"Test #{num} {test['name']}   Running")
                test['method'](self)
                print(f"Test #{num} {test['name']}   Passed")
                num_passed += 1
            except AssertionError as error:
                if str(error):
                    msg = f' with message\nERROR: {error}'
                else:
                    msg = f'''\
 without a message'''

                print(f"Test #{num} {test['name']}   Failed{msg}\n")
        delta_time = datetime.datetime.now() - start_time
        print(f'\nPassed {num_passed}/{num_tests} tests in {delta_time}')

if __name__ == "__main__":
    Test().run()
