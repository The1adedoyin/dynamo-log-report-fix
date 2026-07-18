import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Expected values computed directly from environment/data/access.log:
# 192.168.0.1 -> /index.html, /index.html   (2 requests)
# 192.168.0.2 -> /about.html, /index.html   (2 requests)
# 10.0.0.5    -> /api/login,  /about.html   (2 requests)
# totals: 6 requests, 3 unique IPs, /index.html is the top path (3 hits)
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load_report():
    assert REPORT_PATH.exists(), f"missing {REPORT_PATH}"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_is_valid_json():
    """Criterion 1: /app/report.json exists and contains valid JSON."""
    _load_report()


def test_total_requests_correct():
    """Criterion 2: total_requests equals the number of log lines in access.log."""
    report = _load_report()
    assert report.get("total_requests") == EXPECTED_TOTAL_REQUESTS, (
        f"expected total_requests={EXPECTED_TOTAL_REQUESTS}, got {report.get('total_requests')}"
    )


def test_unique_ips_correct():
    """Criterion 3: unique_ips equals the count of distinct client IPs in access.log."""
    report = _load_report()
    assert report.get("unique_ips") == EXPECTED_UNIQUE_IPS, (
        f"expected unique_ips={EXPECTED_UNIQUE_IPS}, got {report.get('unique_ips')}"
    )


def test_top_path_correct():
    """Criterion 4: top_path equals the most requested path in access.log."""
    report = _load_report()
    assert report.get("top_path") == EXPECTED_TOP_PATH, (
        f"expected top_path={EXPECTED_TOP_PATH!r}, got {report.get('top_path')!r}"
    )