try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

def readme():
	with open('README.md') as f:
		return f.read()

config = {
	'name': 'charc_math',
	'version': '1.0',
	'description': 'Private collection of math functions',
	'long_description': readme(),
	'classifiers': [
		'Development Status :: 2 - Pre-Alpha',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Intended Audience :: Education'
	],
	'keywords': 'math elementary number theory simple',
	'url': 'https://github.com/Charc248/cmath',
	'author': 'Mayur Dave',
	'author_email': 'm.dave@warwick.ac.uk',
	'license': 'MIT',
	'packages': ['cmath'],
	'install_requires': [
		'markdown',
		'nose'
	],
	'test_suite': 'nose.collector',
	'tests_require': ['nose', 'nose-cover3'],
#	'entry_points': {
#		'console_scripts': ['funniestjoke=funniest.command_line:main'],
#	},
	'include_package_data': True,
	'zip_safe': False
}

setup(**config)
