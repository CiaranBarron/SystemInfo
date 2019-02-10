from setuptools import setup
setup(
    name='systeminfo',
    version='0.1',
    description='Basic system information',
    url='',
    author='Ciaran Barron',
    author_email='ciaran.barron.1@ucdconnect.ie',
    license='MIT',
    packages=['systeminfo'],
    entry_points={
        'console_scripts':['COMP30830systeminfo=systeminfo.main:main']
        }
    )
