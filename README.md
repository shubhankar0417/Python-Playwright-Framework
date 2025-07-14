# Python Playwright Test Automation Framework

This is a scalable and modular test automation framework built using [Microsoft Playwright](https://playwright.dev/python/), `pytest`, and GitHub Actions. It follows the **Page Object Model (POM)** design and supports:

- Structured locators, pages, tests, and utilities
- HTML test reports
- GitHub Actions CI integration
- JSON-based test data support
- Screenshot capture and failure debugging

---

## Project Structure

Python-Playwright-Framework/
│
├── tests/ # Test cases
│ └── test_main.py
│
├── pages/ # Page object model files
│ └── login_page.py
│
├── locators/ # Locator definitions
│ └── login_locators.py
│
├── data/ # Test data (JSON, CSV, etc.)
│ └── test_data.json
│
├── utils/ # Utility scripts and helpers
│ └── data_loader.py
│
├── reports/ # HTML test reports
│
├── .github/workflows/ # GitHub Actions workflow file
│ └── playwright-tests.yml
│
├── conftest.py # Pytest configuration and fixtures
├── requirements.txt # Python dependencies
└── README.


## Running Tests Locally
Run a specific test file with HTML report:
pytest tests/test_main.py --html=reports/report.html --self-contained-html


## Running Tests on GitHub Actions
This repo includes a GitHub Actions workflow (.github/workflows/playwright-tests.yml) that:

Installs Python and dependencies
Installs Playwright browsers
Runs tests
Uploads HTML report as an artifact
Triggered on every push or pull request to main.