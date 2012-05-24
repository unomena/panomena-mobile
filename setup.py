from setuptools import setup, find_packages

setup(
    name='panomena-mobile',
    description='Panomena Mobile',
    version='0.0.7',
    author='',
    license='Proprietory',
    url='http://www.unomena.com/',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    dependency_links = [],
    install_requires = [
        'Django',
    ],
    zip_safe=False,
)
