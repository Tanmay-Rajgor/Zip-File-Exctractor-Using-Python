from zipfile import ZipFile


file_name = "css_notes.zip"

with ZipFile(file_name, 'r') as zip:
    zip.printdir()
    print('Exctracting all the files now...')
    zip.extractall()
    print('Done!')