@echo off
chcp 65001 >nul
echo Đang chạy kiểm thử tự động Unit Test...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_local_tests.ps1"
pause

