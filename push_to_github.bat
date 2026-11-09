@echo off
chcp 65001 >nul
echo ====================================================================
echo    TỰ ĐỘNG ĐẨY ĐỒ ÁN LÊN GITHUB (MÃ ĐỀ: 01CS420)
echo ====================================================================
echo.

cd /d "%~dp0"

echo [*] Kiểm tra trạng thái Git...
git status >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [*] Đang khởi tạo Git repository cục bộ...
    git init
)

echo.
set /p REPO_URL=">> Nhập đường link Repository GitHub của bạn (URL dạng https://github.com/...): "

if "%REPO_URL%"=="" (
    echo [X] Bạn chưa nhập đường link! Vui lòng chạy lại script.
    pause
    exit /b 1
)

echo.
echo [*] Thêm các tệp tin vào Git...
git add .

echo [*] Tạo commit...
git commit -m "feat: initial commit of distributed CI/CD project and documentation"

echo [*] Đặt tên nhánh chính là main...
git branch -M main

echo [*] Cấu hình remote origin...
git remote remove origin >nul 2>&1
git remote add origin %REPO_URL%

echo.
echo ====================================================================
echo [*] ĐANG ĐẨY CODE LÊN GITHUB (git push -u origin main)...
echo [LƯU Ý] Nếu hiện cửa sổ đăng nhập GitHub, hãy chọn 'Sign in with your browser'.
echo ====================================================================
echo.
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================================================
    echo [SUCCESS] ĐẨY LÊN GITHUB THÀNH CÔNG RỰC RỠ!
    echo Bây giờ bạn hãy mở trình duyệt vào repo và bấm tab 'Actions' để xem
    echo các Runner phân tán tự động chạy pipeline nhé!
    echo ====================================================================
) else (
    echo.
    echo [!] Quá trình push gặp lỗi. Hãy kiểm tra lại đường dẫn repo hoặc tài khoản của bạn.
)

pause

