# Postmortem

## Issue Summary
**Duration of the outage:**  
Start: June 10, 2024, 3:00 PM WAT  
End: June 10, 2024, 4:30 PM WAT

**Impact:**  
The main website was down, causing users to see a `500 Internal Server Error` page. Approximately 70% of users were affected, as the outage primarily impacted users accessing the site from Europe and Africa.

**Root Cause:**  
A configuration error in the Nginx server caused a critical system file to be misread, leading to the server being unable to process requests correctly.

## Timeline

- **3:00 PM WAT:** Issue detected by an automated monitoring system alert.
- **3:05 PM WAT:** Alert received by the on-call engineer via SMS and email.
- **3:10 PM WAT:** On-call engineer started investigating the issue, checking server logs and running diagnostic commands.
- **3:20 PM WAT:** Initial assumption was a spike in traffic causing resource exhaustion.
- **3:30 PM WAT:** Misleading path: Engineer restarted the server to clear potential memory leaks but the issue persisted.
- **3:40 PM WAT:** Issue escalated to the DevOps team for further investigation.
- **4:00 PM WAT:** DevOps team discovered a recent configuration change in the Nginx server that caused a syntax error in the configuration file.
- **4:10 PM WAT:** Correct configuration applied and Nginx server restarted.
- **4:15 PM WAT:** Confirmed website was back online.
- **4:30 PM WAT:** Monitoring system confirmed that the website was stable and functioning normally.

## Root Cause and Resolution

**Root Cause:**  
A recent deployment included an incorrect configuration in the Nginx server. The configuration file had a misplaced semicolon which caused the server to fail to load properly, leading to the `500 Internal Server Error`.

**Resolution:**  
The configuration file was corrected by removing the misplaced semicolon. The Nginx server was then restarted, and the system began processing requests normally. The issue was verified as resolved by running multiple tests to ensure the server was stable.

## Corrective and Preventative Measures

**Improvements/Fixes:**
- Implement a stricter code review process for configuration changes to catch syntax errors.
- Enhance the automated testing suite to include syntax validation for configuration files.

**Specific Tasks:**
- **Patch Nginx Configuration:**
  - Correct the misplaced semicolon in the Nginx configuration file.
- **Add Configuration Syntax Checks:**
  - Implement automated syntax checking tools for configuration files in the CI/CD pipeline.
- **Improve Monitoring Alerts:**
  - Enhance monitoring alerts to include detailed error messages for quicker diagnosis.
- **Conduct Training:**
  - Provide additional training for engineers on proper configuration management and error detection.
