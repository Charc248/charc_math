try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

config = {
	'name': 'cmath',
    'version': '0.1',
    'description': 'Private collection of math functions',
    'long_description': readme(),
	'classifiers': [
		'Development Status :: 2 - Pre-Alpha',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Intended Audience :: Education'
	],
    'keywords': 'math elementary number theory simple',
    'url': 'http://github.com/storborg/funniest',
    'author': 'Mayur Dave',
    'author_email': 'm.dave@warwick.ac.uk',
    'license': 'MIT',
    'packages': ['funniest'],
    'install_requires': [
    	'markdown',
    	'nose'
    ],
    'test_suite': 'nose.collector',
    'tests_require': ['nose', 'nose-cover3'],
    'entry_points': {
    	'console_scripts': ['funniestjoke=funniest.command_line:main'],
    },
    'include_package_data': True,
    'zip_safe': False
}

setup(**config)
