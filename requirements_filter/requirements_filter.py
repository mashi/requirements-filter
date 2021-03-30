# The exit(1) is used to indicate error in pre-commit
NOT_OK = 1


def rqf(file1="requirements.txt", file2="requirements-private.txt"):
    requirements = open_file(file1)
    private_txt = open_file(file2)

    at_sign_set = create_set(private_txt, "@")

    requirements_without_at_sign = remove_common_elements(
        requirements, at_sign_set, "@"
    )
    requirements_without_equal_sign = remove_common_elements(
        requirements_without_at_sign, at_sign_set, "=="
    )

    # the file1 will be overwritten
    write_file(file1, requirements_without_equal_sign)


def remove_common_elements(requirements, private_set, delimiter="@"):
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
        package_at_sign = package.split(delimiter)[0].strip()
        if package_at_sign not in private_set:
            requirements_without_private.append(package)
    return requirements_without_private


def open_file(filename):
    """
    Open txt file.

    Parameters
    ----------
    filename : str
        Name of the file to be opened.

    Returns
    -------
    list
        List of strings with the packages names and versions.
    """
    try:
        with open(filename) as file_object:
            requirements = file_object.readlines()
        return requirements
    except FileNotFoundError:
        print(f"{filename} not found.")
        exit(NOT_OK)


def create_set(package_list, delimiter):
    """
    Create a set of packages to be excluded.

    This function receives a list of strings, takes the packages' names
    and transforms them to a set.

    If the list contains packages with @ but the delimiter input is '==',
    then the package is ignored.

    Parameters
    ----------
    package_list : list
        List of strings with each element representing a package name
        and version.

    Returns
    -------
    set
        Set with the package names.
    """
    list_of_package_names = []
    for package in package_list:
        if delimiter in package:
            package_name = package.split(delimiter)
            list_of_package_names.append(package_name[0].strip())
    package_set = set(list_of_package_names)
    return package_set


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
