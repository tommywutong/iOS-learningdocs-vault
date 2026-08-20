---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/UnitTesting.html
archived_at: '2026-07-27T06:57:08.162904Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](ContinuousIntegrationTesting.md)[Previous](CustomizingYourWorkflow.md)

## Using Unit Tests

Xcode supports three main types of testing. _Functional tests_ focus on code functionality. _Performance tests_ focus on measuring execution time. _User Interface tests_ focus on flows through the user interface. Functional and performances tests are functions that you write. Each function sets up an environment for the test, executes the targeted parts of the app, and tears down the test environment. User interface tests are recordings you make as you use your app.

The most common type of functional testing is unit testing. A _unit_ of code is the smallest testable component of your project—for example, a method in a class or a set of methods that accomplish an essential purpose. Unit tests are often used to detect regressions introduced by code changes to a project. Some developers write unit tests first and then implement methods that pass the tests.

Performance tests measure the time it takes your app to complete a task on different types of devices. Xcode tracks times for different configurations and you choose baselines from measured values.

A _test case_ exercises a unit of code in a specific way or measures a specific part of your app’s performance; if the result of the test is different from the expected result, the test case fails. A _test suite_ is made up of a set of test cases.

When you create a project or a target, Xcode includes a unit test target in the scheme that builds the app. The implementation file for the target includes stubs for the `setUp`, `tearDown`, and `testExample` methods. Complete these stub implementations and add other code as necessary to perform unit tests on your app.

Run all tests by choosing Product > Test. Click the Test Navigator icon to view the status and results of the tests. You can add a test target to a project (or add a class to a test) by clicking the Add button (+) in the bottom-left corner of the test navigator. To view the source code for a particular test, select it from the test list. The file opens in the source code editor.

（原归档配图获取待重试：`XC_O_about_test_navigator_2x.png`）

To run a test suite, click the arrow to the right of the name. To run a subset of test methods, select them in the test navigator and choose Product > Perform Action > Run Test Methods. To run an individual test method, click the arrow to the right of the method name. Choose Product > Test to run all tests in the active scheme.

When a test succeeds, a green diamond with a checkmark denoting success appears to the right of the test name. When a test fails, a red diamond with an X denoting failure appears to the right of the test name and the issue is displayed in the issue navigator. To see the issue, click the Issue Navigator button (（原归档配图未能恢复：`XG_NavArea_Issue_icon_2x.png`）) in the navigator bar.

To view only the failed tests, click the Failed Test button (（原归档配图获取待重试：`FailedTestIcon_2x.png`）) at the bottom of the test navigator. Select a failed method to examine it in the source code editor. After addressing the reason for the failure, click the failed test indicator (a red diamond with an X) to rerun the test.

Show related test methods in an assistant editor by choosing either the Test Classes or Test Callers category from the Assistant pop-up menu.

For more detail on writing, running, and viewing tests, see _[Testing with Xcode](../../Developer%20Tools/Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_.

[Customizing Your Workflow](CustomizingYourWorkflow.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrsfvjvomi)

[Using Continuous Integration Testing](ContinuousIntegrationTesting.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrufvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](ContinuousIntegrationTesting.md)[Previous](CustomizingYourWorkflow.md)
