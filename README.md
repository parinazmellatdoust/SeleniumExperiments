# Selenium Automation Framework Portfolio

A robust Python-based UI automation framework demonstrating advanced Selenium skills using the **Page Object Model (POM)** design pattern.

## Project Overview

This framework is designed to demonstrate proficiency in handling modern web application challenges. It targets `www.uitestingplayground.com` to showcase solutions for dynamic locators, AJAX waits, and Shadow DOM interaction.

## Key Features

*   **Design Pattern:** Page Object Model (POM) for maintainable code.
*   **Synchronization:** Explicit Waits (WebDriverWait) for handling dynamic elements and AJAX delays (No hard sleeps).
*   **Data-Driven Testing:** JSON-driven test parameters for Positive and Negative testing.
*   **Advanced Interactions:** JavaScript execution to penetrate Shadow DOM.
*   **Reporting:** HTML report generation.

## Technology Stack

*   **Language:** Python 3.14
*   **Framework:** Pytest
*   **Automation:** Selenium 4
*   **Driver Management:** Webdriver Manager

## Project Structure

```text
SeleniumExperiments/
├── base/              # Base driver and common methods
├── pages/             # Page Object classes
├── testcases/         # Pytest test scripts
├── utilities/         # Custom logging, assertions, JSON loaders
├── testdata/          # JSON data files
├── reports/           # HTML test reports
├── configfiles/       # Configuration files
├── conftest.py        # Pytest fixtures (setup/teardown)
├── pytest.ini         # Pytest configuration
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd SeleniumExperiments
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

*   **Run all tests:**
    ```bash
    pytest testcases/
    ```

*   **Run with HTML Report:**
    ```bash
    pytest testcases/ --html=reports/report.html --self-contained-html
    ```

*   **Run specific categories (Markers):**
    ```bash
    # Run only Positive (Happy Path) tests
    pytest testcases/ -m positive

    # Run only Negative (Sad Path) tests
    pytest testcases/ -m negative
    ```

*   **Run on specific browser:**
    ```bash
    pytest testcases/ --browser edge
    ```

## Test Scenarios Covered

1.  **Dynamic ID:** Handling elements with constantly changing IDs.
2.  **Sample App:** Data-driven Login/Logout flow (Positive & Negative).
3.  **Client Side Delay:** AJAX synchronization and explicit waits.
4.  **Hidden Layers:** Handling DOM overlays and element visibility states.
5.  **Shadow DOM:** Advanced JavaScript interaction with encapsulated elements.