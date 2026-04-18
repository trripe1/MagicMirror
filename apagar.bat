@echo off
taskkill /F /FI "WINDOWTITLE eq MagicMirror" /T >nul 2>&1
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":3000 "') do taskkill /F /PID %%a >nul 2>&1
echo MagicMirror detenido.
timeout /t 2 /nobreak >nul
