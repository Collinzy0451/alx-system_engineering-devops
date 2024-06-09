#Postmortem: Web Stack Outage on June 1, 2024
Issue Summary
Duration:
The outage lasted from 10:00 AM to 12:30 PM (PDT) on June 1, 2024.

Impact:
The outage affected 70% of our users. Users experienced slow load times and frequent 500 Internal Server Error messages on the main website. The mobile application was also partially affected, with significant latency in loading data.

Root Cause:
The root cause was an overloaded database server due to a misconfigured database query that caused excessive CPU and memory usage.

Timeline
10:00 AM: Issue detected by automated monitoring system; high latency and error rate alerts triggered.
10:05 AM: On-call engineer notified and begins investigation.
10:15 AM: Initial investigation suggests network latency issues; network team is engaged.
10:30 AM: Network team reports no anomalies; focus shifts to application servers.
10:45 AM: Application logs indicate a spike in database query times; database team is engaged.
11:00 AM: Database queries are analyzed; a specific query is identified as the culprit.
11:15 AM: Misleading investigation into potential DDoS attack, which is ruled out.
11:30 AM: Query optimization attempts begin; development team is notified for immediate assistance.
12:00 PM: Optimized query is deployed, and performance starts to improve.
12:30 PM: All services return to normal; monitoring confirms stability.
Root Cause and Resolution
Root Cause:
The issue was caused by a poorly optimized database query introduced in a recent update. The query did not utilize indexes properly, leading to full table scans that significantly increased CPU and memory usage on the database server. This, in turn, caused slow response times and server errors across the web and mobile platforms.

Resolution:
To resolve the issue, the problematic query was optimized by:

Adding appropriate indexes to the database table.
Refactoring the query to reduce complexity and improve execution time.
After these changes were implemented, the query performance improved dramatically, reducing CPU and memory load on the database server. Normal service resumed once the optimized query was deployed.

Corrective and Preventative Measures
Improvements/Fixes:

Enhance database query review process before deploying updates.
Implement more comprehensive database performance monitoring.
Increase capacity planning to handle unexpected spikes in database load.
Tasks:

Patch Nginx server: Update to the latest version to ensure optimal performance and security.
Add monitoring on server memory: Implement alerts for high memory usage on the database server.
Refactor database queries: Audit and optimize existing queries to prevent similar issues.
Training for developers: Conduct regular training sessions on writing efficient database queries and performance optimization.
Review and update SLA: Ensure that service level agreements reflect current performance and reliability standards.
Automated testing: Enhance automated tests to include performance benchmarks for critical database queries.
Backup and recovery drills: Regularly conduct drills to ensure the team is prepared for quick recovery in case of database issues.
By addressing these areas, we aim to improve system reliability and prevent similar incidents in the future. The lessons learned from this incident will guide our ongoing efforts to enhance the stability and performance of our services.

