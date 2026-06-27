# CI/CD Demo — Automated Reporting Pipeline with GitHub Actions

![CI](https://github.com/Nib123-lab/ci-cd-demo/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A hands-on project demonstrating **Continuous Integration & Continuous Deployment (CI/CD)** practices using **GitHub Actions**. The project automates code build/test on every push and generates a weekly analytics CSV report on a schedule — showcasing scheduled jobs, artifact uploads, and pipeline automation.

---

##  Overview

This repository implements two automated GitHub Actions workflows:

1. **Continuous Integration (CI)** — Triggers on every push and pull request to the `main` branch, running build and test steps.
2. **Weekly Report Generator** — A scheduled job that runs every Monday at 9:00 AM UTC, generates a CSV analytics report using a Python script, and uploads it as a downloadable artifact.

The project demonstrates real-world DevOps concepts such as workflow automation, cron-based scheduling, artifact management, and pipeline status reporting.

---

##  Features

-  **Automated CI Pipeline** — Build and test stages triggered on every push and pull request.
-  **Scheduled Workflow** — Runs automatically every Monday at 9 AM UTC using cron syntax.
-  **Python Report Generation** — Generates a weekly CSV report with simulated visitor and signup analytics.
-  **Artifact Upload** — Reports are stored as downloadable artifacts with 30-day retention.
-  **Manual Trigger Support** — Workflows can also be triggered manually via `workflow_dispatch`.
-  **Python 3.12 Environment** — Uses the latest stable Python in the runner.

---

##  Tech Stack

| Category | Technology |
|----------|------------|
| **CI/CD Platform** | GitHub Actions |
| **Language** | Python 3.12 |
| **Runner** | Ubuntu Latest |
| **Version Control** | Git & GitHub |
| **Format** | YAML (workflows), CSV (output) |

---

##  Project Structure

```
ci-cd-demo/
│
├── .github/
│   └── workflows/
│       ├── ci.yml                 # CI pipeline (build & test)
│       └── weekly-report.yml      # Scheduled weekly report workflow
│
├── generate_report.py             # Python script to generate CSV reports
└── README.md                      # Project documentation
```

---

##  How It Works

### 1. CI Workflow (`ci.yml`)
Runs automatically on every push to `main` or on pull requests:
- Checks out the code
- Runs the build step
- Runs the test step

### 2. Weekly Report Workflow (`weekly-report.yml`)
Runs every **Monday at 9:00 AM UTC** (or manually on demand):
- Sets up Python 3.12
- Executes `generate_report.py`
- Generates a CSV file with 7 days of simulated analytics data (visitors & signups)
- Uploads the CSV as a downloadable artifact for 30 days

### 3. Report Generator (`generate_report.py`)
A small Python script that:
- Creates a 7-day rolling analytics report
- Outputs columns: `day`, `visitors`, `signups`
- Saves the file as `weekly_report_YYYY-MM-DD.csv`

---

##  Getting Started

### Run Locally

Clone the repository and run the script:

```bash
git clone https://github.com/Nib123-lab/ci-cd-demo.git
cd ci-cd-demo
python generate_report.py
```

A CSV file named `weekly_report_<today>.csv` will be generated in your current directory.

### Trigger the Workflow Manually
1. Go to the **Actions** tab in this repository.
2. Select the workflow you want to run (`CI` or `Weekly Report`).
3. Click **Run workflow**.

### Download a Generated Report
1. Open the **Actions** tab.
2. Click on a completed `Weekly Report` run.
3. Scroll to the **Artifacts** section and download `weekly-report`.

---

##  Sample Output

A snippet of the generated CSV:

| day | visitors | signups |
|-----|----------|---------|
| 2026-06-14 | 215 | 18 |
| 2026-06-15 | 187 | 12 |
| 2026-06-16 | 264 | 29 |
| 2026-06-17 | 142 | 7 |

---

## 🎯 What I Learned

Building this project helped me understand:
- Writing and configuring GitHub Actions workflows in YAML
- Using cron expressions for scheduled jobs
- Managing build artifacts in CI/CD pipelines
- Setting up Python environments in CI runners
- Real-world Git workflows (branching, pull requests, automated checks)

---

##  Future Improvements

- Add unit tests for `generate_report.py` using `pytest`
- Integrate notifications (email/Slack) on workflow completion
- Deploy the generated reports to a static hosting service (e.g., GitHub Pages)
- Add code quality checks (linting with `flake8`, formatting with `black`)
- Containerize the script using Docker

---

##  Author

**Nibha**  
 GitHub: [@Nib123-lab](https://github.com/Nib123-lab)

---

