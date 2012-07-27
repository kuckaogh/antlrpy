from distutils.core import setup
import py2exe
from glob import glob
data_files = [(".", glob(r'C:\PortablePython2.7.3.1\App\msvcr90.dll'))]
setup(data_files=data_files,console=['test2.py'])
#setup(console=['test.py'])
