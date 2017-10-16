@echo off

c:

cd C:\Python27\Scripts
pip install git+http://github.com/AMondelin/ProjectManager.git

start "3DS Max" "C:\Program Files\Autodesk\3ds Max 2016\3dsmax.exe" %*
