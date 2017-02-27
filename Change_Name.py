import os

print os.getcwd()
os.chdir('/Users/TigranTT/Desktop/alphabet copy')
print os.getcwd()
file_name=os.listdir('/Users/TigranTT/Desktop/alphabet copy')
print file_name
for i in file_name:
    print i
    os.rename(i, i.translate(None, 'ma*ic'))
