import tempfile
import unittest
from pathlib import Path

from requirements_filter import requirements_filter as rq
from requirements_filter.requirements_filter import NOT_OK

requirements = """
flake8==3.9.0
project==0.0.0
"""


requirements_at_sign = r"""project @ git+https://${GITHUB_TOKEN}@github.com/user/project.git@{version}
"""


requirements_without_private = """
flake8==3.9.0
"""


def write_file(filepath, filename, information):
    """
    Write a text file.

    Used here to save known files to test the package behavior.

    Parameters
    ----------
    filepath : str
        Path where the file will be written.

    filename : str
        Name of the file.

    information : str
        Information to be written.
    """
    with open(Path(f"{filepath}/{filename}"), "w") as file_object:
        file_object.write(information)


def convert_str_list(my_string):
    """
    Function to convert from string to list.

    The create_set() function requires a specific input.

    Parameters
    ----------
    my_string : str
        Input string.

    Returns
    -------
    list
        The input string converted to list.
    """
    return my_string.strip("\n").split("\n")


class RequirementsFilterTest(unittest.TestCase):
    def test_true(self):
        self.assertEqual(1, 1)

    def test_rqf_two_files(self):
        with tempfile.TemporaryDirectory() as tp:
            write_file(tp, "requirements.txt", requirements)
            write_file(tp, "requirements-private.txt", requirements_at_sign)

            rq.rqf(f"{tp}/requirements.txt", f"{tp}/requirements-private.txt")

            with open(Path(f"{tp}/requirements.txt")) as file_object:
                received = file_object.readlines()
            self.assertEqual("".join(received), requirements_without_private)

    def test_open_file_invalid_filename(self):
        invalid_filename = "invalid_requirements.txt"
        with self.assertRaises(SystemExit) as cm:
            rq.open_file(invalid_filename)
        self.assertEqual(cm.exception.code, NOT_OK)

    def test_open_file_valid_filename(self):
        right_filename = "requirements.txt"
        received = rq.open_file(right_filename)
        self.assertIs(type(received), list)

    def test_create_set_is_set(self):
        input_list = convert_str_list(requirements_at_sign)
        received = rq.create_set(input_list, "@")
        self.assertIsInstance(received, set)

    def test_create_set_at_sign(self):
        answer_list = ["project"]
        answer = set(answer_list)
        input_list = convert_str_list(requirements_at_sign)
        received = rq.create_set(input_list, "@")
        self.assertEqual(answer, received)

    def test_create_set_equal_sign(self):
        answer_package_list = ["flake8", "project"]
        answer_set = set(answer_package_list)
        input_list = convert_str_list(requirements)
        received = rq.create_set(input_list, "==")
        self.assertEqual(answer_set, received)

    def test_create_set_at_equal_sign(self):
        # test what happens with packages using @ delimiter
        # are applied with the "==" parameter
        answer_package_list = []
        answer_set = set(answer_package_list)
        input_list = convert_str_list(requirements_at_sign)
        received = rq.create_set(input_list, "==")
        self.assertEqual(answer_set, received)


if __name__ == "__main__":
    unittest.main()
