"""
Distributed Calculation & Task API Service
Môn học: Hệ phân tán (CS420G) - Đại học Duy Tân
Ứng dụng minh họa quy trình CI/CD phân tán với GitHub Actions & GitLab CI
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys
import os

PORT = int(os.environ.get("PORT", 8080))
NODE_ID = os.environ.get("NODE_ID", "Worker-Node-01")
APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")

class DistributedTaskService:
    @staticmethod
    def calculate_stats(numbers):
        """Tính toán thống kê dữ liệu phân tán (Sum, Average, Min, Max)."""
        if not numbers or not isinstance(numbers, list):
            raise ValueError("Dữ liệu đầu vào phải là một danh sách số không rỗng.")
        
        valid_nums = [float(x) for x in numbers]
        total = sum(valid_nums)
        count = len(valid_nums)
        avg = round(total / count, 2)
        min_val = min(valid_nums)
        max_val = max(valid_nums)
        
        return {
            "total_items": count,
            "sum": total,
            "average": avg,
            "min": min_val,
            "max": max_val
        }

    @staticmethod
    def merge_distributed_data(node_a_data, node_b_data):
        """Giả lập cơ chế hòa trộn dữ liệu phân tán (Three-way merge simulation)."""
        if not isinstance(node_a_data, dict) or not isinstance(node_b_data, dict):
            raise TypeError("Dữ liệu hòa trộn phải là đối tượng dictionary.")
        
        merged = {}
        conflicts = []
        all_keys = set(node_a_data.keys()).union(set(node_b_data.keys()))
        
        for k in all_keys:
            if k in node_a_data and k in node_b_data:
                if node_a_data[k] == node_b_data[k]:
                    merged[k] = node_a_data[k]
                else:
                    conflicts.append({
                        "key": k,
                        "node_a_val": node_a_data[k],
                        "node_b_val": node_b_data[k],
                        "resolution": "NODE_B_WINS_BY_TIMESTAMP"
                    })
                    merged[k] = node_b_data[k]  # Last write wins
            elif k in node_a_data:
                merged[k] = node_a_data[k]
            else:
                merged[k] = node_b_data[k]
                
        return {
            "status": "MERGED" if not conflicts else "CONFLICTS_RESOLVED",
            "conflicts": conflicts,
            "result": merged
        }


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8"))

    def do_GET(self):
        if self.path == "/" or self.path == "/health":
            self._send_response(200, {
                "status": "UP",
                "service": "CS420G Distributed Demo API",
                "node_id": NODE_ID,
                "version": APP_VERSION
            })
        elif self.path == "/info":
            self._send_response(200, {
                "project": "01CS420 - GitHub GitLab CI/CD",
                "subject": "He Phan Tan (CS420G)",
                "team": ["Le Van Hoai Rin", "Nguyen Trung Hieu", "Truong Anh Tuan"],
                "instructor": "Nguyen Minh Nhat"
            })
        else:
            self._send_response(404, {"error": "Endpoint not found"})

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_body = self.rfile.read(content_length)
        
        try:
            req_data = json.loads(post_body.decode("utf-8"))
        except Exception as e:
            self._send_response(400, {"error": "Invalid JSON", "details": str(e)})
            return

        if self.path == "/api/stats":
            try:
                numbers = req_data.get("numbers", [])
                stats = DistributedTaskService.calculate_stats(numbers)
                self._send_response(200, {
                    "node_id": NODE_ID,
                    "metrics": stats
                })
            except Exception as ex:
                self._send_response(400, {"error": str(ex)})

        elif self.path == "/api/merge":
            try:
                node_a = req_data.get("node_a", {})
                node_b = req_data.get("node_b", {})
                res = DistributedTaskService.merge_distributed_data(node_a, node_b)
                self._send_response(200, res)
            except Exception as ex:
                self._send_response(400, {"error": str(ex)})
        else:
            self._send_response(404, {"error": "Endpoint not found"})

def run_server():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"[*] CS420G Service is running on port {PORT} (Node: {NODE_ID}, Version: {APP_VERSION})...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Shutting down server gracefully...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()

