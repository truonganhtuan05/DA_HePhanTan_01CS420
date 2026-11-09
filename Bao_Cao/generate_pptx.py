# -*- coding: utf-8 -*-
"""
Tự động tạo file Slide Thuyết Trình (.pptx) chuẩn đồ án Hệ phân tán Duy Tân
Đề tài: 01CS420 - GitHub GitLab trong Hệ phân tán
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation(output_path):
    prs = Presentation()
    # 16:9 Widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Color Palette
    NAVY = RGBColor(10, 37, 64)       # Header / Primary dark
    RED_DTU = RGBColor(186, 12, 47)   # DTU Accent Red
    BLUE_ACCENT = RGBColor(0, 119, 182) # Cyan/Blue accent
    BG_LIGHT = RGBColor(248, 249, 250) # Light grey background
    CARD_BG = RGBColor(255, 255, 255)
    CARD_BORDER = RGBColor(220, 226, 235)
    TEXT_DARK = RGBColor(33, 37, 41)
    TEXT_MUTED = RGBColor(108, 117, 125)
    WHITE = RGBColor(255, 255, 255)
    GREEN = RGBColor(40, 167, 69)

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_LIGHT
        bg.line.fill.background()
        return bg

    def add_header(slide, category, title):
        # Header banner
        banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        banner.fill.solid()
        banner.fill.fore_color.rgb = NAVY
        banner.line.fill.background()

        # Accent line
        accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.15), Inches(13.333), Inches(0.06))
        accent.fill.solid()
        accent.fill.fore_color.rgb = RED_DTU
        accent.line.fill.background()

        # Category & Title text
        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.5), Inches(0.95))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0

        p1 = tf.paragraphs[0]
        p1.text = category.upper()
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = RGBColor(144, 224, 239)

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(20)
        p2.font.bold = True
        p2.font.color.rgb = WHITE

        # Footer info
        ftBox = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.7), Inches(0.35))
        tf_ft = ftBox.text_frame
        tf_ft.margin_top = tf_ft.margin_bottom = tf_ft.margin_left = tf_ft.margin_right = 0
        p_ft = tf_ft.paragraphs[0]
        p_ft.text = "Đồ án Hệ phân tán (CS420G)  |  Mã đề 01CS420: GitHub & GitLab  |  Đại học Duy Tân"
        p_ft.font.size = Pt(10)
        p_ft.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title, body_bullets, title_color=NAVY):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1.5)

        txBox = slide.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.2), Inches(width - 0.5), Inches(height - 0.4))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = title_color
        p_t.space_after = Pt(8)

        for b in body_bullets:
            p = tf.add_paragraph()
            p.text = f"•  {b}"
            p.font.size = Pt(12)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(4)

    # =========================================================================
    # SLIDE 1: BÌA CHÍNH (TITLE SLIDE)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY
    bg1.line.fill.background()

    # DTU Badge Banner
    badge = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(4.5), Inches(0.45))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RED_DTU
    badge.line.fill.background()
    p_b = badge.text_frame.paragraphs[0]
    p_b.text = "TRƯỜNG ĐẠI HỌC DUY TÂN - KHOA KHOA HỌC MÁY TÍNH"
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = WHITE
    p_b.alignment = PP_ALIGN.CENTER

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.2))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "ĐỒ ÁN NHÓM - MÔN HỌC: HỆ PHÂN TÁN (CS420G)"
    p1.font.size = Pt(16)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(144, 224, 239)

    p2 = tf1.add_paragraph()
    p2.text = "TÌM HIỂU GITHUB, GITLAB VÀ TRIỂN KHAI\nQUY TRÌNH CI/CD PIPELINE PHÂN TÁN"
    p2.font.size = Pt(28)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(8)

    p3 = tf1.add_paragraph()
    p3.text = "MÃ ĐỀ TÀI: 01CS420  |  CHỦ ĐỀ: GITHUB & GITLAB"
    p3.font.size = Pt(14)
    p3.font.color.rgb = RGBColor(255, 214, 10)
    p3.space_before = Pt(8)

    # Info card on Title Slide
    info_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.3), Inches(11.7), Inches(2.4))
    info_card.fill.solid()
    info_card.fill.fore_color.rgb = RGBColor(20, 50, 85)
    info_card.line.color.rgb = RGBColor(50, 90, 140)

    tb_info = s1.shapes.add_textbox(Inches(1.1), Inches(4.5), Inches(11.1), Inches(2.0))
    tfi = tb_info.text_frame
    tfi.word_wrap = True

    p_gv = tfi.paragraphs[0]
    p_gv.text = "GIẢNG VIÊN HƯỚNG DẪN: ThS. Nguyễn Minh Nhật    |    LỚP: CS420G"
    p_gv.font.size = Pt(13)
    p_gv.font.bold = True
    p_gv.font.color.rgb = RGBColor(144, 224, 239)
    p_gv.space_after = Pt(10)

    p_sv = tfi.add_paragraph()
    p_sv.text = "SINH VIÊN THỰC HIỆN:"
    p_sv.font.size = Pt(12)
    p_sv.font.bold = True
    p_sv.font.color.rgb = WHITE

    sv_list = [
        "1. Lê Văn Hoài Rin  -  MSSV: 29211434001 (Trưởng nhóm)",
        "2. Nguyễn Trung Hiếu -  MSSV: 29211434002",
        "3. Trương Anh Tuấn  -  MSSV: 29211434003"
    ]
    for s_name in sv_list:
        p_m = tfi.add_paragraph()
        p_m.text = f"   •  {s_name}"
        p_m.font.size = Pt(12)
        p_m.font.color.rgb = RGBColor(230, 235, 245)

    # =========================================================================
    # SLIDE 2: MỤC LỤC & BỐ CỤC BÁO CÁO
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_background(s2)
    add_header(s2, "Nội dung trình bày", "BỐ CỤC BÁO CÁO ĐỒ ÁN")

    agenda_items = [
        ("1. Mở đầu", "Lý do chọn đề tài, mục tiêu, phạm vi nghiên cứu và phương pháp thực hiện."),
        ("2. Chương 1: Cơ sở lý thuyết", "Tổng quan DVCS, Git, kiến trúc phân tán GitHub/GitLab, đồ thị DAG, nguyên lý CI/CD."),
        ("3. Chương 2: Thiết kế Demo", "Bài toán thực tế, yêu cầu Input/Output, kiến trúc Pipeline 5 Stages, thiết kế mã nguồn."),
        ("4. Chương 3: Thực nghiệm & Kết quả", "Môi trường, 6 kịch bản kiểm thử, chụp ảnh log/màn hình thực tế, xử lý sự cố Quality Gate."),
        ("5. Kết luận & Định hướng", "Tổng kết kết quả đạt được, bài học kinh nghiệm và hướng phát triển hạ tầng trong tương lai.")
    ]
    for idx, (title, desc) in enumerate(agenda_items):
        top_y = 1.6 + idx * 1.05
        add_card(s2, 0.8, top_y, 11.7, 0.9, title, [desc], title_color=NAVY)

    # =========================================================================
    # SLIDE 3: MỞ ĐẦU - LÝ DO CHỌN ĐỀ TÀI
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_background(s3)
    add_header(s3, "Mở đầu", "1. LÝ DO CHỌN ĐỀ TÀI GITHUB & GITLAB")

    add_card(s3, 0.8, 1.6, 3.7, 5.2, "Vấn đề thực tế", [
        "Hệ thống tập trung (SVN/CVS) phụ thuộc hoàn toàn máy chủ.",
        "Mất mạng là tê liệt toàn bộ quy trình phát triển.",
        "Nguy cơ điểm lỗi đơn (SPOF): hỏng máy chủ là mất dữ liệu.",
        "Khó khăn khi mở rộng nhóm lập trình viên trên toàn cầu."
    ], RED_DTU)

    add_card(s3, 4.8, 1.6, 3.7, 5.2, "Giải pháp với DVCS", [
        "Mỗi client là một kho chứa đầy đủ (Full Mirror).",
        "Làm việc, commit, rẽ nhánh offline hoàn toàn.",
        "Mô hình đồ thị DAG bảo đảm tính toàn vẹn lịch sử mã nguồn.",
        "Cơ chế đồng bộ hóa phi tập trung qua Push/Fetch/Pull."
    ], BLUE_ACCENT)

    add_card(s3, 8.8, 1.6, 3.7, 5.2, "Giá trị với Hệ phân tán", [
        "Quan sát cơ chế Eventual Consistency và Three-way merge.",
        "Khảo sát tính chịu lỗi (Fault-Tolerance) của hệ thống.",
        "Điều phối tác vụ tự động hóa song song qua Distributed Runners.",
        "Xây dựng Quality Gate bảo vệ nhánh chính trong môi trường cộng tác."
    ], GREEN)

    # =========================================================================
    # SLIDE 4: MỞ ĐẦU - MỤC TIÊU & PHẠM VI
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_background(s4)
    add_header(s4, "Mở đầu", "2 & 3. MỤC TIÊU VÀ PHẠM VI NGHIÊN CỨU")

    add_card(s4, 0.8, 1.6, 5.7, 5.2, "Mục tiêu nghiên cứu", [
        "Lý thuyết: Nắm vững kiến trúc nội tại của GitHub (Spokes, Actions) và GitLab (Puma, Gitaly Cluster, Runner).",
        "Hiểu rõ cơ chế DAG, hàm băm SHA, phát hiện và xử lý xung đột (Conflict Resolution).",
        "Thực nghiệm: Xây dựng hoàn chỉnh Pipeline phân tán 5 Stages.",
        "Kiểm chứng cơ chế Fail-Fast và Quality Gate khi có sự cố."
    ])

    add_card(s4, 6.8, 1.6, 5.7, 5.2, "Phạm vi đề tài", [
        "Trong phạm vi:",
        "  - Mô hình DVCS và so sánh CVCS vs DVCS.",
        "  - Workflow GitHub Actions (.yml) & GitLab CI (.gitlab-ci.yml).",
        "  - Dịch vụ tính toán phân tán Python và bộ Unit Test tự động.",
        "  - Script mô phỏng và thực thi trên Runner phân tán.",
        "Ngoài phạm vi:",
        "  - Vận hành cụm máy chủ GitLab đa quốc gia trên phần cứng vật lý chuyên dụng.",
        "  - Đo kiểm tải hàng triệu request/giây trên môi trường thương mại."
    ])

    # =========================================================================
    # SLIDE 5: CHƯƠNG 1 - TỔNG QUAN DVCS & GIT
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_background(s5)
    add_header(s5, "Chương 1: Cơ sở lý thuyết", "1.1. TỔNG QUAN DVCS, GIT, GITHUB & GITLAB")

    add_card(s5, 0.8, 1.6, 5.7, 5.2, "DVCS & Git", [
        "DVCS (Distributed Version Control System):",
        "  - Không có kho lưu trữ nào là độc tôn về dữ liệu.",
        "  - Mọi nút đều có thể trở thành nguồn khôi phục dữ liệu.",
        "Git (Linus Torvalds, 2005):",
        "  - Lưu dữ liệu dưới dạng Snapshot (Ảnh chụp) trạng thái.",
        "  - Tốc độ xử lý siêu nhanh trên ổ đĩa cục bộ.",
        "  - Tính toán mã băm SHA đảm bảo tính toàn vẹn 100%."
    ])

    add_card(s5, 6.8, 1.6, 5.7, 5.2, "GitHub & GitLab", [
        "GitHub:",
        "  - Nền tảng SaaS Cloud lớn nhất thế giới (trên 100M dev).",
        "  - Nổi bật với Pull Request, Marketplace và GitHub Actions.",
        "GitLab:",
        "  - Giải pháp DevOps All-in-One hoàn chỉnh.",
        "  - Hỗ trợ Self-Hosted cực mạnh cho doanh nghiệp cần bảo mật tuyệt đối.",
        "  - Tích hợp sẵn GitLab CI/CD và bộ quản lý Runner đa năng."
    ])

    # =========================================================================
    # SLIDE 6: CHƯƠNG 1 - SO SÁNH CVCS VÀ DVCS
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_background(s6)
    add_header(s6, "Chương 1: Cơ sở lý thuyết", "BẢNG SO SÁNH: HỆ TẬP TRUNG (CVCS) VS HỆ PHÂN TÁN (DVCS)")

    add_card(s6, 0.8, 1.6, 11.7, 5.2, "Đặc điểm so sánh kỹ thuật", [
        "1. Bản sao kho lưu trữ: CVCS chỉ lưu tại 1 Server trung tâm  <-->  DVCS mỗi máy khách giữ 1 bản sao trọn vẹn.",
        "2. Khả năng Offline: CVCS tê liệt hoàn toàn khi mất mạng  <-->  DVCS commit, xem log, rẽ nhánh offline 100%.",
        "3. Điểm lỗi đơn (SPOF): CVCS sập Server là mất hết lịch sử  <-->  DVCS bất kỳ Client nào cũng khôi phục được Server.",
        "4. Hiệu năng & Tốc độ: CVCS phụ thuộc băng thông mạng  <-->  DVCS thao tác trực tiếp đĩa cứng cục bộ siêu tốc.",
        "5. Rẽ nhánh & Hòa trộn: CVCS tốn tài nguyên và dễ lỗi  <-->  DVCS chi phí nhánh O(1), cơ chế Three-way merge mạnh mẽ."
    ], NAVY)

    # =========================================================================
    # SLIDE 7: CHƯƠNG 1 - SO SÁNH GITHUB VÀ GITLAB
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_background(s7)
    add_header(s7, "Chương 1: Cơ sở lý thuyết", "SO SÁNH NỀN TẢNG GITHUB VÀ GITLAB")

    add_card(s7, 0.8, 1.6, 5.7, 5.2, "Nền tảng GitHub", [
        "Mô hình: Tập trung chính vào SaaS Đám mây.",
        "CI/CD Engine: GitHub Actions với thư viện khổng lồ từ GitHub Marketplace.",
        "Hạ tầng Runner: GitHub-Hosted Runners (quản lý bởi GitHub) và Self-Hosted Runners.",
        "Cộng đồng: Kho lưu trữ mã nguồn mở lớn nhất thế giới, tối ưu cho Open Source."
    ], BLUE_ACCENT)

    add_card(s7, 6.8, 1.6, 5.7, 5.2, "Nền tảng GitLab", [
        "Mô hình: Vừa có SaaS vừa hỗ trợ Self-Hosted (GitLab Community Edition cài trên Server riêng).",
        "CI/CD Engine: GitLab CI/CD tích hợp sâu sắc vào vòng đời sản phẩm.",
        "Hạ tầng Runner: GitLab Runner hỗ trợ Docker, Kubernetes, SSH, Shell.",
        "Phù hợp: Doanh nghiệp, ngân hàng, quốc phòng yêu cầu lưu trữ mã nguồn nội bộ."
    ], RED_DTU)

    # =========================================================================
    # SLIDE 8: CHƯƠNG 1 - KIẾN TRÚC PHÂN TÁN GITHUB
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_background(s8)
    add_header(s8, "Chương 1: Cơ sở lý thuyết", "1.2. KIẾN TRÚC HẠ TẦNG PHÂN TÁN CỦA GITHUB")

    add_card(s8, 0.8, 1.6, 3.7, 5.2, "Lớp Cân bằng tải & Mạng", [
        "Anycast IP và CDN toàn cầu.",
        "Reverse Proxy tiếp nhận SSH & HTTPS.",
        "Phân tán tải tới các Data Center theo vị trí địa lý."
    ])

    add_card(s8, 4.8, 1.6, 3.7, 5.2, "Lớp Lưu trữ Git Phân tán", [
        "Spokes Cluster: Cụm máy chủ chuyên trách nhân bản Git Repo.",
        "Đảm bảo dữ liệu ghi nhân bản đồng bộ sang nhiều Node.",
        "Vitess & MySQL phân tán lưu trữ Metadata."
    ])

    add_card(s8, 8.8, 1.6, 3.7, 5.2, "Cụm Tính toán Actions", [
        "Hàng triệu máy ảo Runner phân tán theo nhu cầu (Ephemeral VMs).",
        "Hàng đợi tác vụ điều phối qua Kafka/Redis.",
        "Chia sẻ Artifact qua Azure Blob Storage."
    ])

    # =========================================================================
    # SLIDE 9: CHƯƠNG 1 - KIẾN TRÚC PHÂN TÁN GITLAB
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_background(s9)
    add_header(s9, "Chương 1: Cơ sở lý thuyết", "1.2. KIẾN TRÚC CÁC THÀNH PHẦN PHÂN TÁN CỦA GITLAB")

    add_card(s9, 0.8, 1.6, 5.7, 5.2, "Lõi máy chủ GitLab CE", [
        "• GitLab Workhorse: Reverse proxy xử lý tải Git HTTP nặng.",
        "• GitLab Rails (Puma): Xử lý logic ứng dụng và Web UI.",
        "• PostgreSQL & Redis: Cơ sở dữ liệu và hàng đợi cache.",
        "• Sidekiq: Tiến trình xử lý tác vụ nền phân tán bất đồng bộ."
    ])

    add_card(s9, 6.8, 1.6, 5.7, 5.2, "Cụm Lưu trữ & Runner Phân tán", [
        "• Gitaly Cluster (Praefect): Cụm lưu trữ Git đạt chuẩn High Availability (HA), tự động phát hiện node chết và failover.",
        "• GitLab Runners: Các agent độc lập cài trên nhiều server khác nhau, liên tục kết nối về GitLab để nhận job xử lý song song."
    ])

    # =========================================================================
    # SLIDE 10: CHƯƠNG 1 - ĐỒ THỊ DAG CỦA GIT
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_background(s10)
    add_header(s10, "Chương 1: Cơ sở lý thuyết", "1.3. CẤU TRÚC ĐỒ THỊ DAG TRONG GIT (DIRECTED ACYCLIC GRAPH)")

    add_card(s10, 0.8, 1.6, 5.7, 5.2, "4 Đối tượng nền tảng trong Git", [
        "1. Blob (Binary Large Object): Lưu trữ nội dung tệp tin.",
        "2. Tree: Đại diện thư mục, ánh xạ tên file tới Blob hash.",
        "3. Commit: Chứa thông tin tác giả, thời gian, con trỏ tới Tree và con trỏ trỏ về commit cha (Parent).",
        "4. Tag / Branch Pointer: Con trỏ di động trỏ tới commit."
    ])

    add_card(s10, 6.8, 1.6, 5.7, 5.2, "Ý nghĩa với Hệ phân tán", [
        "• Đồ thị có hướng không chu trình (DAG): Không có vòng lặp vô tận trong lịch sử.",
        "• Hàm băm Mật mã học (SHA-1/SHA-256): Dữ liệu bất biến (Immutable), không thể sửa trộm commit quá khứ.",
        "• Rẽ nhánh (Branching): Chỉ là tạo 1 con trỏ mới, chi phí O(1) cực nhẹ."
    ])

    # =========================================================================
    # SLIDE 11: CHƯƠNG 1 - HÒA TRỘN & XUNG ĐỘT PHÂN TÁN
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_background(s11)
    add_header(s11, "Chương 1: Cơ sở lý thuyết", "CƠ CHẾ ĐỒNG BỘ, RẼ NHÁNH VÀ XỬ LÝ XUNG ĐỘT")

    add_card(s11, 0.8, 1.6, 3.7, 5.2, "Three-way Merge", [
        "Xác định Commit gốc chung (Common Ancestor).",
        "So sánh nhánh A với gốc.",
        "So sánh nhánh B với gốc.",
        "Tự động hòa trộn nếu 2 nhánh sửa ở các dòng khác nhau."
    ])

    add_card(s11, 4.8, 1.6, 3.7, 5.2, "Xung đột phân tán", [
        "Xảy ra khi cả 2 nhánh cùng sửa cùng 1 vị trí tệp.",
        "Git dừng tự động hòa trộn.",
        "Đánh dấu thẻ conflict (<<<<<<< ======= >>>>>>>).",
        "Đảm bảo an toàn, không tự ý ghi đè mất mã nguồn."
    ], RED_DTU)

    add_card(s11, 8.8, 1.6, 3.7, 5.2, "Giải quyết xung đột", [
        "Lập trình viên xem xét ngữ cảnh nghiệp vụ.",
        "Lựa chọn giữ phiên bản A, B hoặc gộp cả hai.",
        "Tạo một Commit hòa trộn mới (Merge Commit).",
        "Cập nhật lại đồ thị DAG chung."
    ], GREEN)

    # =========================================================================
    # SLIDE 12: CHƯƠNG 1 - WEBHOOK VÀ CI/CD RUNNERS
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_background(s12)
    add_header(s12, "Chương 1: Cơ sở lý thuyết", "CƠ CHẾ WEBHOOK VÀ ĐIỀU PHỐI RUNNER PHÂN TÁN")

    add_card(s12, 0.8, 1.6, 5.7, 5.2, "Cơ chế Webhook", [
        "Kiến trúc hướng sự kiện (Event-driven Architecture).",
        "Mỗi khi có Push, Merge, Pull Request, máy chủ Git phát tin HTTP POST.",
        "Payload chứa thông tin chi tiết commit và người thực hiện.",
        "Kích hoạt các hệ thống bên thứ ba và CI/CD Pipelines."
    ])

    add_card(s12, 6.8, 1.6, 5.7, 5.2, "Điều phối Runner Phân tán", [
        "Hàng đợi tác vụ (Job Queue) trung tâm phân chia công việc.",
        "Runners phân tán (Ubuntu, Windows, macOS, Container) kéo việc về chạy.",
        "Chạy song song (Parallel Execution) giúp giảm thời gian kiểm thử.",
        "Chia sẻ Artifact qua giao thức lưu trữ phân tán."
    ])

    # =========================================================================
    # SLIDE 13: CHƯƠNG 2 - BÀI TOÁN DEMO
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_background(s13)
    add_header(s13, "Chương 2: Thiết kế Demo", "2.1. ĐẶT BÀI TOÁN VÀ YÊU CẦU ỨNG DỤNG THỰC TẾ")

    add_card(s13, 0.8, 1.6, 5.7, 5.2, "Bài toán thực tế", [
        "Xây dựng dịch vụ phân tán (Distributed Task Service) phục vụ tính toán số liệu và hòa trộn dữ liệu đa node.",
        "Mã nguồn được quản lý trên GitHub / GitLab.",
        "Thiết lập quy trình CI/CD Pipeline 5 Stages tự động.",
        "Mỗi khi push code hoặc mở Pull Request, hệ thống tự động kiểm thử trên nhiều Runner phân tán."
    ])

    add_card(s13, 6.8, 1.6, 5.7, 5.2, "Yêu cầu Đầu vào & Đầu ra", [
        "Đầu vào (Input):",
        "  - Mã nguồn mới hoặc Pull Request vào nhánh 'main'.",
        "  - Bộ test suite kiểm thử tính toán và hòa trộn dữ liệu.",
        "Đầu ra (Output):",
        "  - Báo cáo kiểm thử tự động từ các Runner phân tán.",
        "  - Gói phân phối ứng dụng (Artifact tar.gz / JSON).",
        "  - Triển khai và Health Check thành công tại Staging.",
        "  - Quyết định cho phép hoặc chặn merge của Quality Gate."
    ])

    # =========================================================================
    # SLIDE 14: CHƯƠNG 2 - KIẾN TRÚC PIPELINE 5 STAGES
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_background(s14)
    add_header(s14, "Chương 2: Thiết kế Demo", "2.2. SƠ ĐỒ KIẾN TRÚC PIPELINE PHÂN TÁN 5 STAGES")

    stages = [
        ("STAGE 1", "Lint & Syntax Check", "Kiểm tra cú pháp tĩnh mã nguồn Python."),
        ("STAGE 2", "Distributed Matrix Tests", "Chạy song song trên Runner Ubuntu & Windows."),
        ("STAGE 3", "Package & Artifacts", "Đóng gói release và upload lên Object Storage."),
        ("STAGE 4", "Deploy to Staging", "Bung gói lên Staging Node & kiểm tra Health."),
        ("STAGE 5", "Production & Quality Gate", "Kiểm tra nhánh main và bảo vệ phát hành.")
    ]
    for idx, (stg, title, desc) in enumerate(stages):
        left_x = 0.8 + idx * 2.38
        add_card(s14, left_x, 1.6, 2.2, 5.2, stg, [title, "", desc], title_color=BLUE_ACCENT)

    # =========================================================================
    # SLIDE 15: CHƯƠNG 2 - THIẾT KẾ MÃ NGUỒN VÀ KIỂM THỬ
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_background(s15)
    add_header(s15, "Chương 2: Thiết kế Demo", "2.3. THIẾT KẾ MÃ NGUỒN VÀ BỘ KIỂM THỬ TỰ ĐỘNG")

    add_card(s15, 0.8, 1.6, 5.7, 5.2, "Dịch vụ nghiệp vụ (app.py)", [
        "• calculate_stats(numbers):",
        "    Tính toán thống kê dữ liệu phân tán (Sum, Avg, Min, Max).",
        "• merge_distributed_data(node_a, node_b):",
        "    Mô phỏng Three-way merge và phát hiện xung đột dữ liệu.",
        "• SimpleAPIHandler:",
        "    REST API Endpoint: /health, /info, /api/stats, /api/merge."
    ])

    add_card(s15, 6.8, 1.6, 5.7, 5.2, "Bộ kiểm thử tự động (Unit Tests)", [
        "• test_app.py:",
        "    - Test tính đúng đắn của phép tính số học phân tán.",
        "    - Test xử lý ngoại lệ khi danh sách số liệu rỗng.",
        "    - Test hòa trộn dữ liệu không có xung đột.",
        "    - Test phát hiện xung đột khi hai node ghi đè cùng key.",
        "• test_fault_scenario.py:",
        "    - Cho phép kích hoạt biến SIMULATE_FAIL=1 để giả lập lỗi kiểm thử phục vụ chụp ảnh Quality Gate."
    ])

    # =========================================================================
    # SLIDE 16: CHƯƠNG 2 - CẤU HÌNH GITHUB ACTIONS & GITLAB CI
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_background(s16)
    add_header(s16, "Chương 2: Thiết kế Demo", "2.4. CẤU HÌNH PIPELINE TRÊN GITHUB ACTIONS & GITLAB CI")

    add_card(s16, 0.8, 1.6, 5.7, 5.2, "GitHub Actions (.yml)", [
        "• Tệp: .github/workflows/ci-cd-distributed.yml",
        "• strategy: matrix (os: [ubuntu, windows], python: [3.10, 3.11, 3.12]).",
        "• upload-artifact / download-artifact để chuyển giao bản build qua các job.",
        "• environment: production chỉ kích hoạt trên nhánh main."
    ], BLUE_ACCENT)

    add_card(s16, 6.8, 1.6, 5.7, 5.2, "GitLab CI (.gitlab-ci.yml)", [
        "• Tệp: .gitlab-ci.yml",
        "• stages: [lint, test, package, staging, production].",
        "• artifacts: lưu trữ gói tar.gz với expire_in: 1 week.",
        "• rules kết hợp when: manual yêu cầu phê duyệt trước khi lên Production."
    ], RED_DTU)

    # =========================================================================
    # SLIDE 17: CHƯƠNG 3 - MÔI TRƯỜNG & KỊCH BẢN THỰC NGHIỆM
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_background(s17)
    add_header(s17, "Chương 3: Thực nghiệm & Đánh giá", "3.1. MÔI TRƯỜNG VÀ CÁC PHÉP THỬ THỰC TẾ")

    add_card(s17, 0.8, 1.6, 3.7, 5.2, "Môi trường thực nghiệm", [
        "Hệ điều hành: Windows 11 64-bit.",
        "Python Runtime: 3.15.",
        "PowerShell 7 Terminal.",
        "Distributed Runners (GitHub Actions & GitLab Engine)."
    ])

    add_card(s17, 4.8, 1.6, 3.7, 5.2, "Kịch bản kiểm thử", [
        "Phép thử 1: Chạy Unit Test tự động cục bộ.",
        "Phép thử 2: Chạy thành công toàn bộ 5 Stages Pipeline.",
        "Phép thử 3: Kích hoạt lỗi giả lập và kiểm tra Fail-Fast.",
        "Phép thử 4: Đóng gói và lưu trữ Artifact phân tán."
    ])

    add_card(s17, 8.8, 1.6, 3.7, 5.2, "Mục tiêu quan sát", [
        "Quan sát thời gian chạy song song của Runner.",
        "Kiểm tra tính toàn vẹn gói phát hành.",
        "Kiểm tra phản hồi Health Probe của Staging.",
        "Chứng minh Quality Gate ngăn chặn mã lỗi vào nhánh main."
    ])

    # =========================================================================
    # SLIDE 18: CHƯƠNG 3 - KẾT QUẢ UNIT TEST CỤC BỘ
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    add_background(s18)
    add_header(s18, "Chương 3: Thực nghiệm & Đánh giá", "3.2. KẾT QUẢ THỰC THI UNIT TEST CỤC BỘ (ALL PASS)")

    add_card(s18, 0.8, 1.6, 5.7, 5.2, "Lệnh thực thi & Kết quả", [
        "Lệnh PowerShell:",
        "  .\\run_local_tests.ps1",
        "",
        "Kết quả đo lường:",
        "  • 6/6 test cases vượt qua hoàn toàn.",
        "  • Thời gian chạy: 0.223 giây.",
        "  • Exit Code: 0 (Thành công).",
        "  • Trạng thái: Sẵn sàng đẩy lên Remote Repo."
    ], GREEN)

    add_card(s18, 6.8, 1.6, 5.7, 5.2, "Vị trí dán hình ảnh báo cáo", [
        "[HÌNH ẢNH 3.1: MÀN HÌNH CHẠY UNIT TEST XANH]",
        "",
        "• Dán ảnh chụp màn hình PowerShell hiển thị:",
        "  - Ran 6 tests in 0.001s -> OK.",
        "  - [STATUS: PASS] Tất cả bài kiểm thử đều vượt qua!",
        "  - Dòng chữ xanh thông báo sẵn sàng đẩy code."
    ])

    # =========================================================================
    # SLIDE 19: CHƯƠNG 3 - KẾT QUẢ PIPELINE 5 STAGES THÀNH CÔNG
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    add_background(s19)
    add_header(s19, "Chương 3: Thực nghiệm & Đánh giá", "3.3. THỰC THI THÀNH CÔNG PIPELINE PHÂN TÁN 5 STAGES")

    add_card(s19, 0.8, 1.6, 5.7, 5.2, "Lệnh thực thi & Kết quả", [
        "Lệnh PowerShell:",
        "  .\\simulate_pipeline.ps1",
        "",
        "Kết quả quan sát 5 Stages:",
        "  • Stage 1 (Lint): Cú pháp hợp lệ 100%.",
        "  • Stage 2 (Parallel Tests): Runner A & B đều PASS.",
        "  • Stage 3 (Package): Tạo tệp metadata & tar.gz.",
        "  • Stage 4 (Staging): Triển khai & Health 200 OK.",
        "  • Stage 5 (Production): Quality Gate cấp phép release."
    ], GREEN)

    add_card(s19, 6.8, 1.6, 5.7, 5.2, "Vị trí dán hình ảnh báo cáo", [
        "[HÌNH ẢNH 3.2: 5 STAGES PIPELINE MÀU XANH]",
        "",
        "• Dán ảnh chụp màn hình PowerShell hiển thị đầy đủ 5 stage màu xanh lá cây:",
        "  - [STAGE 1/5] LINT & SYNTAX VERIFICATION",
        "  - [STAGE 2/5] DISTRIBUTED TEST MATRIX",
        "  - [STAGE 3/5] BUILD & PACKAGE ARTIFACT",
        "  - [STAGE 4/5] STAGING DEPLOYMENT",
        "  - [STAGE 5/5] PRODUCTION RELEASE & QUALITY GATE"
    ])

    # =========================================================================
    # SLIDE 20: CHƯƠNG 3 - KỊCH BẢN LỖI & QUALITY GATE
    # =========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    add_background(s20)
    add_header(s20, "Chương 3: Thực nghiệm & Đánh giá", "3.4. THỬ NGHIỆM TÌNH HUỐNG LỖI VÀ QUALITY GATE")

    add_card(s20, 0.8, 1.6, 5.7, 5.2, "Lệnh thực thi & Hiện tượng lỗi", [
        "Lệnh PowerShell:",
        "  .\\simulate_pipeline.ps1 -FailAtTest",
        "",
        "Hiện tượng quan sát được:",
        "  • Stage 1: Vẫn PASS bình thường.",
        "  • Stage 2: Runner B báo FAIL bài test.",
        "  • Cơ chế Fail-Fast: Lập tức NGẮT pipeline.",
        "  • Stage 3, 4, 5 bị hủy bỏ hoàn toàn.",
        "  • Quality Gate: TỪ CHỐI Merge vào nhánh main."
    ], RED_DTU)

    add_card(s20, 6.8, 1.6, 5.7, 5.2, "Vị trí dán hình ảnh báo cáo", [
        "[HÌNH ẢNH 3.3: PIPELINE BỊ NGẮT MÀU ĐỎ]",
        "",
        "• Dán ảnh chụp màn hình PowerShell hiển thị chữ đỏ:",
        "  - FAIL: test_pipeline_quality_gate",
        "  - [STAGE 2 FAILED]: Phát hiện lỗi kiểm thử!",
        "  - [QUALITY GATE TRIGGERED]: Ngắt pipeline ngay!",
        "  - [STATUS: BLOCKED]: Từ chối Merge vào 'main'."
    ])

    # =========================================================================
    # SLIDE 21: CHƯƠNG 3 - BẢNG TỔNG HỢP CÁC PHÉP THỬ
    # =========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    add_background(s21)
    add_header(s21, "Chương 3: Thực nghiệm & Đánh giá", "3.6. BẢNG TỔNG HỢP CÁC PHÉP THỬ THỰC NGHIỆM")

    add_card(s21, 0.8, 1.6, 11.7, 5.2, "Bảng tổng hợp kết quả (100% Đạt yêu cầu)", [
        "1. Kiểm tra cú pháp tĩnh (py_compile)  ----------------->  Không có lỗi cú pháp  -------------->  [ĐẠT]",
        "2. Kiểm thử Unit Test (run_local_tests.ps1)  --------->  6/6 tests PASS trong 0.22s  --------->  [ĐẠT]",
        "3. Phân phối song song (simulate_pipeline.ps1)  ------>  Runner A & B chạy đồng thời  -------->  [ĐẠT]",
        "4. Đóng gói Artifact (dist/pipeline_build_info)  ------>  Tạo gói nén & metadata  ------------->  [ĐẠT]",
        "5. Kiểm tra Staging Service (/health)  ---------------->  Phản hồi HTTP 200 OK  --------------->  [ĐẠT]",
        "6. Xử lý sự cố Fail-Fast (-FailAtTest)  --------------->  Khóa nhánh main, bảo vệ hệ thống  --->  [ĐẠT]"
    ], GREEN)

    # =========================================================================
    # SLIDE 22: KẾT LUẬN - KẾT QUẢ ĐẠT ĐƯỢC
    # =========================================================================
    s22 = prs.slides.add_slide(blank_layout)
    add_background(s22)
    add_header(s22, "Kết luận", "1. TỔNG KẾT KẾT QUẢ ĐẠT ĐƯỢC")

    add_card(s22, 0.8, 1.6, 3.7, 5.2, "Về Lý thuyết", [
        "Hệ thống hóa toàn diện kiến trúc phân tán của GitHub & GitLab.",
        "Làm sáng tỏ cấu trúc đồ thị DAG, thuật toán Three-way merge và cơ chế giải quyết xung đột.",
        "So sánh chi tiết CVCS vs DVCS và GitHub vs GitLab."
    ])

    add_card(s22, 4.8, 1.6, 3.7, 5.2, "Về Sản phẩm Demo", [
        "Xây dựng dịch vụ phân tán REST API bằng Python.",
        "Cấu hình trọn vẹn 5 Stages CI/CD trên cả GitHub Actions và GitLab CI.",
        "Bộ script tự động hóa kiểm thử và mô phỏng pipeline trực quan."
    ])

    add_card(s22, 8.8, 1.6, 3.7, 5.2, "Về Kiểm chứng", [
        "Thực hiện thành công 6 phép thử thực nghiệm.",
        "Chứng minh cơ chế phân phối song song của Runners.",
        "Xác nhận cơ chế Fail-Fast và Quality Gate chặn đứng mã lỗi."
    ], GREEN)

    # =========================================================================
    # SLIDE 23: KẾT LUẬN - BÀI HỌC KINH NGHIỆM
    # =========================================================================
    s23 = prs.slides.add_slide(blank_layout)
    add_background(s23)
    add_header(s23, "Kết luận", "2. BÀI HỌC KINH NGHIỆM RÚT RA TỪ ĐỒ ÁN")

    add_card(s23, 0.8, 1.6, 11.7, 5.2, "Các bài học quan trọng trong Hệ phân tán", [
        "1. Phân biệt rõ Git và GitHub/GitLab: Git là giao thức DVCS cốt lõi; GitHub và GitLab là nền tảng quản trị và tự động hóa.",
        "2. Kiểm thử tự động là xương sống: Trong môi trường phân tán nhiều người code, không thể tin tưởng việc kiểm tra thủ công.",
        "3. Cơ chế Fail-Fast cứu rỗi hệ thống: Phát hiện lỗi càng sớm ở các Stage đầu thì chi phí khắc phục sự cố càng rẻ.",
        "4. Quality Gate không thể thiếu: Branch Protection Rules là chốt chặn cuối cùng bảo vệ môi trường Production.",
        "5. Tính bất biến của dữ liệu: Hiểu cách DAG và hàm băm SHA bảo vệ lịch sử phát triển phần mềm."
    ])

    # =========================================================================
    # SLIDE 24: KẾT LUẬN - HƯỚNG PHÁT TRIỂN
    # =========================================================================
    s24 = prs.slides.add_slide(blank_layout)
    add_background(s24)
    add_header(s24, "Kết luận", "3. HƯỚNG PHÁT TRIỂN TRONG TƯƠNG LAI")

    add_card(s24, 0.8, 1.6, 3.7, 5.2, "Mở rộng Hạ tầng", [
        "Triển khai cụm Self-Hosted GitLab Runner trên Kubernetes (K8s).",
        "Tự động co giãn (Autoscaling) số lượng Runner theo khối lượng commit."
    ])

    add_card(s24, 4.8, 1.6, 3.7, 5.2, "Tích hợp DevSecOps", [
        "Quét mã tĩnh với SonarQube.",
        "Quét lỗ hổng container image với Trivy.",
        "Kiểm tra lộ bí mật (Secret leak scanning) với GitGuardian."
    ])

    add_card(s24, 8.8, 1.6, 3.7, 5.2, "Đồng bộ Đa vùng", [
        "Cấu hình GitLab Geo-Replication giữa hai trung tâm dữ liệu.",
        "Đảm bảo khả năng phục hồi sau thảm họa (Disaster Recovery)."
    ])

    # =========================================================================
    # SLIDE 25: TÀI LIỆU THAM KHẢO
    # =========================================================================
    s25 = prs.slides.add_slide(blank_layout)
    add_background(s25)
    add_header(s25, "Tài liệu", "TÀI LIỆU THAM KHẢO")

    add_card(s25, 0.8, 1.6, 11.7, 5.2, "Danh mục tài liệu chính", [
        "[1] Chacon, S., & Straub, B. (2014). Pro Git (2nd ed.). Apress.",
        "[2] GitHub Documentation. (2026). Understanding GitHub Actions & Distributed Workflows. https://docs.github.com/en/actions",
        "[3] GitLab Documentation. (2026). GitLab Architecture overview and Gitaly Cluster. https://docs.gitlab.com/ee/development/architecture.html",
        "[4] GitLab Documentation. (2026). GitLab CI/CD pipeline configuration reference. https://docs.gitlab.com/ee/ci/yaml/",
        "[5] Tanenbaum, A. S., & Van Steen, M. (2017). Distributed Systems: Principles and Paradigms (3rd ed.).",
        "[6] Humble, J., & Farley, D. (2010). Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation.",
        "[7] Fowler, M. (2018). Patterns for Managing Source Code Branches in Distributed Teams."
    ])

    # =========================================================================
    # SLIDE 26: CẢM ƠN & HỎI ĐÁP (Q&A)
    # =========================================================================
    s26 = prs.slides.add_slide(blank_layout)
    bg26 = s26.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg26.fill.solid()
    bg26.fill.fore_color.rgb = NAVY
    bg26.line.fill.background()

    tb_end = s26.shapes.add_textbox(Inches(1.5), Inches(2.2), Inches(10.333), Inches(3.0))
    tfe = tb_end.text_frame
    tfe.word_wrap = True

    pe1 = tfe.paragraphs[0]
    pe1.alignment = PP_ALIGN.CENTER
    pe1.text = "XIN TRÂN TRỌNG CẢM ƠN THẦY VÀ CÁC BẠN!"
    pe1.font.size = Pt(28)
    pe1.font.bold = True
    pe1.font.color.rgb = WHITE

    pe2 = tfe.add_paragraph()
    pe2.alignment = PP_ALIGN.CENTER
    pe2.text = "PHẦN HỎI ĐÁP & ĐÓNG GÓP Ý KIẾN (Q&A)"
    pe2.font.size = Pt(20)
    pe2.font.bold = True
    pe2.font.color.rgb = RGBColor(144, 224, 239)
    pe2.space_before = Pt(16)

    pe3 = tfe.add_paragraph()
    pe3.alignment = PP_ALIGN.CENTER
    pe3.text = "Nhóm 01 (Mã đề: 01CS420)  -  Lớp CS420G  -  Đại học Duy Tân"
    pe3.font.size = Pt(13)
    pe3.font.italic = True
    pe3.font.color.rgb = RGBColor(220, 226, 235)
    pe3.space_before = Pt(16)

    prs.save(output_path)
    print(f"[OK] Presentation slide generated at: {output_path}")

if __name__ == "__main__":
    out_dir = r"d:\HocKyI_Nam4\CS_420_G\DA_HePhanTan_ver2\Bao_Cao"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "Slide_Bao_Cao_01CS420_GitHub_GitLab.pptx")
    create_presentation(out_file)

