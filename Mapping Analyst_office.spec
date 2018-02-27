# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main.py'],
             pathex=['D:\\Python\\Python36-32\\Lib\\site-packages\\PyQt5\\Qt\\bin','D:\\Github\\Mapping-Analyst'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Mapping Analyst',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='D:\\Github\\Mapping-Analyst\\images\\logo.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Mapping Analyst')
