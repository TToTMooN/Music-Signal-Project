# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['atexit','sip','PyQt4.QtCore','PyQt4.QtGui','os','sys','librosa','librosa.display']
    }
}

executables = [
    Executable('GUIplayer.py', base=base)
]

setup(name='SpectrumCompare',
      version='0.1',
      description='Sample cx_Freeze PyQt4 script',
      options=options,
      executables=executables
      )
