# ĐỒ ÁN MÔN HỌC: HỆ PHÂN TÁN (CS420G)
## ĐỀ TÀI: TÌM HIỂU GITHUB, GITLAB VÀ TRIỂN KHAI QUY TRÌNH CI/CD PHÂN TÁN
**Mã đề tài:** `01CS420`  
**Trường:** Đại học Duy Tân - Khoa Khoa học Máy tính  
**Giảng viên hướng dẫn:** ThS. Nguyễn Minh Nhật  

---

### THÀNH VIÊN NHÓM THỰC HIỆN
1. **Lê Văn Hoài Rin** (Trưởng nhóm) - MSSV: 29211434001
2. **Nguyễn Trung Hiếu** - MSSV: 29211434002
3. **Trương Anh Tuấn** - MSSV: 29211434003

---

### KIẾN TRÚC PIPELINE PHÂN TÁN (DISTRIBUTED CI/CD)
```
               [ LẬP TRÌNH VIÊN ]
                       |
               git push origin main
                       |
                       v
         [ GITHUB / GITLAB REPOSITORY ] (DAG Node)
                       |
                Webhook Trigger
                       |
                       v
===================================================================
             DISTRIBUTED CI/CD PIPELINE (5 STAGES)
===================================================================
[Stage 1: Lint & Syntax Check] ----------> Kiểm tra cú pháp mã nguồn
              |
              v (Trigger song song)
[Stage 2: Distributed Matrix Testing] ---> Runner A (Ubuntu / Python 3.11)
                                      ---> Runner B (Windows / Python 3.12)
              |
              v (Khi tất cả tests đạt)
[Stage 3: Package & Artifact Upload] ----> Tạo gói build tar.gz / Object Store
              |
              v
[Stage 4: Staging Deploy & Healthcheck] -> Khởi chạy & Probe HTTP 200 OK
              |
              v
[Stage 5: Quality Gate & Prod Release] --> Kiểm tra điều kiện bảo vệ nhánh main
===================================================================
```

---

### CẤU TRÚC THƯ MỤC DỰ ÁN
- `.github/workflows/ci-cd-distributed.yml`: Kịch bản GitHub Actions tự động kích hoạt Runner phân tán.
- `Bao_Cao/`: Chứa file báo cáo Word (`.docx`), Slide thuyết trình (`.pptx`) và toàn văn nội dung Markdown.
- `Demo/`: Mã nguồn dịch vụ REST API, các bài kiểm thử Unit Test và script tự động.
- `Demo/.gitlab-ci.yml`: Kịch bản GitLab CI/CD tương đương.
- `01CS420_Demo_GitHub_GitLab.zip`: Gói nén demo nộp Google Drive.

