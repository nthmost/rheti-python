from setuptools import setup, find_packages

setup (
       name = "rheti",
       version = "0.0.1a",
       description = "Enneagram test based on official RHETI specs",
       url="https://github.com/nthmost/rheti-python",
       author = "Naomi Most",
       author_email = "naomi@nthmost.com",
       maintainer = "Naomi Most",
       maintainer_email = "naomi@nthmost.com",
       license = "MIT",
       zip_safe = False,
       packages = find_packages(),
       entry_points = { 'console_scripts': [
           'rheti = rheti.__main__:main',] }, 
       install_requires = [
                           ],
     )
