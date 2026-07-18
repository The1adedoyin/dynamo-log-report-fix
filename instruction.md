There's an Apache-style access log at /app/access.log. Parse it and produce a summary report.

1. Write the report as valid JSON to /app/report.json.
2. Include a total_requests key: the total number of log lines in access.log, as an integer.
3. Include a unique_ips key: the number of distinct client IP addresses across all log lines, as an integer.
4. Include a top_path key: the request path that appears most often across all log lines, as a string (e.g. "/index.html").

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.