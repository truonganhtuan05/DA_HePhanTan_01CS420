# ĐẠI HỌC DUY TÂN - TRƯỜNG KHOA HỌC MÁY TÍNH
## BÁO CÁO ĐỒ ÁN NHÓM - MÔN HỌC: HỆ PHÂN TÁN (CS420G)

---

### ĐỀ TÀI: TÌM HIỂU GITHUB, GITLAB VÀ TRIỂN KHAI QUY TRÌNH TÍCH HỢP LIÊN TỤC (CI/CD) PHÂN TÁN
**Mã đề tài:** 01CS420  
**Giảng viên hướng dẫn:** ThS. Nguyễn Minh Nhật  
**Lớp môn học:** CS420G  

**Danh sách sinh viên thực hiện:**
1. **Lê Văn Hoài Rin** (Trưởng nhóm)
2. **Nguyễn Trung Hiếu**
3. **Trương Anh Tuấn**

*Đà Nẵng, 11/2026*

---

## MỤC LỤC

- [MỞ ĐẦU](#mở-đầu)
  - [1. Lý do chọn đề tài](#1-lý-do-chọn-đề-tài)
  - [2. Mục tiêu của đề tài](#2-mục-tiêu-của-đề-tài)
  - [3. Phạm vi nghiên cứu đề tài](#3-phạm-vi-nghiên-cứu-đề-tài)
  - [4. Bố cục báo cáo](#4-bố-cục-báo-cáo)
- [CHƯƠNG 1: GIỚI THIỆU VÀ TỔNG QUAN VỀ LÝ THUYẾT LIÊN QUAN](#chương-1-giới-thiệu-và-tổng-quan-về-lý-thuyết-liên-quan)
  - [1.1. Tổng quan về Hệ thống quản lý phiên bản phân tán (DVCS)](#11-tổng-quan-về-hệ-thống-quản-lý-phiên-bản-phân-tán-dvcs)
    - [1.1.1. Khái niệm DVCS, Git, GitHub và GitLab](#111-khái-niệm-dvcs-git-github-và-gitlab)
    - [1.1.2. Git trong bài toán Hệ phân tán](#112-git-trong-bài-toán-hệ-phân-tán)
    - [1.1.3. So sánh Hệ thống tập trung (CVCS) và Hệ thống phân tán (DVCS)](#113-so-sánh-hệ-thống-tập-trung-cvcs-và-hệ-thống-phân-tán-dvcs)
    - [1.1.4. So sánh nền tảng GitHub và GitLab](#114-so-sánh-nền-tảng-github-và-gitlab)
  - [1.2. Kiến trúc và các thành phần của GitHub và GitLab](#12-kiến-trúc-và-các-thành-phần-của-github-và-gitlab)
    - [1.2.1. Kiến trúc phân tán của GitHub](#121-kiến-trúc-phân-tán-của-github)
    - [1.2.2. Kiến trúc phân tán của GitLab](#122-kiến-trúc-phân-tán-của-gitlab)
  - [1.3. Nguyên lý hoạt động trong môi trường phân tán](#13-nguyên-lý-hoạt-động-trong-môi-trường-phân-tán)
    - [1.3.1. Mô hình cấu trúc đồ thị DAG (Directed Acyclic Graph)](#131-mô-hình-cấu-trúc-đồ-thị-dag-directed-acyclic-graph)
    - [1.3.2. Cơ chế đồng bộ, rẽ nhánh và giải quyết xung đột (Conflict Resolution)](#132-cơ-chế-đồng-bộ-rẽ-nhánh-và-giải-quyết-xung-đột-conflict-resolution)
    - [1.3.3. Cơ chế kích hoạt sự kiện và điều phối tác vụ phân tán (Webhooks & CI/CD Runners)](#133-cơ-chế-kích-hoạt-sự-kiện-và-điều-phối-tác-vụ-phân-tán-webhooks--cicd-runners)
  - [1.4. Ưu điểm và hạn chế của GitHub và GitLab](#14-ưu-điểm-và-hạn-chế-của-github-và-gitlab)
  - [1.5. Các lĩnh vực áp dụng](#15-các-lĩnh-vực-áp-dụng)
- [CHƯƠNG 2: TRÌNH BÀY NỘI DUNG CHÍNH CỦA ĐỀ TÀI](#chương-2-trình-bày-nội-dung-chính-của-đề-tài)
  - [2.1. Bài toán và yêu cầu ứng dụng demo](#21-bài-toán-và-yêu-cầu-ứng-dụng-demo)
    - [2.1.1. Mô tả bài toán thực tế](#211-mô-tả-bài-toán-thực-tế)
    - [2.1.2. Yêu cầu đầu vào và đầu ra (Input / Output)](#212-yêu-cầu-đầu-vào-và-đầu-ra-input--output)
    - [2.1.3. Yêu cầu triển khai phân tán](#213-yêu-cầu-triển-khai-phân-tán)
  - [2.2. Kiến trúc và cơ chế hoạt động của hệ thống demo](#22-kiến-trúc-và-cơ-chế-hoạt-động-của-hệ-thống-demo)
    - [2.2.1. Sơ đồ kiến trúc Pipeline phân tán](#221-sơ-đồ-kiến-trúc-pipeline-phân-tán)
    - [2.2.2. Luồng xử lý công việc qua các Runner phân tán](#222-luồng-xử-lý-công-việc-qua-các-runner-phân-tán)
  - [2.3. Thiết kế mã nguồn và bộ kiểm thử tự động](#23-thiết-kế-mã-nguồn-và-bộ-kiểm-thử-tự-động)
    - [2.3.1. Cấu trúc thư mục dự án](#231-cấu-trúc-thư-mục-dự-án)
    - [2.3.2. Thiết kế dịch vụ nghiệp vụ (app.py)](#232-thiết-kế-dịch-vụ-nghiệp-vụ-apppy)
    - [2.3.3. Thiết kế các kịch bản kiểm thử (Unit Tests)](#233-thiết-kế-các-kịch-bản-kiểm-thử-unit-tests)
  - [2.4. Đóng gói và cấu hình Pipeline trên GitHub Actions & GitLab CI](#24-đóng-gói-và-cấu-hình-pipeline-trên-github-actions--gitlab-ci)
    - [2.4.1. Cấu hình GitHub Actions Workflow](#241-cấu-hình-github-actions-workflow)
    - [2.4.2. Cấu hình GitLab CI/CD Pipeline](#242-cấu-hình-gitlab-cicd-pipeline)
    - [2.4.3. Cơ chế Quality Gate và bảo vệ nhánh chính](#243-cơ-chế-quality-gate-và-bảo-vệ-nhánh-chính)
- [CHƯƠNG 3: TRIỂN KHAI THỬ NGHIỆM VÀ KHẮC PHỤC SỰ CỐ](#chương-3-triển-khai-thử-nghiệm-và-khắc-phục-sự-cố)
  - [3.1. Môi trường triển khai thực nghiệm](#31-môi-trường-triển-khai-thực-nghiệm)
  - [3.2. Kết quả kiểm thử Unit Test cục bộ](#32-kết-quả-kiểm-thử-unit-test-cục-bộ)
  - [3.3. Kết quả thực thi Pipeline 5 Stages thành công](#33-kết-quả-thực-thi-pipeline-5-stages-thành-công)
  - [3.4. Thử nghiệm tình huống lỗi và cơ chế Quality Gate](#34-thử-nghiệm-tình-huống-lỗi-và-cơ-chế-quality-gate)
  - [3.5. Kết quả đóng gói và phân phối Artifact](#35-kết-quả-đóng-gói-và-phân-phối-artifact)
  - [3.6. Bảng tổng hợp các phép thử và đánh giá](#36-bảng-tổng-hợp-các-phép-thử-và-đánh-giá)
- [KẾT LUẬN](#kết-luận)
  - [1. Tổng kết kết quả đạt được](#1-tổng-kết-kết-quả-đạt-được)
  - [2. Bài học kinh nghiệm](#2-bài-học-kinh-nghiệm)
  - [3. Hướng phát triển trong tương lai](#3-hướng-phát-triển-trong-tương-lai)
- [TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)

---

## MỞ ĐẦU

### 1. Lý do chọn đề tài
Trong quá trình phát triển phần mềm hiện đại, việc phối hợp làm việc giữa nhiều lập trình viên trên các địa điểm địa lý khác nhau đặt ra thách thức lớn về tính nhất quán của mã nguồn, kiểm soát phiên bản và tốc độ phát hành ứng dụng. Trước đây, các hệ thống quản lý phiên bản tập trung (như SVN, CVS) phụ thuộc hoàn toàn vào một máy chủ duy nhất. Nếu máy chủ này gặp sự cố hoặc mất kết nối mạng, toàn bộ chu trình phát triển của nhóm sẽ bị tê liệt.

Sự ra đời của Hệ thống quản lý phiên bản phân tán (Distributed Version Control System - DVCS), tiêu biểu là Git, cùng với các nền tảng cộng tác phân tán hàng đầu như **GitHub** và **GitLab**, đã giải quyết triệt để bài toán này. Trong môn học **Hệ phân tán (CS420G)**, việc tìm hiểu cách GitHub và GitLab vận hành giúp sinh viên hiểu sâu sắc về:
- Cấu trúc dữ liệu phân tán (Directed Acyclic Graph - DAG).
- Cơ chế đồng bộ dữ liệu phi tập trung (Decentralized Synchronization).
- Khả năng xử lý phân tán các tác vụ tự động hóa xây dựng, kiểm thử và triển khai ứng dụng thông qua kiến trúc **CI/CD Runners** phân tán.

Chính vì vậy, nhóm lựa chọn đề tài **"Tìm hiểu GitHub, GitLab và triển khai quy trình tích hợp liên tục (CI/CD) phân tán"** nhằm kết hợp chặt chẽ giữa lý thuyết hệ phân tán và kỹ năng thực hành kỹ thuật phần mềm tiên tiến.

### 2. Mục tiêu của đề tài
1. **Về lý thuyết:**
   - Hệ thống hóa toàn diện kiến trúc, các thành phần nội tại và nguyên lý vận hành phân tán của GitHub và GitLab.
   - Phân tích cơ chế đồng bộ, rẽ nhánh (branching), hòa trộn (merging) và giải quyết xung đột (conflict resolution) theo mô hình dữ liệu đồ thị DAG.
   - So sánh chuyên sâu giữa GitHub và GitLab, phân tích ưu nhược điểm và phạm vi ứng dụng trong doanh nghiệp.
2. **Về thực nghiệm:**
   - Thiết kế và triển khai một quy trình tích hợp liên tục (CI/CD Pipeline) phân tán bao gồm 5 giai đoạn: Linting $\rightarrow$ Parallel Testing Matrix $\rightarrow$ Packaging & Artifact Distribution $\rightarrow$ Staging Deployment $\rightarrow$ Quality Gate & Production Release.
   - Xây dựng kịch bản kiểm thử giả lập lỗi (Fault Injection) để chứng minh cơ chế tự động bảo vệ hệ thống (Fail-Fast và Quality Gate) của nền tảng CI/CD phân tán.

### 3. Phạm vi nghiên cứu đề tài
- **Phạm vi lý thuyết:** Nghiên cứu mô hình DVCS, kiến trúc máy chủ GitLab CE (Gitaly, Sidekiq, Puma) và kiến trúc GitHub Actions Runners (Hosted và Self-Hosted).
- **Phạm vi thực nghiệm:** Xây dựng dịch vụ phân tán bằng Python, thiết lập tệp cấu hình quy trình làm việc chuẩn cho cả GitHub Actions (`.github/workflows/ci-cd-distributed.yml`) và GitLab CI (`.gitlab-ci.yml`), kèm theo các script PowerShell kiểm thử và mô phỏng pipeline tự động.

### 4. Bố cục báo cáo
Báo cáo gồm ba chương chính:
- **Chương 1:** Giới thiệu và tổng quan về lý thuyết liên quan (Kiến trúc, nguyên lý, ưu/nhược điểm, ứng dụng).
- **Chương 2:** Trình bày nội dung chính của đề tài (Mô tả bài toán demo, kiến trúc hệ thống, thiết kế mã nguồn và cấu hình pipeline).
- **Chương 3:** Triển khai thử nghiệm và đánh giá kết quả (Môi trường, các phép thử thực nghiệm, phân tích lỗi, bảng đánh giá).
- **Kết luận:** Tổng kết kết quả, bài học kinh nghiệm và định hướng phát triển.

---

## CHƯƠNG 1: GIỚI THIỆU VÀ TỔNG QUAN VỀ LÝ THUYẾT LIÊN QUAN

### 1.1. Tổng quan về Hệ thống quản lý phiên bản phân tán (DVCS)

#### 1.1.1. Khái niệm DVCS, Git, GitHub và GitLab
- **DVCS (Distributed Version Control System):** Là hệ thống quản lý mã nguồn trong đó mỗi máy khách (Client node) không chỉ tải về bản sao lưu mới nhất của tệp tin mà sao chép toàn bộ kho lưu trữ (Repository), bao gồm toàn bộ lịch sử commit. Mỗi nút mạng đều đóng vai trò như một kho chứa hoàn chỉnh và độc lập.
- **Git:** Là phần mềm DVCS mã nguồn mở được Linus Torvalds sáng lập năm 2005, hoạt động dựa trên cơ chế chụp ảnh trạng thái (Snapshot) thay vì lưu trữ sự sai khác giữa các phiên bản (Delta differences).
- **GitHub:** Là nền tảng lưu trữ và cộng tác mã nguồn trên nền tảng đám mây lớn nhất thế giới, cung cấp các tính năng quản lý mã nguồn Git, theo dõi lỗi (Issue Tracking), tính năng thảo luận Pull Request và nền tảng tính toán phân tán **GitHub Actions**.
- **GitLab:** Là một nền tảng DevOps hoàn chỉnh theo mô hình "All-in-One", cho phép tổ chức tự cài đặt trên máy chủ riêng (Self-hosted GitLab Community Edition - CE) hoặc sử dụng dịch vụ đám mây (GitLab.com), nổi bật với công cụ **GitLab CI/CD** mạnh mẽ.

#### 1.1.2. Git trong bài toán Hệ phân tán
Trong hệ phân tán, vấn đề đồng thuận và tính nhất quán của dữ liệu (Consistency) là bài toán cốt lõi. Git giải quyết bài toán này mà không cần sử dụng các thuật toán đồng thuận phức tạp như Paxos hay Raft trong thời gian thực. Thay vào đó, Git áp dụng mô hình **Tính nhất quán cuối cùng (Eventual Consistency)**:
- Mỗi thành viên làm việc độc lập trên kho lưu trữ cục bộ (Local Repository).
- Dữ liệu được đồng bộ khi có hành động tường minh: `git fetch`, `git pull`, `git push`.
- Nếu có hai nút cùng thay đổi dữ liệu tại một vị trí, Git sẽ phát hiện xung đột (Conflict) và yêu cầu người dùng giải quyết trước khi hoàn tất việc hòa trộn (Merge Commit).

#### 1.1.3. So sánh Hệ thống tập trung (CVCS) và Hệ thống phân tán (DVCS)

| Tiêu chí | Hệ thống tập trung (CVCS - SVN/CVS) | Hệ thống phân tán (DVCS - Git/GitHub/GitLab) |
| :--- | :--- | :--- |
| **Bản sao kho lưu trữ** | Chỉ có 1 bản duy nhất trên máy chủ trung tâm. | Mỗi nút máy khách sở hữu một kho lưu trữ đầy đủ. |
| **Phụ thuộc mạng** | Bắt buộc phải có mạng để commit, xem lịch sử, tạo nhánh. | Có thể commit, xem lịch sử, tạo nhánh offline hoàn toàn. |
| **Điểm lỗi đơn (SPOF)** | Máy chủ chết $\rightarrow$ Toàn bộ nhóm tê liệt, nguy cơ mất dữ liệu. | Máy chủ chết $\rightarrow$ Bất kỳ bản sao nào của máy khách cũng có thể khôi phục lại kho chứa. |
| **Tốc độ thực thi** | Chậm (phụ thuộc vào băng thông và độ trễ mạng). | Cực nhanh (các thao tác lịch sử, commit diễn ra trực tiếp trên ổ đĩa cục bộ). |
| **Mô hình bảo mật** | Dễ phân quyền chi tiết theo từng thư mục. | Bảo mật theo mức kho lưu trữ (Repository-level). |

#### 1.1.4. So sánh nền tảng GitHub và GitLab

| Đặc điểm | GitHub | GitLab |
| :--- | :--- | :--- |
| **Mô hình cung cấp** | Chủ yếu là SaaS Đám mây (có GitHub Enterprise Server). | Hỗ trợ mạnh mẽ cả Cloud SaaS và Self-Hosted (GitLab CE/EE). |
| **CI/CD Engine** | GitHub Actions (Workflow định nghĩa bằng YAML). | GitLab CI/CD (Cấu hình qua file `.gitlab-ci.yml`). |
| **Điều phối Runner** | GitHub-hosted runners hoặc Self-hosted runners. | GitLab Runner (hỗ trợ Docker, Kubernetes, Shell, VirtualBox). |
| **Cộng đồng** | Cộng đồng mã nguồn mở lớn nhất toàn cầu. | Rất phổ biến trong môi trường nội bộ doanh nghiệp yêu cầu bảo mật dữ liệu tuyệt đối. |

---

### 1.2. Kiến trúc và các thành phần của GitHub và GitLab

#### 1.2.1. Kiến trúc phân tán của GitHub
GitHub không chỉ là một máy chủ Git đơn lẻ mà là một hệ thống phân tán quy mô siêu lớn (Hyper-scale Distributed System):
1. **Lớp định tuyến (Routing & Edge):** Tiếp nhận các kết nối HTTPS và SSH từ lập trình viên, cân bằng tải tới các dịch vụ nội bộ.
2. **Spokes / Gitaly Storage Cluster:** Cụm máy chủ lưu trữ Git phân tán. GitHub sử dụng cơ chế nhân bản (Replication) đa điểm để đảm bảo dữ liệu kho chứa không bị mất mát khi một ổ đĩa hoặc node phần cứng gặp sự cố.
3. **Database Cluster (MySQL/Vitess):** Lưu trữ metadata (Issues, Pull Requests, Comments, User profiles).
4. **Cache & Event Bus (Redis, Kafka):** Phân tán thông điệp sự kiện (Event-driven Architecture). Mỗi khi có commit, sự kiện được phát đi để kích hoạt Webhook và GitHub Actions.
5. **GitHub Actions Compute Engine:** Cụm máy ảo phân tán tiếp nhận các job trong workflow, thực thi trên các Runner độc lập và trả kết quả về giao diện người dùng.

#### 1.2.2. Kiến trúc phân tán của GitLab
GitLab được thiết kế theo kiến trúc module hóa với các thành phần phân tán rõ rệt:
1. **GitLab Workhorse:** Reverse Proxy viết bằng Go, xử lý các luồng dữ liệu Git HTTP nặng mà không làm tắc nghẽn máy chủ ứng dụng chính.
2. **GitLab Rails (Puma):** Xử lý toàn bộ logic giao diện, nghiệp vụ và API của hệ thống.
3. **Gitaly & Gitaly Cluster (Praefect):** Dịch vụ RPC phân tán chuyên trách việc đọc/ghi các thao tác Git trên đĩa, hỗ trợ nhân bản đồng bộ (HA - High Availability).
4. **PostgreSQL & Redis:** PostgreSQL lưu trữ dữ liệu có cấu trúc; Redis lưu cache phiên làm việc và hàng đợi tác vụ nền.
5. **Sidekiq:** Xử lý các tác vụ nền bất đồng bộ (gửi email, tính toán dung lượng repo, trigger CI/CD).
6. **GitLab Runner:** Các tiến trình độc lập, có thể phân tán trên hàng trăm máy chủ vật lý, cụm Docker hoặc Kubernetes để nhận và xử lý các tác vụ xây dựng/kiểm thử.

---

### 1.3. Nguyên lý hoạt động trong môi trường phân tán

#### 1.3.1. Mô hình cấu trúc đồ thị DAG (Directed Acyclic Graph)
Cốt lõi của Git là cơ chế lưu trữ hướng đối tượng dạng đồ thị có hướng không chu trình:
- **Blob Object:** Lưu trữ nội dung nhị phân thuần túy của tệp tin.
- **Tree Object:** Đại diện cho thư mục, ánh xạ tên tệp tin tới mã hash của Blob hoặc Tree con.
- **Commit Object:** Trỏ tới một Tree đại diện cho trạng thái toàn bộ thư mục tại thời điểm đó, kèm theo thông tin tác giả, thời gian và mã băm SHA trỏ về commit cha (Parent Commit).
- **Cơ chế Hash Cryptographic (SHA-1 / SHA-256):** Mỗi node trong đồ thị được định danh duy nhất bởi mã băm. Do tính chất của hàm băm, dữ liệu không thể bị thay đổi âm thầm; bất kỳ chỉnh sửa nào trong quá khứ sẽ làm thay đổi mã băm của toàn bộ các commit tiếp theo.

#### 1.3.2. Cơ chế đồng bộ, rẽ nhánh và giải quyết xung đột (Conflict Resolution)
- **Branching (Rẽ nhánh):** Trong Git, một nhánh chỉ là một con trỏ có thể di chuyển (Movable Pointer) trỏ tới một nút commit trong đồ thị DAG. Việc tạo nhánh có chi phí tài nguyên $O(1)$.
- **Three-way Merge (Hòa trộn ba điểm):** Khi hòa trộn hai nhánh (ví dụ: `feature` vào `main`), Git xác định commit gốc chung gần nhất (Common Ancestor), sau đó so sánh sự thay đổi ở cả hai nhánh so với điểm gốc.
- **Xung đột phân tán (Conflict):** Nếu cả hai lập trình viên cùng thay đổi cùng một dòng trên cùng một tệp từ điểm gốc chung, thuật toán hòa trộn tự động sẽ dừng lại và đánh dấu trạng thái Conflict. Quá trình này đòi hỏi con người hoặc chính sách quy định (Policy) để xác định phiên bản cuối cùng được chấp nhận.

#### 1.3.3. Cơ chế kích hoạt sự kiện và điều phối tác vụ phân tán (Webhooks & CI/CD Runners)
1. **Webhook:** Là cơ chế thông báo dựa trên sự kiện (Event-driven). Khi có một hành động diễn ra (ví dụ: `push`, `pull_request_opened`), máy chủ Git sẽ gửi một bản tin HTTP POST chứa payload JSON tới các dịch vụ được đăng ký trước.
2. **Cơ chế Điều phối Runner (Job Scheduling):**
   - Bộ điều phối (Scheduler) đưa các công việc cần làm vào hàng đợi (Queue).
   - Các Runner phân tán (được cài đặt trên nhiều hệ điều hành và môi trường khác nhau) liên tục gửi tín hiệu thăm dò (Polling) hoặc lắng nghe sự kiện để nhận job phù hợp.
   - Các job trong cùng một stage có thể chạy hoàn toàn **song song** (Parallel Execution), giúp rút ngắn thời gian phản hồi kiểm thử từ hàng chục phút xuống còn vài phút.

---

### 1.4. Ưu điểm và hạn chế của GitHub và GitLab

#### 1.4.1. Ưu điểm
1. **Loại bỏ điểm lỗi đơn trong phát triển:** Mỗi lập trình viên có đầy đủ lịch sử mã nguồn, cho phép làm việc ngoại tuyến và dễ dàng phục hồi dữ liệu khi có thảm họa.
2. **Tự động hóa toàn diện quy trình:** CI/CD phân tán cho phép tự động kiểm tra cú pháp, chạy unit test, kiểm tra bảo mật (SAST/DAST) và tự động triển khai.
3. **Bảo vệ mã nguồn thông qua Quality Gate:** Cơ chế Branch Protection ngăn chặn việc đưa mã nguồn có lỗi hoặc chưa được kiểm thử vào nhánh chính (`main`).
4. **Khả năng mở rộng (Scalability):** Hệ thống Runner có thể mở rộng quy mô linh hoạt (Auto-scaling) từ một vài máy tính cục bộ lên hàng ngàn node tính toán trên đám mây.

#### 1.4.2. Hạn chế
1. **Quản lý tệp nhị phân lớn (Binary Large Objects):** Git không được tối ưu để lưu trữ các tệp dung lượng lớn (video, mô hình máy học, file database). Cần sử dụng các giải pháp mở rộng như Git LFS (Large File Storage).
2. **Độ phức tạp trong việc giải quyết xung đột:** Trong các dự án lớn với hàng trăm lập trình viên, tình trạng xung đột mã nguồn khi hòa trộn diễn ra thường xuyên, đòi hỏi quy trình phân nhánh (GitFlow / Trunk-based) nghiêm ngặt.
3. **Chi phí tài nguyên và vận hành (đối với Self-hosted GitLab):** GitLab CE tiêu tốn nhiều RAM và CPU để vận hành ổn định cụm dịch vụ (Gitaly, Puma, PostgreSQL, Redis, Sidekiq).

---

### 1.5. Các lĩnh vực áp dụng
- **Phát triển phần mềm doanh nghiệp & Ngân hàng:** Quản lý quy trình phát hành an toàn, tích hợp kiểm thử bảo mật tự động.
- **Văn hóa DevOps & GitOps:** Quản lý toàn bộ hạ tầng (Infrastructure as Code - IaC) bằng mã nguồn Git (Terraform, Kubernetes manifest), đồng bộ hạ tầng tự động qua Git commit.
- **Hệ sinh thái Mã nguồn mở toàn cầu:** Hàng triệu dự án phần mềm mã nguồn mở được phát triển, đánh giá và chia sẻ qua nền tảng GitHub/GitLab.

---

## CHƯƠNG 2: TRÌNH BÀY NỘI DUNG CHÍNH CỦA ĐỀ TÀI

### 2.1. Bài toán và yêu cầu ứng dụng demo

#### 2.1.1. Mô tả bài toán thực tế
Để minh họa rõ nét các đặc tính của GitHub và GitLab trong hệ phân tán, nhóm xây dựng một bài toán thực tế:
Một hệ thống tính toán thống kê và hòa trộn dữ liệu phân tán (Distributed Task & Calculation Service) phục vụ nhiều nút mạng. Mã nguồn hệ thống được quản lý trên kho lưu trữ Git và áp dụng chu trình **Tích hợp liên tục phân tán (Distributed CI/CD)**.

Mỗi khi lập trình viên cập nhật mã nguồn hoặc gửi đề xuất hòa trộn (Pull Request / Merge Request), hệ thống phải tự động điều phối các Runner phân tán thực hiện quy trình kiểm tra chất lượng đa tầng trước khi cho phép đóng gói và phát hành.

#### 2.1.2. Yêu cầu đầu vào và đầu ra (Input / Output)
- **Đầu vào (Input):**
  - Commit mã nguồn mới hoặc yêu cầu tạo Pull Request từ nhánh phát triển (`feature/*`) vào nhánh chính (`main`).
  - Bộ dữ liệu kiểm thử giả lập tính toán phân tán (danh sách số liệu, cấu trúc dữ liệu hòa trộn).
- **Đầu ra (Output):**
  - Báo cáo kết quả kiểm thử tự động từ các Runner phân tán (Pass/Fail).
  - Gói phân phối ứng dụng (Distributed Build Artifact) được nén và lưu trữ an toàn.
  - Ứng dụng được triển khai tự động lên môi trường thử nghiệm (Staging) và kiểm tra sức khỏe thành công (Health Check: HTTP 200 OK).
  - Trạng thái cấp phép hoặc khóa nhánh (Merge Allowed / Blocked) của Quality Gate.

#### 2.1.3. Yêu cầu triển khai phân tán
- Thiết lập tệp pipeline tương thích cho cả hai nền tảng: GitHub Actions (`ci-cd-distributed.yml`) và GitLab CI (`.gitlab-ci.yml`).
- Cơ chế kiểm thử đa nền tảng (Matrix Execution) phân bổ công việc đồng thời trên nhiều hệ điều hành (Ubuntu, Windows) và các phiên bản môi trường thực thi khác nhau.
- Cơ chế xử lý sự cố (Fault-Tolerance & Fail-Fast): Khi phát hiện lỗi ở bất kỳ khâu kiểm thử nào, toàn bộ pipeline phải dừng ngay lập tức, ngăn ngừa lỗi lây lan sang các môi trường triển khai tiếp theo.

---

### 2.2. Kiến trúc và cơ chế hoạt động của hệ thống demo

#### 2.2.1. Sơ đồ kiến trúc Pipeline phân tán

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

#### 2.2.2. Luồng xử lý công việc qua các Runner phân tán
1. **Lập trình viên commit code:** Git tạo commit mới, cập nhật con trỏ nhánh cục bộ và đẩy lên remote repo.
2. **Remote Repo phát hiện sự kiện:** Kích hoạt Webhook nội bộ khởi động Pipeline.
3. **Stage 1 (Linting):** Runner nhận việc, kéo mã nguồn (Git Checkout), biên dịch tĩnh kiểm tra lỗi cú pháp.
4. **Stage 2 (Matrix Testing):** Bộ điều phối chia việc cho 2 Runner độc lập chạy song song: một Runner chạy bộ test nghiệp vụ, một Runner chạy bộ test giả lập xử lý ngoại lệ và hòa trộn dữ liệu.
5. **Stage 3 (Artifact Packaging):** Sau khi các bài test đều vượt qua, Runner tạo bản nén ứng dụng và đưa lên hệ thống lưu trữ phân tán (Artifacts Repository).
6. **Stage 4 & 5 (Staging & Production):** Tự động bung gói release lên môi trường kiểm thử, gọi API kiểm tra trạng thái dịch vụ và phát hành sản phẩm.

---

### 2.3. Thiết kế mã nguồn và bộ kiểm thử tự động

#### 2.3.1. Cấu trúc thư mục dự án
Toàn bộ dự án được cấu trúc theo chuẩn công nghiệp:
- `Demo/.github/workflows/ci-cd-distributed.yml`: Kịch bản GitHub Actions.
- `Demo/.gitlab-ci.yml`: Kịch bản GitLab CI/CD.
- `Demo/src/app.py`: Dịch vụ tính toán phân tán và REST API.
- `Demo/tests/test_app.py`: Bộ kiểm thử chức năng tự động.
- `Demo/tests/test_fault_scenario.py`: Bộ kiểm thử kịch bản lỗi giả lập.
- `Demo/run_local_tests.ps1`: Script PowerShell chạy kiểm thử nhanh.
- `Demo/simulate_pipeline.ps1`: Script PowerShell mô phỏng toàn bộ quy trình CI/CD.

#### 2.3.2. Thiết kế dịch vụ nghiệp vụ (app.py)
Dịch vụ được xây dựng bằng Python với các chức năng phân tán:
- `calculate_stats(numbers)`: Xử lý tập dữ liệu phân tán, tính toán tổng, trung bình, giá trị cực tiểu và cực đại.
- `merge_distributed_data(node_a_data, node_b_data)`: Mô phỏng cơ chế hòa trộn dữ liệu phân tán 3 chiều (Three-way merge), tự động phát hiện xung đột khi hai node cùng ghi đè một trường dữ liệu.
- `SimpleAPIHandler`: Cung cấp các endpoint REST API:
  - `GET /health`: Trả về trạng thái hoạt động (Health Probe).
  - `GET /info`: Trả về thông tin nhóm thực hiện và đề tài.
  - `POST /api/stats`: Tiếp nhận dữ liệu số và trả kết quả tính toán.
  - `POST /api/merge`: Tiếp nhận dữ liệu từ 2 node và trả kết quả hòa trộn.

#### 2.3.3. Thiết kế các kịch bản kiểm thử (Unit Tests)
- **Kiểm thử tính toán (`test_app.py`):** Kiểm thử tính đúng đắn của phép toán thống kê và kiểm tra phản ứng của hệ thống khi danh sách dữ liệu rỗng (`ValueError`).
- **Kiểm thử hòa trộn dữ liệu sạch:** Đảm bảo khi hai node gửi các cặp key khác nhau, dữ liệu được gộp hoàn hảo (`status: MERGED`).
- **Kiểm thử phát hiện xung đột:** Đảm bảo khi hai node gửi cùng một key với giá trị trái ngược, hệ thống gắn cờ xung đột và áp dụng chính sách giải quyết tự động (`status: CONFLICTS_RESOLVED`).
- **Kiểm thử kịch bản lỗi (`test_fault_scenario.py`):** Cho phép kích hoạt biến môi trường `SIMULATE_FAIL=1` để cố tình tạo lỗi logic, phục vụ kiểm tra khả năng ngắt pipeline của hệ thống.

---

### 2.4. Đóng gói và cấu hình Pipeline trên GitHub Actions & GitLab CI

#### 2.4.1. Cấu hình GitHub Actions Workflow
Tệp `.github/workflows/ci-cd-distributed.yml` được cấu hình với 5 công việc (jobs) liên hoàn:
- Sử dụng chiến lược ma trận (`strategy: matrix`) để phân phối kiểm thử song song trên nhiều môi trường (`os: [ubuntu-latest, windows-latest]`).
- Cơ chế chuyển giao sản phẩm giữa các job bằng action `actions/upload-artifact@v4` và `actions/download-artifact@v4`.
- Điều kiện kiểm soát môi trường (`environment: production`) chỉ kích hoạt khi commit diễn ra trên nhánh `main`.

#### 2.4.2. Cấu hình GitLab CI/CD Pipeline
Tệp `.gitlab-ci.yml` định nghĩa 5 giai đoạn (`stages: [lint, test, package, staging, production]`):
- Tận dụng `artifacts` để lưu trữ bản release với thời gian hết hạn (`expire_in: 1 week`).
- Sử dụng quy tắc `rules: if: '$CI_COMMIT_BRANCH == "main"'` kết hợp `when: manual` để yêu cầu xác nhận phê duyệt chất lượng từ quản trị viên trước khi đưa lên môi trường Production.

#### 2.4.3. Cơ chế Quality Gate và bảo vệ nhánh chính
Quality Gate là bức tường bảo vệ chất lượng phần mềm. Trên GitHub và GitLab, quy tắc bảo vệ nhánh (Branch Protection Rules) yêu cầu:
1. Bắt buộc toàn bộ các bài kiểm thử trong pipeline phải có kết quả **Pass** (Status Check Success).
2. Yêu cầu ít nhất 1 thành viên trong nhóm phê duyệt mã nguồn (Code Review Approval).
3. Nghiêm cấm hành vi ép ghi đè lịch sử (`git push --force`) lên nhánh `main`.

---

## CHƯƠNG 3: TRIỂN KHAI THỬ NGHIỆM VÀ KHẮC PHỤC SỰ CỐ

### 3.1. Môi trường triển khai thực nghiệm
- **Hệ điều hành:** Windows 11 64-bit.
- **Môi trường thực thi:** Python 3.15 / PowerShell 7 / Windows Terminal.
- **Nền tảng kiểm thử phân tán:** GitHub Actions Runner / GitLab CI Engine.
- **Công cụ điều phối tự động:** PowerShell Automation Scripts (`run_local_tests.ps1`, `simulate_pipeline.ps1`).

---

### 3.2. Kết quả kiểm thử Unit Test cục bộ
Thực thi lệnh kiểm thử nhanh trên terminal PowerShell:
```powershell
.\run_local_tests.ps1
```
*Kết quả ghi nhận:*
- Toàn bộ 6/6 test cases đều vượt qua trong thời gian 0.223 giây.
- Hệ thống xác nhận mã nguồn đạt chuẩn, sẵn sàng đẩy lên Remote Repository.

*(Hình 3.1: Màn hình kiểm thử Unit Test thành công - Trạng thái ALL PASS)*

---

### 3.3. Kết quả thực thi Pipeline 5 Stages thành công
Thực thi kịch bản mô phỏng đầy đủ quy trình tích hợp liên tục phân tán:
```powershell
.\simulate_pipeline.ps1
```
*Kết quả ghi nhận theo từng giai đoạn:*
- **Stage 1 (Lint & Syntax):** Đạt chuẩn cú pháp Python trên runner Ubuntu.
- **Stage 2 (Distributed Matrix Tests):** Hai node Runner A và Runner B hoàn thành kiểm thử song song, đạt 6/6 bài kiểm tra.
- **Stage 3 (Build & Package):** Tạo thành công tệp thông tin release `dist\pipeline_build_info.json` và đóng gói artifact.
- **Stage 4 (Staging Deployment):** Triển khai thử nghiệm thành công, Health Check phản hồi mã HTTP 200 OK.
- **Stage 5 (Production Release):** Quality Gate xác nhận nhánh chính hợp lệ, hoàn tất phát hành phiên bản v1.0.0.

*(Hình 3.2: Toàn bộ 5 Stages của Pipeline phân tán chạy thành công)*

---

### 3.4. Thử nghiệm tình huống lỗi và cơ chế Quality Gate
Để chứng minh tính chịu lỗi và năng lực bảo vệ mã nguồn của hệ thống, nhóm tiến hành thử nghiệm giả lập lỗi logic thông qua cờ `-FailAtTest`:
```powershell
.\simulate_pipeline.ps1 -FailAtTest
```
*Hiện tượng quan sát được:*
1. Stage 1 (Linting) vẫn vượt qua thành công.
2. Tại Stage 2 (Distributed Test Matrix), Runner B phát hiện lỗi AssertionError từ bài kiểm tra `test_pipeline_quality_gate`.
3. **Cơ chế Fail-Fast được kích hoạt ngay lập tức:** Hệ thống tự động hủy bỏ các stage tiếp theo (Stage 3, 4, 5 không được chạy).
4. **Cơ chế Quality Gate:** Khóa trạng thái Pull Request trên GitHub/GitLab, báo đỏ toàn bộ Pipeline và từ chối hành động Merge vào nhánh `main`.

*(Hình 3.3: Pipeline bị ngắt kết nối tại Stage 2 khi phát hiện lỗi kiểm thử)*

---

### 3.5. Kết quả đóng gói và phân phối Artifact
Dữ liệu tệp build metadata được ghi nhận tại `dist/pipeline_build_info.json`:
```json
{
  "pipeline_id": 48215,
  "status": "SUCCESS",
  "commit": "7d4a9f8b",
  "branch": "main",
  "built_at": "2026-11-06T10:17:02"
}
```
Gói phần mềm sau khi đóng gói được phân phối lên kho lưu trữ đối tượng phân tán, cho phép các máy chủ biên tải về triển khai mà không cần biên dịch lại mã nguồn từ đầu.

---

### 3.6. Bảng tổng hợp các phép thử và đánh giá

| STT | Tên phép thử | Thao tác thực hiện | Kết quả quan sát | Đánh giá |
| :---: | :--- | :--- | :--- | :---: |
| **1** | Kiểm tra cú pháp tĩnh | `python -m py_compile` | Không có lỗi cú pháp | **ĐẠT** |
| **2** | Kiểm thử Unit Test | `run_local_tests.ps1` | 6/6 bài kiểm thử PASS (0.22s) | **ĐẠT** |
| **3** | Phân phối job song song | `simulate_pipeline.ps1` | Runner A và B chạy độc lập đồng thời | **ĐẠT** |
| **4** | Đóng gói Artifact | Kiểm tra thư mục `dist/` | Tạo metadata và gói nén thành công | **ĐẠT** |
| **5** | Kiểm tra dịch vụ Staging | Gọi endpoint `/health` | Phản hồi HTTP 200 OK | **ĐẠT** |
| **6** | Xử lý sự cố (Fault Test) | `simulate_pipeline.ps1 -FailAtTest` | Ngắt pipeline, khóa merge vào main | **ĐẠT** |

---

## KẾT LUẬN

### 1. Tổng kết kết quả đạt được
1. **Về mặt lý thuyết:** Đề tài đã phân tích và làm sáng tỏ nguyên lý vận hành của GitHub và GitLab dưới lăng kính của môn học Hệ phân tán. Làm rõ cấu trúc dữ liệu đồ thị DAG, cơ chế đồng bộ phi tập trung, thuật toán hòa trộn 3 điểm và kiến trúc Runner phân tán.
2. **Về mặt thực nghiệm:** Nhóm đã xây dựng thành công bộ mã nguồn dịch vụ phân tán, cấu hình hoàn chỉnh quy trình CI/CD 5 giai đoạn cho cả GitHub Actions và GitLab CI, đồng thời xây dựng các công cụ kịch bản tự động hóa kiểm thử và mô phỏng thực nghiệm.
3. **Về mặt chứng minh:** Các phép thử thực tế đã chứng minh rõ nét cơ chế Fail-Fast và Quality Gate – nền tảng then chốt bảo vệ tính ổn định của các hệ thống phân tán quy mô lớn.

### 2. Bài học kinh nghiệm
- **Hiểu rõ bản chất Git:** Phân biệt rõ sự khác nhau giữa Git (giao thức và công cụ DVCS phân tán) với GitHub/GitLab (nền tảng dịch vụ cộng tác và điều phối CI/CD).
- **Tầm quan trọng của kiểm thử tự động:** Trong một hệ thống phân tán có nhiều lập trình viên cùng đóng góp, kiểm thử tự động không phải là tùy chọn mà là điều kiện tiên quyết để duy trì tính nhất quán của hệ thống.
- **Tư duy thiết kế chịu lỗi:** Thiết kế các pipeline luôn phải tính đến các tình huống ngoại lệ, đảm bảo lỗi ở một nút mạng không làm sụp đổ toàn bộ chuỗi phát hành sản phẩm.

### 3. Hướng phát triển trong tương lai
- Triển khai cụm Self-Hosted GitLab Runner trên hạ tầng Kubernetes để tự động co giãn số lượng Runner theo tải công việc thực tế.
- Tích hợp thêm các khâu quét lỗ hổng bảo mật chuyên sâu (SAST/DAST) và kiểm tra phụ thuộc thư viện mã nguồn mở.
- Mở rộng cơ chế Geo-Replication (nhân bản phân tán theo vùng địa lý) giữa các máy chủ GitLab để nâng cao tính sẵn sàng cao (High Availability).

---

## TÀI LIỆU THAM KHẢO

1. Chacon, S., & Straub, B. (2014). *Pro Git* (2nd ed.). Apress. https://git-scm.com/book/en/v2
2. GitHub Documentation. (2026). *Understanding GitHub Actions & Distributed Workflows*. https://docs.github.com/en/actions
3. GitLab Documentation. (2026). *GitLab Architecture overview and Gitaly Cluster*. https://docs.gitlab.com/ee/development/architecture.html
4. GitLab Documentation. (2026). *GitLab CI/CD pipeline configuration reference*. https://docs.gitlab.com/ee/ci/yaml/
5. Tanenbaum, A. S., & Van Steen, M. (2017). *Distributed Systems: Principles and Paradigms* (3rd ed.). CreateSpace Independent Publishing Platform.
6. Humble, J., & Farley, D. (2010). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*. Addison-Wesley Professional.
7. Torvalds, L., & Hamano, J. (2005). *Git: Fast Version Control System Design*. https://git-scm.com
8. Fowler, M. (2018). *Patterns for Managing Source Code Branches in Distributed Teams*. MartinFowler.com.
9. Nygard, M. T. (2018). *Release It!: Design and Deploy Production-Ready Software* (2nd ed.). Pragmatic Bookshelf.
10. Morris, K. (2020). *Infrastructure as Code: Dynamic Systems for the Cloud Age* (2nd ed.). O'Reilly Media.

