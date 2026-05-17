## Cloud Security Posture Management (CSPM)

Cloud infrastructure has become the default platform for developing and operating modern services. As adoption accelerates, the attack surface grows—primarily because of misconfigurations.

### What Is a Cloud Misconfiguration?

A cloud misconfiguration is any incorrect or suboptimal setting in your cloud environment (IAM permissions, storage buckets, network rules, etc.) introduced during provisioning, deployment, or ongoing operations. These issues expose resources to unauthorized access, data breaches, or compliance violations.

### What Is CSPM?

Cloud Security Posture Management (CSPM) is the continuous practice of discovering, assessing, prioritizing, and remediating misconfigurations across multi-cloud and hybrid environments. It operates within the shared responsibility model: the cloud provider secures the underlying infrastructure, while the customer remains responsible for securely configuring resources and data.

### Core Capabilities

CSPM platforms deliver three essential functions:

- #### Centralized Visibility
    A single pane of glass to inventory, monitor, and map all cloud assets, configurations, and relationships across providers.

- #### Automated Remediation
    Policy-driven workflows that automatically detect drifts and apply fixes (or suggest them), reducing mean time to resolution and human error.

- #### Compliance Management
    Continuous assessment and reporting against industry and regulatory frameworks (NIST, PCI-DSS, CIS Benchmarks, SOC 2, etc.) with evidence collection and audit-ready artifacts.

### Cloud Misconfigurations and CSPM

Cloud misconfigurations are the leading cause of cloud security incidents. They typically result from human error, use of default settings, and inadequate governance. CSPM (Cloud Security Posture Management) continuously discovers, assesses, and remediates these issues across multi-cloud environments.

#### Common Cloud Misconfigurations

- #### Missing or unenforced Multi-Factor Authentication (MFA)
    Without mandatory MFA, accounts are vulnerable to credential-stuffing and phishing attacks, weakening identity and access management.
- #### Overly permissive network rules
    Security groups, network ACLs, or firewalls with unrestricted inbound/outbound traffic (especially open ports or protocols) enable data exfiltration, lateral movement, and unauthorized access.
- #### Over-permissive IAM policies
    Roles or policies that grant broad read/write permissions beyond the principle of least privilege allow unintended access to resources and increase blast radius during compromise.
- #### Publicly exposed storage
    Cloud storage buckets, databases, or file shares left accessible over the public internet risk data leakage, unauthorized modification, or injection attacks.
- #### Inadequate logging and monitoring
    Absence of centralized logging, real-time alerts, or audit trails prevents timely detection and forensic analysis of suspicious activity.

#### What CSPM Delivers

CSPM platforms provide continuous visibility and automated governance of cloud posture. 

#### Core capabilities include:

1. #### Asset discovery and inventory
    Automatically maps all cloud resources, APIs, configurations, and dependencies across accounts and regions.
2. #### Configuration assessment
    Continuously evaluates resources against security frameworks, compliance standards (CIS, NIST, PCI-DSS, etc.), and best-practice benchmarks.
3. #### Risk identification and prioritization
    Detects misconfigurations, calculates risk using CVSS scoring and contextual factors, and surfaces exploitable issues.
4. #### Remediation and hardening
    Recommends or automates fixes, enforces policy-as-code, and prevents drift from secure baselines.
5. #### Real-time threat detection and compliance
    Monitors for anomalous behavior, provides audit-ready evidence, and maintains continuous compliance posture.

### Cloud-Native vs Third-Party CSPM Solutions

#### Cloud-Native CSPM Solutions

These tools are developed and deeply integrated by the cloud service provider (CSP) into its own infrastructure. They leverage native APIs, logging, and identity systems for seamless visibility and control with minimal setup.

Popular examples include:

- **AWS Security Hub** – aggregates security findings and compliance checks across AWS accounts.
- **Microsoft Defender for Cloud** – provides posture management, threat protection, and compliance for Azure (and hybrid) workloads.
- **Google Cloud Security Command Center** – offers asset inventory, vulnerability detection, and compliance reporting within GCP.

#### Third-Party CSPM Solutions

These platforms are built by independent security companies and integrate with multiple cloud providers through APIs and agents. They typically offer broader multi-cloud support, advanced analytics, and features that extend beyond native capabilities.

Popular examples include:

P- **risma Cloud (Palo Alto Networks)** – comprehensive CNAPP platform with strong CSPM, compliance, and IaC scanning.
- **Falcon Cloud Security (CrowdStrike)** – focuses on real-time threat detection and posture management across clouds.
- **Wiz** – graph-based cloud security platform known for rapid risk prioritization and agentless scanning.

## AWS Security Hub

AWS Security Hub is CSPM (Cloud Security Posture Management) service, provides a centralised view of cloud security state. Security Hub aggregate findings from various aws services (such as Amazon GuardDuty, AWS Config, AWS Inspector, IAM Access Analyzer etc), third-party tools, and native compliance checks. 

## Key Capabilities

- Aggregates findings across accounts, Regions, and resources into a single console.
- Runs contineous security checks against best security practices and compliance standards. 
- Lay out security scores and surface trends for security prioritization and remediation.

## Getting Started and Prerequisites

Enable AWS Security Hub in the desired region. 

For most control findings and compliance assessment to work, you must also enable AWS Config in each Region with resource recording turned on for the relevant resource types. (Security Hub includes a built-in control, Config.1, that flags missing Config configuration.)

After enabling Security Hub, activate the security standards you need. Supported standards include:

- AWS Foundational Security Best Practices (FSBP)
- CIS AWS Foundations Benchmark
- PCI DSS
- NIST SP 800-53
- HIPAA (and others)

Activating a standard automatically enables its associated controls.

## Console Sections

The Security Hub console is organized around three primary views:

- ### Summary Dashboard
    High-level statistics and trends, including:

     - Overall security score and compliance status
     - Findings by severity, standard, Region, and resource
     - Resources with the highest number of findings
     - Most common threat types and exploitable vulnerabilities

- ### Findings

    Detailed, filterable list of all security findings. Each entry shows:

     - Affected resource and account
     - Severity (Critical, High, Medium, Low)
     - Description of the issue or failed check
     - Remediation guidance

- ### Controls

    Consolidated view of every security control across your enabled standards. It displays:

     - Control status (Passed, Failed, or Not Applicable)
     - Number of controls that succeeded or failed per standard
     - Option to enable, disable, or suppress individual controls

