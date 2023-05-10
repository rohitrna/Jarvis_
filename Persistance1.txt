echo off
set program=C:\Users\RN\Desktop\Python\Jarvis_Online\Jarvis-master\Persistance.bat
set alias_name=%1
set alias_path=%~dp0
set batch_file=%2
set alias=%alias_path%%alias_name%.exe
call :find_args %*
call :make_link %program% %alias%
%alias% /C %batch_file% %args%
:find_args
set args=
shift
shift
:loop
  if [%1] == [] goto :eof
  set args=%args% %1
  shift
  goto :loop
:make_link
  copy %1 %2