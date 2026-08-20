---
title: Xcode Unit Testing Guide
apple_id: TP40002143
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/UnitTesting/01-Unit-Test_Overview/overview.html
archived_at: '2026-07-15T07:26:59.925519Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Unit Testing Guide](About%20Unit%20Testing.md)


[Next](Setting%20Up%20Unit-Testing%20in%20a%20Project.md)[Previous](About%20Unit%20Testing.md)

# Unit-Testing Overview

Unit-testing lets you specify behavior that your code must exhibit to ensure that its functionality remains unchanged as you modify it to, for example, make performance improvements or fix bugs. A _unit_ of code is the smallest testable component of your code—for example, a method in a class or a set of methods that accomplish an essential purpose. A _test case_ exercises a unit of code in a specific way; if the result of the test is different from the expected result, the test case fails. A _test suite_ is made up of a set of test cases. You can develop one or more test suites to test different aspects of your code.

Unit tests are the basis of test-driven development, which is a style of writing code in which you write test cases before writing the code to be tested. This development approach lets you codify requirements and edge cases for your code before you get down to writing it. After writing the test cases, you develop your algorithms with the aim of passing your test cases. After your code passes the test cases, you have a foundation upon which you can make improvements to your code, with confidence that any changes to the expected behavior (which would result in bugs in your product) are identified the next time you run the tests.

Even when not using test-driven development, unit tests can help reduce the introduction of bugs in your code. You can incorporate unit-testing in a working app to ensure that future changes don’t modify the app’s behavior. As you fix bugs, you can add test cases that confirm that the bugs are fixed. However, adding unit tests to a project that’s not designed with unit-testing in mind may require redesigning or refactoring parts of the code to make them testable.

The Xcode unit-testing environment is based on the open-source SenTestingKit framework. This framework provides a set of classes and command-line tools that let you design test suites and run them on your code.

Xcode offers two types of unit tests: _logic tests_ and _application tests_.

- __Logic tests.__ These tests check the correct functionality of a unit of code by itself (not in an app). With logic tests you can put together specific test cases to exercise a unit of code. You can also use logic tests to perform stress-testing of your code to ensure that it behaves correctly in extreme situations that are unlikely in a running app. These tests help you produce robust code that works correctly when used in ways that you did not anticipate.
- __Application tests.__ These tests check units of code in the context of your app. You can use application tests to ensure that the connections of your user-interface controls (outlets and actions) remain in place, and that your controls and controller objects work correctly with your object model as you work on your app. You can also use these tests to perform hardware testing, such as getting the location of the device on which your app is running.

[Next](Setting%20Up%20Unit-Testing%20in%20a%20Project.md)[Previous](About%20Unit%20Testing.md)

