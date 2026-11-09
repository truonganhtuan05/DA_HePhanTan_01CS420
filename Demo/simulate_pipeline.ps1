<#
.SYNOPSIS
    Mô phỏng quy trình Distributed CI/CD Pipeline (GitHub Actions & GitLab CI)
.DESCRIPTION
    Kịch bản chạy giả lập 5 stages của Pipeline phân tán:
    Stage 1: Lint & Syntax Check
    Stage 2: Distributed Test Matrix (Parallel Runners)
    Stage 3: Build & Package Artifact
    Stage 4: Staging Deployment & Health Probe
    Stage 5: Quality Gate & Production Release
#>

param(
    [switch]$FailAtTest = $false,
    [string]$Branch = "main"
)

Set-Location $PSScriptRoot
$env:PYTHONPATH = "$PSScriptRoot"

Clear-Host
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "   DAI HOC DUY TAN - KHOA KHOA HOC MAY TINH                                    " -ForegroundColor White
Write-Host "   DO AN HE PHAN TAN (CS420G) - MA DE TAI: 01CS420 (GitHub / GitLab)            " -ForegroundColor Yellow
Write-Host "   MO PHONG QUY TRINH CI/CD PIPELINE PHAN TAN & QUALITY GATE                   " -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "Trigger Event : git push origin $Branch" -ForegroundColor Gray
Write-Host "Commit Hash   : 7d4a9f8b2c1e54a3 (Distributed DAG Node)" -ForegroundColor Gray
Write-Host "Triggered by  : Le Van Hoai Rin / Nguyen Trung Hieu / Truong Anh Tuan" -ForegroundColor Gray
Write-Host "Timestamp     : $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
Write-Host "--------------------------------------------------------------------------------" -ForegroundColor Gray

# -------------------------------------------------------------
# STAGE 1: LINT & SYNTAX
# -------------------------------------------------------------
Write-Host "`n[STAGE 1/5] LINT & SYNTAX VERIFICATION" -ForegroundColor Cyan
Write-Host "[Runner: GitHub-Hosted-Runner-Ubuntu-22.04 | Node-ID: gh-runner-01]" -ForegroundColor DarkGray
Start-Sleep -Milliseconds 600

python -m py_compile src/app.py tests/test_app.py tests/test_fault_scenario.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "[X] STAGE 1 FAILED: Cu phap ma nguon khong hop le!" -ForegroundColor Red
    exit 1
}
Write-Host "[PASS] Cu phap hop le. Khong co loi typing hoac logic can ban." -ForegroundColor Green

# -------------------------------------------------------------
# STAGE 2: DISTRIBUTED TEST MATRIX (PARALLEL RUNNERS)
# -------------------------------------------------------------
Write-Host "`n[STAGE 2/5] DISTRIBUTED TEST MATRIX EXECUTION" -ForegroundColor Cyan
Write-Host "[Strategy: Parallel Matrix across 2 Runner Nodes (Ubuntu & Windows)]" -ForegroundColor DarkGray
Start-Sleep -Milliseconds 700

if ($FailAtTest) {
    $env:SIMULATE_FAIL = "1"
} else {
    $env:SIMULATE_FAIL = "0"
}

Write-Host "  -> Node A (Runner-Ubuntu-Py311) : Running test_app.py..." -ForegroundColor Yellow
python -m unittest tests/test_app.py
$resA = $LASTEXITCODE

Write-Host "  -> Node B (Runner-Win-Py312)    : Running test_fault_scenario.py..." -ForegroundColor Yellow
python -m unittest tests/test_fault_scenario.py
$resB = $LASTEXITCODE

if ($resA -ne 0 -or $resB -ne 0) {
    Write-Host "`n[X] STAGE 2 FAILED: Phat hien bai test bi loi!" -ForegroundColor Red
    Write-Host "[QUALITY GATE TRIGGERED] He thong tu dong NGAT PIPELINE (Fail-Fast)!" -ForegroundColor Red
    Write-Host "[STATUS: BLOCKED] Tu choi Merge vao nhanh '$Branch'. Chup anh nay de minh hoa loi!" -ForegroundColor Red
    Write-Host "================================================================================" -ForegroundColor Red
    exit 1
}
Write-Host "[PASS] Toan bo 6/6 test cases deu thanh cong tren cac Runner phan tan!" -ForegroundColor Green

# -------------------------------------------------------------
# STAGE 3: BUILD & DISTRIBUTED ARTIFACT
# -------------------------------------------------------------
Write-Host "`n[STAGE 3/5] BUILD & PACKAGE DISTRIBUTED ARTIFACT" -ForegroundColor Cyan
Write-Host "[Runner: Docker-Worker-Package-Node]" -ForegroundColor DarkGray
Start-Sleep -Milliseconds 500

$distDir = "dist"
if (-not (Test-Path $distDir)) { New-Item -ItemType Directory -Path $distDir | Out-Null }
$infoFile = "$distDir\pipeline_build_info.json"
@{
    pipeline_id = (Get-Random -Minimum 10000 -Maximum 99999)
    status = "SUCCESS"
    commit = "7d4a9f8b"
    branch = $Branch
    built_at = (Get-Date -Format 'o')
} | ConvertTo-Json | Set-Content -Path $infoFile

Write-Host "[INFO] Package tao tai: $infoFile" -ForegroundColor Gray
Write-Host "[PASS] Artifact da duoc dong goi va upload len Distributed Object Storage." -ForegroundColor Green

# -------------------------------------------------------------
# STAGE 4: STAGING DEPLOYMENT & HEALTH PROBE
# -------------------------------------------------------------
Write-Host "`n[STAGE 4/5] STAGING ENVIRONMENT DEPLOYMENT" -ForegroundColor Cyan
Write-Host "[Target: Staging Cluster (Port 8080)]" -ForegroundColor DarkGray
Start-Sleep -Milliseconds 600
Write-Host "[*] Dong bo phan phoi toi cum Node thu nghiem..." -ForegroundColor Gray
Write-Host "[*] Health Check: Ping http://staging-node.internal/health -> 200 OK (Healthy)" -ForegroundColor Green
Write-Host "[PASS] He thong Staging hoat dong on dinh." -ForegroundColor Green

# -------------------------------------------------------------
# STAGE 5: PRODUCTION DEPLOYMENT & QUALITY GATE
# -------------------------------------------------------------
Write-Host "`n[STAGE 5/5] PRODUCTION RELEASE & QUALITY GATE" -ForegroundColor Cyan
if ($Branch -eq "main") {
    Write-Host "[QUALITY GATE PASSED] Nhanh 'main' duoc bao ve, moi tieu chuan da duoc xac nhan!" -ForegroundColor Green
    Write-Host "[*] Kich hoat Zero-Downtime Deployment toi Production Nodes..." -ForegroundColor Cyan
    Start-Sleep -Milliseconds 500
    Write-Host "[SUCCESS] Phien ban v1.0.0 da duoc phat hanh thanh cong tren Production!" -ForegroundColor Green
} else {
    Write-Host "[SKIP] Branch '$Branch' khong phai 'main'. Bo qua buoc deploy production." -ForegroundColor Yellow
}

Write-Host "`n================================================================================" -ForegroundColor Cyan
Write-Host "   PIPELINE PHAN TAN HOAN TAT: TAT CA CAC GIAI DOAN DEU THANH CONG!           " -ForegroundColor Green
Write-Host "================================================================================" -ForegroundColor Cyan
