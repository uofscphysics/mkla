from setuptools import setup
import os,glob,warnings,sys,fnmatch,subprocess
from setuptools.command.test import test as TestCommand
from distutils.core import setup
import numpy.distutils.misc_util


if sys.version_info < (3,0):
    sys.exit('Sorry, Python 2 is not supported')

#class SNTDTest(TestCommand):

#    def run_tests(self):
#        import sntd
#        errno = sntd.test()
#        sntd.test_sntd()
#        sys.exit(errno)

AUTHOR = 'Douglas Adams and Justin Pierel'
AUTHOR_EMAIL = 'douglasquincyadams@gmail.com'
VERSION = '0.0.3'
LICENSE = 'BSD'
URL = 'mkla.readthedocs.io'



def recursive_glob(basedir, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(basedir):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

PACKAGENAME='mkla'
# Add the project-global data
#pkgdatadir = os.path.join(PACKAGENAME, 'data')
#microdatadir = os.path.join(PACKAGENAME, 'microlens')
#simdatadir = os.path.join(PACKAGENAME, 'sim')
#batchdatadir = os.path.join(PACKAGENAME, 'batch')
#data_files = []
#data_files.extend(recursive_glob(pkgdatadir, '*'))
#data_files.extend(recursive_glob(microdatadir, '*'))
#data_files.extend(recursive_glob(simdatadir, '*'))
#data_files.extend(recursive_glob(batchdatadir, '*'))

#data_files = [f[len(PACKAGENAME)+1:] for f in data_files]


setup(
    name='mkla',
    #cmdclass={'test': SNTDTest},
    setup_requires=['numpy','cython'],
    install_requires=['numpy','scipy','cython'],
    packages=['mkla'],
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
    #package_data={'sntd':data_files},
    include_package_data=False
)
