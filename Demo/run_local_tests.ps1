<#
.SYNOPSIS
    Script chạy kiểm thử tự động cục bộ cho đồ án CS420G (GitHub / GitLab)
.DESCRIPTION
    Thực hiện chạy toàn bộ Unit Test và xuất báo cáo kết quả chi tiết.
#>

param(
    [switch]$SimulateFailure = $false
)

Set-Location $PSScriptRoot
$env:PYTHONPATH = "$PSScriptRoot"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   DO AN HE PHAN TAN (CS420G) - MA DE: 01CS420           " -ForegroundColor Yellow
Write-Host "   KIEM THU TU DONG - UNIT TEST SUITE                    " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

if ($SimulateFailure) {
    Write-Host "[!] Che do kiem thu: MO PHONG SU CO (SIMULATE_FAIL = 1)" -ForegroundColor Red
    $env:SIMULATE_FAIL = "1"
} else {
    Write-Host "[*] Che do kiem thu: BINH THUONG (ALL PASS)" -ForegroundColor Green
    $env:SIMULATE_FAIL = "0"
}

$startTime = Get-Date

Write-Host "`n[*] Dang chay kiem thu qua Python unittest discovery..." -ForegroundColor Gray
python -m unittest discover -s tests -p "test_*.py" -v

$exitCode = $LASTEXITCODE
$endTime = Get-Date
$duration = ($endTime - $startTime).TotalSeconds

Write-Host "`n----------------------------------------------------------" -ForegroundColor Gray
if ($exitCode -eq 0) {
    Write-Host "[STATUS: PASS] Tat ca cac bai kiem thu deu vuot qua! ($([math]::Round($duration, 3))s)" -ForegroundColor Green
    Write-Host "[ACTION] San sang day code len GitHub / GitLab Remote Repository." -ForegroundColor Cyan
} else {
    Write-Host "[STATUS: FAIL] Phat hien loi kiem thu! Exit Code = $exitCode ($([math]::Round($duration, 3))s)" -ForegroundColor Red
    Write-Host "[QUALITY GATE] Pipeline se bi chan! Khong cho phep merge vao nhanh main." -ForegroundColor Yellow
}
Write-Host "==========================================================" -ForegroundColor Cyan

exit $exitCode
