# Ref: http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2
# PyPI distribution reference: https://packaging.python.org/en/latest/distributing.html#uploading-your-project-to-pypi
# PyPI distribution reference: http://peterdowns.com/posts/first-time-with-pypi.html
# Python distribution reference:
# http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2
# SetupTools reference: https://pythonhosted.org/setuptools/setuptools.html
# Python reference: https://docs.python.org/2/reference/datamodel.html
# Python reference: https://docs.python.org/2/library/operator.html
from setuptools import setup


setup(
    name='MathDict',
    version='0.1.3',
    packages=['MathDict'],
    url='https://github.com/MBALearnsToCode/PyMathDict',
    author='Vinh Luong (a.k.a. MBALearnsToCode)',
    author_email='MBALearnsToCode@UChicago.edu',
    description='Python dict / collections Mapping sub-class that can work with mathematical operators',
    long_description='(please read README.md on GitHub repo)',
    license='MIT License',
    install_requires=['FrozenDict', 'HelpyFuncs', 'SymPy'],
    classifiers=[],   # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='math dict')
