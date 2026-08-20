---
title: Xcode Unit Testing Guide
apple_id: TP40002143
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/UnitTesting/05-Running_Unit_Tests/running.html
archived_at: '2026-07-15T07:27:06.938638Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Unit Testing Guide](About%20Unit%20Testing.md)


[Next](Writing%20Testable%20Code.md)[Previous](Configuring%20a%20Scheme%20to%20Run%20Unit%20Tests.md)

# Running Unit Tests

To ensure that changes you make to your code don’t alter its correct behavior, you should run your test suites periodically, especially after making significant changes. This chapter explains how to run unit tests.

You run unit tests by executing the Test command on a scheme whose Test action identifies one or more unit-test targets.

To run unit tests:

1. From the Scheme toolbar menu, choose the scheme that incorporates the unit-test targets you want to use in its Test action (see [Configuring a Scheme to Run Unit Tests](Configuring%20a%20Scheme%20to%20Run%20Unit%20Tests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbtfvbuqnjnknltc)), and the run destination.
2. Choose Product > Test.

   If one or more tests cases fail, they are listed in the issue navigator (View > Navigators > Show Issue Navigator).
3. To view the transcript of your unit-test run, choose View > Navigators > Show Log Navigator, and select the first test action listed in the log navigator.

   The log viewer shows the log of the unit-test run, as shown in Figure 5-1.

   __Figure 5-1__  Log of an application unit-test run

   !!

[Next](Writing%20Testable%20Code.md)[Previous](Configuring%20a%20Scheme%20to%20Run%20Unit%20Tests.md)

