@echo off
chcp 65001 >nul
echo Đang chạy mô phỏng Pipeline phân tán (ALL PASS)...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0simulate_pipeline.ps1"
pause

