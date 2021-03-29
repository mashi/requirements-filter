# The exit(1) is used to indicate error in pre-commit
NOT_OK = 1
OK = 0


def rqf(file1="requirements.txt", file2="requirements-private.txt"):
    requirements = open_file(file1)
    private_txt = open_file(file2)

    private_set = create_set(private_txt)

    requirements_without_private = remove_common_elements(
        requirements, private_set
    )

    # the file1 will be overwritten
    write_file(file1, requirements_without_private)


def remove_common_elements(requirements, private_set):
    """
    Remove the common elements between requirements and private_set.

    Note that this is *not* an XOR operation: packages that do not
    exist in requirements are not included.

    Parameters
    ----------
    requirements : str
        String with the packages from the requirements file.

    private_set : set
        Set with the names of packages to be removed from requirements.
    """
    requirements_without_private = []
    for package in requirements:
        package_at_sign = package.split("@")[0].strip()
        package_equalequal = package.split("==")[0].strip()
        if package_at_sign not in private_set:
            if package_equalequal not in private_set:
                requirements_without_private.append(package)
    return requirements_without_private


def open_file(filename):
    """
    Open txt file.

    Parameters
    ----------
    filename : str
        Name of the file to be opened.
    """
    try:
        with open(filename) as file_object:
            requirements = file_object.readlines()
        return requirements
    except FileNotFoundError:
        print(f"{filename} not found.")
        exit(NOT_OK)


def create_set(private_txt):
    """
    Create a set of packages to be excluded.

    This function receives a string, takes the package name
    and converts it to a set.

    Parameters
    ----------
    private_txt : str
        String with the name and version of the packages.
    """
    private = []
    for line in private_txt:
        package_name = line.split("@")
        private.append(package_name[0].strip())
    private_set = set(private)
    return private_set


def write_file(file1, requirements_without_private):
    """
    Write string information into a file.

    Parameters
    ----------
    file1 : str
        Name of the file where the information will be saved.

    requirements_without_private : str
        Information to be saved.
    """
    with open(file1, "w") as file_save:
        for line in requirements_without_private:
            file_save.write(line)


if __name__ == "__main__":
    rqf()
