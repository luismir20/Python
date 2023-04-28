import os
import shutil


source_dir = '/Users/fernando/Desktop/Code/Python'
backup_dir = '/Volumes/Extreme SSD/Code Folder/PythonSSD'

# Looping over files in the source directory
for filename in os.listdir(source_dir):
    source_file = os.path.join(source_dir, filename)
    backup_file = os.path.join(backup_dir, f'{filename}.bak')
    
    if os.path.isfile(source_file):
        shutil.copy(source_file, backup_file)
        print(f'Backup of {source_file} created at {backup_file}')
    else:
        print(f'{source_file} is not a file and will not be backed up.')


for dirname, subdirs, files in os.walk(source_dir):
    backup_subdir = os.path.join(backup_dir, os.path.relpath(dirname, source_dir))
    os.makedirs(backup_subdir, exist_ok=True)
    
    for filename in files:
        source_file = os.path.join(dirname, filename)
        backup_file = os.path.join(backup_subdir, f'{filename}.bak')
        
        shutil.copy(source_file, backup_file)
        print(f'Backup of {source_file} created at {backup_file}')


source_dirO = '/Users/fernando/Desktop/Code/Output'
backup_dirO = '/Volumes/Extreme SSD/Code Folder/OutputsSSD/Python Outputs'

for filename in os.listdir(source_dirO):
    source_fileO = os.path.join(source_dirO, filename)
    backup_fileO = os.path.join(backup_dirO, f'{filename}.bak')
    
    if os.path.isfile(source_fileO):
        shutil.copy(source_fileO, backup_fileO)
        print(f'Backup of {source_fileO} created at {backup_fileO}')
    else:
        print(f'{source_fileO} is not a file and will not be backed up.')

for dirname, subdirs, files in os.walk(source_dirO):
    backup_subdirO = os.path.join(backup_dirO, os.path.relpath(dirname, source_dirO))
    os.makedirs(backup_subdirO, exist_ok=True)
    
    for filename in files:
        source_fileO = os.path.join(dirname, filename)
        backup_fileO = os.path.join(backup_subdirO, f'{filename}.bak')
        
        shutil.copy(source_fileO, backup_fileO)
        print(f'Backup of {source_fileO} created at {backup_fileO}')

source_dirR = '/Users/fernando/Desktop/Code/Resources'
backup_dirR = '/Volumes/Extreme SSD/Code Folder/Resources'

for filename in os.listdir(source_dirR):
    source_fileR = os.path.join(source_dirR, filename)
    backup_fileR = os.path.join(backup_dirR, f'{filename}.bak')
    
    if os.path.isfile(source_fileR):
        shutil.copy(source_fileR, backup_fileR)
        print(f'Backup of {source_fileR} created at {backup_fileR}')
    else:
        print(f'{source_fileR} is not a file and will not be backed up.')

for dirname, subdirs, files in os.walk(source_dirR):
    backup_subdirR = os.path.join(backup_dirR, os.path.relpath(dirname, source_dirR))
    os.makedirs(backup_subdirR, exist_ok=True)
    
    for filename in files:
        source_fileR = os.path.join(dirname, filename)
        backup_fileR = os.path.join(backup_subdirR, f'{filename}.bak')
        
        shutil.copy(source_fileR, backup_fileR)
        print(f'Backup of {source_fileR} created at {backup_fileR}')
