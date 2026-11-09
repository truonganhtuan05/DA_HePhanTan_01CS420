"""
Unit tests for DistributedTaskService
Môn học: Hệ phân tán (CS420G)
"""

import unittest
from src.app import DistributedTaskService

class TestDistributedTaskService(unittest.TestCase):
    def test_calculate_stats_success(self):
        numbers = [10, 20, 30, 40, 50]
        stats = DistributedTaskService.calculate_stats(numbers)
        self.assertEqual(stats["total_items"], 5)
        self.assertEqual(stats["sum"], 150.0)
        self.assertEqual(stats["average"], 30.0)
        self.assertEqual(stats["min"], 10.0)
        self.assertEqual(stats["max"], 50.0)

    def test_calculate_stats_single_element(self):
        stats = DistributedTaskService.calculate_stats([42])
        self.assertEqual(stats["total_items"], 1)
        self.assertEqual(stats["sum"], 42.0)
        self.assertEqual(stats["average"], 42.0)

    def test_calculate_stats_empty_input(self):
        with self.assertRaises(ValueError):
            DistributedTaskService.calculate_stats([])

    def test_merge_distributed_data_clean(self):
        node_a = {"task_1": "COMPLETED", "node": "Worker-01"}
        node_b = {"task_2": "PENDING", "node": "Worker-01"}
        result = DistributedTaskService.merge_distributed_data(node_a, node_b)
        self.assertEqual(result["status"], "MERGED")
        self.assertEqual(len(result["conflicts"]), 0)
        self.assertEqual(result["result"]["task_1"], "COMPLETED")
        self.assertEqual(result["result"]["task_2"], "PENDING")

    def test_merge_distributed_data_conflict(self):
        node_a = {"state": "ONLINE", "version": "1.0"}
        node_b = {"state": "OFFLINE", "version": "1.0"}
        result = DistributedTaskService.merge_distributed_data(node_a, node_b)
        self.assertEqual(result["status"], "CONFLICTS_RESOLVED")
        self.assertEqual(len(result["conflicts"]), 1)
        self.assertEqual(result["conflicts"][0]["key"], "state")
        self.assertEqual(result["result"]["state"], "OFFLINE")

if __name__ == "__main__":
    unittest.main()

