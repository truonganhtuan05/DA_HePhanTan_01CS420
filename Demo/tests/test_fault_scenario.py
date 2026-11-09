"""
Fault Scenario Simulation Test
Dùng để minh họa cơ chế Quality Gate trong CI/CD Pipeline.
Khi biến môi trường SIMULATE_FAIL=1, bài kiểm tra sẽ cố tình bị FAIL để chứng minh:
- Pipeline ngắt ngay lập tức (Fail-Fast).
- Không cho phép tự động deploy.
- Khóa tính năng Merge Pull Request trên GitHub / GitLab.
"""

import unittest
import os
from src.app import DistributedTaskService

class TestFaultScenario(unittest.TestCase):
    def test_pipeline_quality_gate(self):
        simulate_fail = os.environ.get("SIMULATE_FAIL", "0")
        if simulate_fail == "1":
            # Cố tình fail để chụp màn hình Pipeline Bị Đỏ (Red Pipeline)
            self.fail("[DEMO ERROR] Phát hiện lỗi logic nghiêm trọng trong mã nguồn! CI/CD Pipeline bị ngắt kết nối.")
        else:
            # Chạy bình thường
            stats = DistributedTaskService.calculate_stats([100, 200])
            self.assertEqual(stats["sum"], 300.0)

if __name__ == "__main__":
    unittest.main()

