################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "JÃ¼rgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: Apache Software License",
	],
	description = "This python module ...",
	download_url = "https://github.com/jkpubsrc/......../tarball/0.2019.10.7",
	include_package_data = False,
	install_requires = [
	],
	keywords = [
		"...",
	],
	license = "Apache 2.0",
	name = "jk_trioinput",
	packages = [
		"jk_trioinput",
	],
	url = "https://github.com/jkpubsrc/........",
	version = "0.2019.10.7",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
