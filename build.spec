# -*- mode: python ; coding: utf-8 -*-

import os
import platform

root = '.'
hookspath = None
if platform.system() == 'Windows':
  hookspath = [os.path.join(os.curdir, 'hooks')]

ffmpeg_bin = os.path.join(root, 'resources/ffmpeg-bin')
datas = []

if platform.system() == 'Windows':
    arch_bits = int(platform.architecture()[0][:2])
    if arch_bits == 64:
        datas.append((os.path.join(root, 'resources/VCRUNTIME140_1.dll'), '.'))

a = Analysis([os.path.join(os.curdir, 'ffsubsync.py')],
             datas=datas,
             hiddenimports=['pkg_resources.py2_warn'],  # ref: https://github.com/pypa/setuptools/issues/1963
             hookspath=hookspath,
             runtime_hooks=None,
             binaries=[(ffmpeg_bin, 'ffmpeg-bin')],
)

pyz = PYZ(a.pure)

# runtime options to pass to interpreter -- '-u' is for unbuffered io
options = [('u', None, 'OPTION')]

exe = EXE(pyz,
  a.scripts,
  a.binaries,
  a.zipfiles,
  a.datas,
  options,
  name='ffsubsync_bin',
  debug=False,
  strip=False,
  upx=True,
  upx_exclude=[],
  console=True,
)
