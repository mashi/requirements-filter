if __name__ == "__main__":
    with open("requirements.txt") as file_object:
        requirements = file_object.readlines()
    with open("requirements-private.txt") as file_object:
        private_txt = file_object.readlines()

    private = []
    for line in private_txt:
        package_name = line.split("@")
        private.append(package_name[0].strip())
    private_set = set(private)

    requirements_without_private = []
    for package in requirements:
        package_at_sign = package.split("@")[0].strip()
        package_equalequal = package.split("==")[0].strip()
        if package_at_sign not in private_set:
            if package_equalequal not in private_set:
                requirements_without_private.append(package)

    with open("requirements.txt", "w") as file_save:
        for line in requirements_without_private:
            file_save.write(line)
