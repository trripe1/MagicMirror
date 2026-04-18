@echo off
cd /d "%~dp0home\magicmirror\MagicMirror"
set MM_PORT=3000
start "MagicMirror" node serveronly
timeout /t 5 /nobreak >nul
start http://localhost:3000
