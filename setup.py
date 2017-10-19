from setuptools import setup

setup(
    name='sutil',
    version='0.1',
    author='Bret Barker',
    author_email='bret.barker@canonical.com',
    scripts=['sutil.py'],
    url='http://pypi.python.org/pypi/sutil/',
    license='LICENSE',
    description='Snap utils',
    install_requires=[
        "requests",
        "pymacaroons",
    ],
    test_suite='tests',
)
