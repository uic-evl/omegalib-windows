REM cd to the directory of this batch file
REM see http://weblogs.asp.net/whaggard/archive/2005/01/28/get-directory-path-of-an-executing-batch-file.aspx for format
REM we need to be in this dir because sclang.exe needs to run scsynth.exe
cd %~dp0
sclang %1
