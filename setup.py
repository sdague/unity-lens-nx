#!/usr/bin/env python
#
from distutils.core import setup
from DistUtilsExtra.command import *

setup(name="unity-lens-nx",
      version="0.1",
      author="David Calle",
      author_email="davidc@framli.eu",
      url="http://launchpad.net/onehundredscopes",
      license="GNU General Public License (GPL)",
      data_files=[
    ('share/dbus-1/services', ['unity-lens-nx.service']),
    ('share/unity/lenses/nx', ['nx.lens']),
    ('share/unity/lenses/nx', ['media/lens-nav-nx.svg']),
    ('lib/unity-lens-nx', ['src/unity-lens-nx']),
    ], cmdclass={"build":  build_extra.build_extra, })
