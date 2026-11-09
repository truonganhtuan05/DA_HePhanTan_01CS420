# ĐỒ ÁN MÔN HỌC: HỆ PHÂN TÁN (CS420G)
## ĐỀ TÀI: GITHUB & GITLAB TRONG HỆ PHÂN TÁN (MÃ ĐỀ: 01CS420)

**Thành viên thực hiện:**
1. Lê Văn Hoài Rin
2. Nguyễn Trung Hiếu
3. Trương Anh Tuấn

**Giảng viên hướng dẫn:** ThS. Nguyễn Minh Nhật  
**Khoa:** Khoa học Máy tính - Trường Đại học Duy Tân

---

## 1. GIỚI THIỆU BÀI TOÁN DEMO
Hệ thống demo mô phỏng quy trình **CI/CD Pipeline phân tán & Quality Gate** trên GitHub Actions và GitLab CI:
- **Quản lý mã nguồn phân tán:** Mô hình Git DAG, bảo vệ nhánh `main` (Branch Protection).
- **Kiểm thử tự động trên nhiều Runner phân tán:** Ma trận song song (Matrix Parallel) trên các hệ điều hành và môi trường khác nhau.
- **Đóng gói và chia sẻ Artifact:** Đóng gói bản build và lưu trữ trên cụm Distributed Object Storage.
- **Triển khai tự động & Bảo vệ chất lượng (Quality Gate):** Khi có lỗi Unit Test, hệ thống tự động ngắt kết nối (Fail-Fast) và từ chối hòa trộn (Merge) vào nhánh chính.

---

## 2. CẤU TRÚC THƯ MỤC
```
Demo/
├── .github/
│   └── workflows/
│       └── ci-cd-distributed.yml     # Workflow GitHub Actions 5 stages phân tán
├── .gitlab-ci.yml                    # Cấu hình GitLab CI/CD tương đương
├── src/
│   ├── __init__.py
│   └── app.py                        # Service xử lý dữ liệu và REST API
├── tests/
│   ├── __init__.py
│   ├── test_app.py                   # Bộ kiểm thử Unit Test nghiệp vụ
│   └── test_fault_scenario.py        # Kịch bản giả lập lỗi Quality Gate
├── Dockerfile                        # Đóng gói container ứng dụng
├── docker-compose.yml                # Cụm node chạy ứng dụng
├── run_local_tests.ps1               # Script PowerShell chạy kiểm thử nhanh
├── simulate_pipeline.ps1             # Script mô phỏng toàn bộ Pipeline 5 stages
└── README.md                         # Hướng dẫn này
```

---

## 3. CÁCH CHẠY THỰC NGHIỆM VÀ CHỤP ẢNH BÁO CÁO

### Bước 1: Kiểm thử Unit Test cục bộ
Mở PowerShell tại thư mục `Demo`:
```powershell
.\run_local_tests.ps1
```
*(Chụp màn hình kết quả màu xanh: 6/6 tests passed để dán vào Mục 3.2 báo cáo)*

### Bước 2: Chạy toàn bộ Pipeline phân tán (Thành công)
```powershell
.\simulate_pipeline.ps1
```
*(Chụp màn hình đầy đủ 5 Stage màu xanh: Lint -> Test Matrix -> Package -> Staging -> Production để dán vào Mục 3.3 báo cáo)*

### Bước 3: Thử nghiệm tình huống lỗi và cơ chế Quality Gate (Fail-Fast)
```powershell
.\simulate_pipeline.ps1 -FailAtTest
```
*(Chụp màn hình màu đỏ báo lỗi Stage 2, hệ thống tự động khóa merge để dán vào Mục 3.4 báo cáo)*

### Bước 4 (Nếu đẩy lên GitHub / GitLab thực tế):
1. Tạo một repository mới trên [GitHub.com](https://github.com) hoặc [GitLab.com](https://gitlab.com).
2. Push toàn bộ mã nguồn thư mục `Demo` lên repo:
   ```bash
   git init
   git add .
   git commit -m "feat: implement distributed CI/CD pipeline"
   git remote add origin <URL_REPO_CUA_BAN>
   git branch -M main
   git push -u origin main
   ```
3. Vào tab **Actions** (trên GitHub) hoặc **Build -> Pipelines** (trên GitLab) để quan sát các node Runner chạy tự động và chụp ảnh màn hình giao diện web.

