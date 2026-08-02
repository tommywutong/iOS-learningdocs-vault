---
title: Xcode Unit Testing Guide
apple_id: TP40002143
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/UnitTesting/00-About_Unit_Testing/about.html
archived_at: '2026-07-15T07:26:59.918163Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Unit-Testing%20Overview.md)

# About Unit Testing

Unit-testing is a way to ensure that the code you write adheres to design specifications and that it keeps adhering to those specifications as you modify it. Unit-testing helps you write robust and secure apps. The essential component of unit-testing is a test case, which tests your code at the lowest testable level, or _unit_.

This document describes how to create products with unit-testing in mind and how to incorporate unit-testing into existing projects.

The content in this document is written for:

- Xcode 4.2
- iOS SDK 5.0
- OS X SDK 10.7

### Incorporate Unit-Testing in a Project

To unit-test your code, your project must include unit-test bundles. These bundles contain the test case methods that exercise code in a library or an app to ensure that it behaves correctly.

### Write Test Cases

A test case method calls a unit of code (one or several methods or functions) to ensure that it behaves in the manner expected by the test case, such as returning specific values or throwing an exception. A test case method reports whether the test case passed or failed.

### Run Unit Tests

Run unit tests to ensure that code you’ve just written or modified behaves as expected.

You should be familiar with app design and programming concepts. You should also understand the workflow described in _App Distribution Guide_.

[Next](Unit-Testing%20Overview.md)

