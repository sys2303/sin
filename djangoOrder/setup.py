import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name = 'djangoOrder',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    license='BSD License',    
    description  = 'order system',
    url = 'c:\djangoOrder',
    author   = 'your name',
    author_email  = 'email@gmail.com',
    classifiers      = [
        'Environment :: Web Environment',
        'Framework :: Django ',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OST Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
	 zip_safe=False
)

