# UI Automation Framework (Selenium + Pytest)

This project is a UI automation testing framework built using Selenium WebDriver and Pytest.
It follows the Page Object Model (POM) design pattern and is designed for practicing and
demonstrating modern UI automation techniques.

## Tech Stack
- Python 3.13
- Selenium WebDriver
- Pytest
- Pytest-HTML (for reports)
- Chrome WebDriver

## Project Structure
learnqaweb/
│
├── Base/ # Base classes (driver, waits, actions)
├── Pages/ # Page Object Model
│ └── Dashboard/
├── TestCase/ # Test cases
├── Reports/ # HTML test reports
├── conftest.py # Pytest fixtures & configuration
└── README.md

## Features Implemented
- Page Object Model (POM)
- Explicit waits using Expected Conditions
- Assertions for UI validation
- Drag and Drop automation
- Dynamic elements handling
- AJAX content validation
- Infinite scrolling
- iFrames and nested iFrames
- Window handling
- Keyboard and mouse interactions
- Shadow DOM interaction

## How to Run Tests

1. Clone the repository:
```bash
git clone https://github.com/your-username/ui-automation-framework.git
```
2. pip install -r requirements.txt
3. pytest -vs --browser chrome


## Reports
HTML reports are generated after test execution and stored in the `Reports/` directory.

## Logging & Screenshots
- Basic logging knowledge acquired
- Logging and automatic screenshots on test failure are planned improvements
