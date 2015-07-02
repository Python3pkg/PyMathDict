# Ref: http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2
from setuptools import setup


setup(name='MathDict',
      version='0.3',
      packages=['MathDict'],
      url='http://github.com/MBALearnsToCode/PyMathDict',
      author='Vinh Luong (a.k.a. MBALearnsToCode)',
      author_email='MBALearnsToCode@UChicago.edu',
      description='Python Dict/Mapping sub-class that can work with mathematical operators',
      long_description=open('README.txt').read(),
      license='MIT License')
