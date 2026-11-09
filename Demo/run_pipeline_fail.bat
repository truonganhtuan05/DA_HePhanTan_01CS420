@echo off
chcp 65001 >nul
echo Đang chạy mô phỏng kịch bản sự cố Quality Gate (FAIL-FAST)...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0simulate_pipeline.ps1" -FailAtTest
pause

