# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


SETUP_DIR = "G:\\pythonproject\\baidupachong\\"
a = Analysis(['G:\\pythonproject\\baidupachong\\\\Main.py', 'G:\\pythonproject\\baidupachong\\config\\Config.py', 'G:\\pythonproject\\baidupachong\\config\\__init__.py', 'G:\\pythonproject\\baidupachong\\Result\\ParseResult.py', 'G:\\pythonproject\\baidupachong\\Result\\ResultException.py', 'G:\\pythonproject\\baidupachong\\Result\\ResultType.py', 'G:\\pythonproject\\baidupachong\\Result\\__init__.py', 'G:\\pythonproject\\baidupachong\\spider\\FormatData.py', 'G:\\pythonproject\\baidupachong\\spider\\GetIp.py', 'G:\\pythonproject\\baidupachong\\spider\\GetTask.py', 'G:\\pythonproject\\baidupachong\\spider\\Request.py', 'G:\\pythonproject\\baidupachong\\spider\\__init__.py', 'G:\\pythonproject\\baidupachong\\test\\TestRequest.py', 'G:\\pythonproject\\baidupachong\\test\\__init__.py', 'G:\\pythonproject\\baidupachong\\utils\\ExcelUtil.py', 'G:\\pythonproject\\baidupachong\\utils\\FileUtil.py', 'G:\\pythonproject\\baidupachong\\utils\\JsonUtil.py', 'G:\\pythonproject\\baidupachong\\utils\\TimeUtil.py', 'G:\\pythonproject\\baidupachong\\utils\\WordUtil.py', 'G:\\pythonproject\\baidupachong\\utils\\__init__.py'],
             pathex=['G:\\pythonproject\\baidupachong'],
             binaries=[],
             datas=[(SETUP_DIR+'config','config')],
             hiddenimports=['spider.GetTask','spider.Request ','spider.FormatData','Result.ParseResult','utils.TimeUtil','utils.FileUtil','spider.GetIp','config.Config'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Main')
