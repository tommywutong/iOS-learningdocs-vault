---
title: Mar 21, 2019 Open-sourcing Python Test Runner for multiple tests in parallel
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2019/03/21/open-source/python-test-runner/'
original_language: en
published: 2019-03-21
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:29aa97d3350ad816'
translated: false
---

> 原文：[Mar 21, 2019 Open-sourcing Python Test Runner for multiple tests in parallel](https://engineering.fb.com/2019/03/21/open-source/python-test-runner/)　·　Meta Engineering — iOS

## WHAT’S NEW:

A new Python-based project called Python Test Runner (`ptr`), that allows developers to run Python unit test suites. The main difference between `ptr` and existing test runners is that `ptr` crawls a repository to find Python projects with unit tests defined in their setup files. It then runs each suite in parallel with configured enabled steps.

## WHY IT MATTERS:

The `ptr` project was created as a way to provide a lightweight tool using standard open source Python components. Supported and tested on Linux, MacOS, and Windows, `ptr` allows developers to test multiple projects in one Python environment and run the tests in parallel.

To achieve this, `ptr` recursively searches for `setup.(cfg|py)` from `BASE_DIR` (-b) and parses the found setup files for `ptr` configuration. If `setup.(cfg|py)` exists with `ptr` configuration, `ptr` runs the tests. When running test suites in parallel, all steps will be run for each suite until failure, and only failed runs will have their output written to `stdout`.

## USE IT FOR:

`ptr` has four main use cases:

- Running a Python test suite
- Optionally checking and enforcing code coverage requirements
- Optionally formatting and linting Python code
- Optionally performing static type analysis

## **GET IT ON GITHUB:**

[ptr on github](https://github.com/facebookincubator/ptr)  
 [ptr on PyPI](https://pypi.org/project/ptr/)
