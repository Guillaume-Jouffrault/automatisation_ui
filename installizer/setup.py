from setuptools import setup, find_packages

VERSION = '1.0'
DESCRIPTION = 'Execution automatique d\'installers'

setup(name='installizer',
      version=VERSION,
      author='Guillaume Jouffrault',
      author_email='jouffrault.guillaume@gmail.com',
      description=DESCRIPTION,
      packages=find_packages(),
      zip_safe=False,
      install_requires=[]  # add any additional packages that
      # needs to be installed along with your package. Eg: 'caer'
      )
