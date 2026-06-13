## DevSecOps Framework: Design and Implementation

### Overview

We adopted industry-standard DevSecOps practices to secure the development lifecycle of 12+ applications on AWS. Security tooling (SAST, DAST, SCA) and container scanning were integrated into a standardized TeamCity CI/CD pipeline, with least-privilege IAM controls governing all automated actions.

#### Static Application Security Testing (SAST), Dynamic Application Security Testing (DAST), and Software Composition Analysis (SCA)

- **SAST**: Code commits and pull requests are scanned before merging. Critical findings are reported to a central SonarQube instance and surfaced in TeamCity for acknowledgment and remediation gating.
- **DAST**: Runtime vulnerability scans are executed in isolated test environments after the application is deployed. Critical issues that would block promotion to higher environments are identified early.
- **SCA**: Snyk is integrated to analyze package manifests, construct dependency trees, and compare library versions against a vulnerability database. Vulnerable components are flagged before build completion.

### Container Security Scanning

Container images are scanned for embedded secrets and operating-system-level vulnerabilities. This eliminates accidental credential leakage and reduces the host-level attack surface before images are promoted.

### CI/CD Pipeline Orchestration with TeamCity

TeamCity acts as the central orchestrator and applies a single reusable pipeline template across all 12+ applications. The enforced flow is:

- Developer commits code and raises a pull request.
- Automated SAST and SCA scans execute on the PR and build.
- If any critical issues are detected, the build fails and the code cannot proceed.
- On success, the pipeline builds the container image, pushes it to Amazon Elastic Container Registry (ECR), and deploys it to the target Amazon Elastic Kubernetes Service (EKS) cluster.

TeamCity executes a parameterized Bash script that accepts inputs such as IAM role ARN, ECR repository name, and EKS cluster name. The script authenticates, pulls the required base image if needed, runs tests in the real environment, and performs the deployment.

### Identity and Access Management (IAM)

Least-privilege IAM roles and trust policies were created specifically for the TeamCity service account. These roles grant only the permissions required to interact with ECR and EKS, ensuring the pipeline can perform its intended actions without excessive privileges.