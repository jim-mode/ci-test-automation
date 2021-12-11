# CI for Test Automation

## Overview
Sandbox project to explore the capability of QA Automation via CI Pipeline

### Github Actions
[![Main pytest CI](https://github.com/jim-mode/ci-test-automation/actions/workflows/github-actions-ci.yml/badge.svg)](https://github.com/jim-mode/ci-test-automation/actions/workflows/github-actions-ci.yml)

### CircleCI
[![FuzzyIO](https://circleci.com/gh/jim-mode/ci-test-automation.svg?style=svg)](https://app.circleci.com/pipelines/github/jim-mode/ci-test-automation)

### Install packages
```
pip install -r requirements.txt
```

### pytest commands
```
pytest
pytest hello_test.py

# Run tests by keyword expressions
pytest hello_test.py -k test_capitalize_string_01

# Run a single test function
pytest hello_test.py::test_capitalize_string_01

# Run a specific test within a module:
pytest hello_test.py::TestCap::test_capitalize_string_02

# Run tests by marker expressions
pytest -m fruits
pytest -m "not fruits"

# html output
pytest --html=test_result_report.html --self-contained-html
```
### allure commands
```
pytest --alluredir=test_result_alluredir

allure generate test_result_alluredir --clean
```