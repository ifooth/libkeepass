from setuptools import setup


setup(
    name="libkeepass",
    version="0.1.2",
    packages=["libkeepass"],
    author="Lukas Koell",
    author_email="phpwutz@gmail.com",
    description="A library to access keepass v3 (keepass1) and v4 (keepass2) files",
    license="GPL",
    keywords="keepass library",
    url="https://github.com/phpwutz/libkeepass",   # project home page, if any
    install_requires=["lxml", "nose", "pycrypto"],
    test_suite="tests"
)
