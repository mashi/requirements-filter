import tempfile
import unittest
from pathlib import Path

from requirements_filter import requirements_filter as rq

requirements = """flake8==3.9.0
project==0.0.0
"""


requirements_private = r"""project @ git+https://${GITHUB_TOKEN}@github.com/user/project.git@{version}
"""


requirements_without_private = """flake8==3.9.0
"""


def write_file(filepath, filename, information):
    with open(Path(f"{filepath}/{filename}"), "w") as file_object:
        file_object.write(information)


class RequirementsFilterTest(unittest.TestCase):
    def test_true(self):
        self.assertEqual(1, 1)

    def test_twofiles(self):
        with tempfile.TemporaryDirectory() as tp:
            print(tp)
            write_file(tp, "requirements.txt", requirements)
            write_file(tp, "requirements-private.txt", requirements_private)

            rq.rqf(f"{tp}/requirements.txt", f"{tp}/requirements-private.txt")

            with open(Path(f"{tp}/requirements.txt")) as file_object:
                received = file_object.readlines()
            self.assertEqual("".join(received), requirements_without_private)


if __name__ == "__main__":
    unittest.main()
