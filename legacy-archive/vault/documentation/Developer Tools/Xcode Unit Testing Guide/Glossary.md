---
title: Xcode Unit Testing Guide
apple_id: TP40002143
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/UnitTesting/08-Glossary/glossary.html
archived_at: '2026-07-15T07:27:07.329279Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Unit Testing Guide](About%20Unit%20Testing.md)


[Next](Document%20Revision%20History.md)[Previous](Unit-Test%20Result%20Macro%20Reference.md)

# Glossary

- __application unit tests__

  Unit tests that test the operation of code in a running app. These tests can ensure that an app’s data model, user-interface elements, and controllers are connected correctly and interact as expected. However, application unit tests are not user-interface tests. Application unit tests do not directly manipulate user-interface elements, and the running app does not initiate a run loop.

- __logic unit test__

  Unit tests that test the operation of code in isolation. These tests ensure that units of code (a single procedure or a set of related procedures) behave as expected.

- __run destination__

  The simulator, device, or architecture on which Xcode runs a product runs after builds it:

  - __iOS:__ The run destination can be a simulator or an iOS device.
  - __Mac:__ The run destination is your Mac device, in the 64-bit or 32-bit architectures.

- __test case__

  A set of criteria that determines whether one or more procedures function correctly. See _test case method_.

- __test case method__

  An Objective-C method that calls one or more procedures to test the correct operation of the unit. When the unit behaves incorrectly, the test case fails. When a test case fails, it calls a test result macro to report the failure.

- __test suite__

  A `SenTestCase` subclass. A test suite contains one or more test cases. See _test case_.

[Next](Document%20Revision%20History.md)[Previous](Unit-Test%20Result%20Macro%20Reference.md)

