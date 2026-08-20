---
title: Xcode Unit Testing Guide
apple_id: TP40002143
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/UnitTesting/AA-Writing_Testable_Code/writing_code.html
archived_at: '2026-07-15T07:27:07.340351Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Unit Testing Guide](About%20Unit%20Testing.md)


[Next](Unit-Test%20Result%20Macro%20Reference.md)[Previous](Running%20Unit%20Tests.md)

# Writing Testable Code

The Xcode integrated support for unit-testing makes it possible for you to build test suites to support your development efforts in any way you want. You can use unit-testing in Xcode to detect potential regressions in your code or to validate the behavior of your app. This testing can improve the stability of your code by ensuring that units behave in the expected ways.

Of course, the level of stability you achieve through unit-testing is highly dependent on the quality of the test cases you write. Follow these guidelines as you write code, to ensure that it’s easily testable:

- __Define API requirements.__ You should define requirements and outcomes for each method or function that you add to your project. These requirements should include input and output ranges, exceptions thrown and the conditions under which they are raised, and the type of values returned (especially if the values are instances of classes). Specifying requirements and making sure that requirements are met in your code help you write robust, secure code.

  See the _[Unit Testing Apps and Frameworks](../../../samplecode/Unit%20Testing%20Apps%20and%20Frameworks/Unit%20Testing%20Apps%20and%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcnzugi)_ sample-code project for an example of using exceptions to identify and report incorrect library usage by client code.
- __Write test cases as you write code.__ As you design and write each method or function, write one or more test cases that ensure that the API’s requirements are met. It’s harder to write unit tests for existing code than for code you are writing.
- __Check boundary conditions.__ If a parameter of a method must have values in a specific range, your tests should pass values that include the lowest and highest values of the range. For example, if a procedure has an integer parameter can have values between 0 and 100, inclusive, the test code for that method should pass the values 0, 50, and 100 for the parameter.
- __Use negative tests.__ Negative tests ensure that your code responds to error conditions appropriately. Verify that your code behaves correctly when it receives invalid or unexpected input values. Also verify that it returns error codes or raises exceptions when it should. For example, if an integer parameter must have values in the range 0 to 100, inclusive, you should create test cases that pass the values -1 and 101 to ensure that the procedure raises an exception or returns an error code.
- __Write comprehensive test cases.__ Comprehensive tests combine different code modules to implement some of the more complex behavior of your API. While simple, isolated tests provide value, stacked tests exercise complex behaviors and tend to catch many more problems. These kinds of tests mimic the behavior of your code under more realistic conditions. For example, in addition to adding objects to an array, you could create the array, add several objects to it, remove a few of them using different methods, and then ensure that the set and number of remaining objects is correct.
- __Cover your bug fixes with test cases.__ Whenever you fix a bug, write one or more tests cases that verify the fix.

[Next](Unit-Test%20Result%20Macro%20Reference.md)[Previous](Running%20Unit%20Tests.md)

