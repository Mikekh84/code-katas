from setuptools import setup


setup(
    name='Code Katas',
    description='Solutions to Code Katas.',
    version=0.1,
    author='Mike Harrison',
    author_email='sample@sample.com',
    license='MIT',
    py_modules=['parenthetics'],
    package_dir={'': 'src'},
    instal_requires=[],
    extra_requires={'test': ['pytest', 'tox']},
)
