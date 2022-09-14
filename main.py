from dataclasses import dataclass, fields
from FFO.item_class import item
from pathlib import Path
import pprint
import os
from glob import glob
import subprocess
pp = pprint.PrettyPrinter(indent=4)

pc = Path(os.environ['USERPROFILE'])

'''
1) Get all folders
'''
@dataclass
class Folders:
    desktop:Path = pc / 'Desktop'
    scripts:Path = desktop / 'Scripts'
    ahk:Path  = scripts / 'AHK'
    utility:Path  = ahk / 'Utility'
    software:Path  = ahk / 'Software'
    python:Path  = scripts / 'Python'
    powershell:Path  = scripts / 'Powershell'

'''
2) Validate that all folders in the Folder class exist
'''
for field in fields(Folders):
    path = getattr(Folders, field.name)
    item.isFolderOrError(path)

'''
3) Get all AHK files that I want on start up
'''
result = [y for x in os.walk(Folders.utility) for y in glob(os.path.join(x[0], '*.ahk'))]
result += [y for x in os.walk(Folders.software) for y in glob(os.path.join(x[0], '*.ahk'))]


'''
4) start all AHK files
'''
for path in result:
    subprocess.run(["powershell", "-Command", f"start-process {path}"])