# HƯỚNG DẪN THỰC HIỆN DEMO, CHỤP ẢNH MINH CHỨNG VÀ NỘP BÀI
## ĐỒ ÁN HỆ PHÂN TÁN (CS420G) - MÃ ĐỀ: 01CS420 (GITHUB & GITLAB)

**Thành viên thực hiện:**
- Lê Văn Hoài Rin (Trưởng nhóm)
- Nguyễn Trung Hiếu
- Trương Anh Tuấn  
**GVHD:** ThS. Nguyễn Minh Nhật - Đại học Duy Tân

---

### BƯỚC 1: CHUẨN BỊ MÔI TRƯỜNG & KHẮC PHỤC LỖI EXECUTION POLICY TRÊN POWERSHELL

Windows mặc định chặn chạy file script `.ps1` (báo lỗi `running scripts is disabled on this system`). 
Bạn có thể chọn **1 trong 2 cách cực kỳ đơn giản** sau:

####  CÁCH 1 (Nhanh nhất - Không cần gõ lệnh dài): Click đúp chuột vào file `.bat`
Trong thư mục `Demo`, mình đã tạo sẵn 3 file chạy tự động, bạn chỉ cần mở thư mục và **click đúp chuột** để chạy:
1. `run_tests.bat`: Chạy Unit Test (Màn hình xanh ALL PASS).
2. `run_pipeline_pass.bat`: Chạy toàn bộ 5 Stages Pipeline phân tán thành công.
3. `run_pipeline_fail.bat`: Chạy tình huống lỗi Quality Gate (Màn hình đỏ FAIL-FAST).

---

####  CÁCH 2: Mở quyền trên cửa sổ PowerShell hiện tại
Trên cửa sổ PowerShell bạn đang mở, gõ lệnh sau để mở quyền cho phiên làm việc hiện tại:
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```
*(Nếu hỏi xác nhận, gõ `Y` rồi nhấn `Enter`)*

Sau đó bạn có thể chạy bình thường các file `.ps1`:
```powershell
.\run_local_tests.ps1
.\simulate_pipeline.ps1
.\simulate_pipeline.ps1 -FailAtTest
```

Hoặc thêm tham số `-ExecutionPolicy Bypass` trực tiếp khi gọi file:
```powershell
powershell -ExecutionPolicy Bypass -File .\run_local_tests.ps1
powershell -ExecutionPolicy Bypass -File .\simulate_pipeline.ps1
powershell -ExecutionPolicy Bypass -File .\simulate_pipeline.ps1 -FailAtTest
```

---

### BƯỚC 2: CHỤP CÁC HÌNH ẢNH MINH CHỨNG THỰC TẾ

Bạn chạy 3 lệnh sau trên PowerShell và dùng công cụ **Snipping Tool** (hoặc tổ hợp phím `Windows + Shift + S`) để chụp màn hình dán vào file Word & PowerPoint:

#### 📸 HÌNH 1: Kiểm thử Unit Test cục bộ (Trạng thái màu xanh ALL PASS)
- **Lệnh thực thi:**
  ```powershell
  .\run_local_tests.ps1
  ```
- **Nội dung chụp:** Cửa sổ PowerShell hiển thị `Ran 6 tests in ... -> OK` và dòng chữ màu xanh `[STATUS: PASS] Tat ca cac bai kiem thu deu vuot qua!`.
- **Vị trí dán:**
  - File Word: **Mục 3.2 - Hình 3.1**
  - File Slide PPT: **Slide 18**

#### 📸 HÌNH 2: Thực thi thành công toàn bộ 5 Stages của Pipeline phân tán
- **Lệnh thực thi:**
  ```powershell
  .\simulate_pipeline.ps1
  ```
- **Nội dung chụp:** Cửa sổ PowerShell hiển thị tuần tự cả 5 Stages từ STAGE 1/5 đến STAGE 5/5 đều màu xanh lá cây và dòng kết luận `PIPELINE PHAN TAN HOAN TAT: TAT CA CAC GIAI DOAN DEU THANH CONG!`.
- **Vị trí dán:**
  - File Word: **Mục 3.3 - Hình 3.2**
  - File Slide PPT: **Slide 19**

#### 📸 HÌNH 3: Thử nghiệm tình huống lỗi và cơ chế Quality Gate (Fail-Fast)
- **Lệnh thực thi:**
  ```powershell
  .\simulate_pipeline.ps1 -FailAtTest
  ```
- **Nội dung chụp:** Cửa sổ PowerShell hiển thị bài test bị lỗi tại Stage 2, dòng chữ đỏ `[QUALITY GATE TRIGGERED] He thong tu dong NGAT PIPELINE (Fail-Fast)!` và `[STATUS: BLOCKED] Tu choi Merge vao nhanh 'main'`.
- **Vị trí dán:**
  - File Word: **Mục 3.4 - Hình 3.3**
  - File Slide PPT: **Slide 20**

#### 📸 HÌNH 4: Kiểm tra tệp Metadata và gói phân phối Artifact
- **Lệnh thực thi:**
  ```powershell
  Get-Content .\dist\pipeline_build_info.json
  ```
- **Nội dung chụp:** Hiển thị nội dung tệp JSON metadata gồm pipeline_id, commit, status: SUCCESS.
- **Vị trí dán:**
  - File Word: **Mục 3.5 - Hình 3.4**

---

### BƯỚC 3: NẾU MUỐN CHỤP THÊM GIAO DIỆN WEB TRÊN GITHUB / GITLAB THẬT (TÙY CHỌN - ĐIỂM CỘNG CAO)
Nếu bạn có tài khoản GitHub hoặc GitLab:
1. Tạo 1 repository mới trên GitHub (ví dụ: `CS420G-Distributed-Demo`).
2. Mở Git Bash hoặc PowerShell đẩy code lên:
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit of distributed CI/CD pipeline"
   git remote add origin https://github.com/<tai-khoan-cua-ban>/CS420G-Distributed-Demo.git
   git branch -M main
   git push -u origin main
   ```  
3. Vào tab **Actions** trên GitHub, bạn sẽ thấy Workflow **CS420G Distributed CI/CD Pipeline** tự động chạy với các icon màu xanh tích cực đẹp mắt. Chụp ảnh màn hình này dán bổ sung vào bài báo cáo!

---

### BƯỚC 4: HƯỚNG DẪN ĐÓNG GÓI VÀ NỘP BÀI

Theo yêu cầu của thầy cô (ghi rõ trong hình ảnh yêu cầu):
1. **Nộp Báo cáo Lý thuyết vào Assignments (LMS của trường):**
   - Nộp file: `Bao_Cao_Do_An_01CS420_GitHub_GitLab.docx`
   - Hoặc có thể xuất ra thêm bản PDF (`Bao_Cao_Do_An_01CS420_GitHub_GitLab.pdf`) để định dạng không bị xô lệch khi thầy cô mở trên máy khác.
2. **Nộp Slide báo cáo tại lớp:**
   - Sử dụng file: `Slide_Bao_Cao_01CS420_GitHub_GitLab.pptx` (gồm 26 slide chuẩn mực, đầy đủ nội dung từ Mở đầu $\rightarrow$ Lý thuyết $\rightarrow$ Demo $\rightarrow$ Thực nghiệm $\rightarrow$ Kết luận $\rightarrow$ Q&A).
3. **Nộp Demo vào Google Drive:**
   - Nén thư mục `Demo` thành tệp `01CS420_Demo_GitHub_GitLab.zip`.
   - Tải lên Google Drive cá nhân, bật quyền chia sẻ link: *"Bất kỳ ai có đường liên kết đều có thể xem"*.
   - Dán link Google Drive vào phần nộp bài theo yêu cầu của giảng viên.

