---
title: Xcode Unit Testing Guide
apple_id: TP40002143
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/UnitTesting/03-Writing_Test_Case_Methods/writing_tests.html
archived_at: '2026-07-15T07:27:05.442910Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Unit Testing Guide](About%20Unit%20Testing.md)


[Next](Configuring%20a%20Scheme%20to%20Run%20Unit%20Tests.md)[Previous](Setting%20Up%20Unit-Testing%20in%20a%20Project.md)

# Writing Test Case Methods

You add test cases to a test suite by adding test case methods to a test suite class. A _test case method_ is an instance method of a test suite class that’s named `test...`, with no parameters, and whose return type is `void`. A test case method calls the code being tested (known as the _unit_), and reports whether the calls produced the expected result—for example, whether they return the anticipated value or raise an appropriate exception. Test case methods use a set of macros to check for the expected conditions and report their findings. [Unit-Test Result Macro Reference](Unit-Test%20Result%20Macro%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbtfvbuqojnknltc) describes these macros.

For a test case method to access the unit to be tested, you have to add the appropriate implementation files to the unit test target and import the corresponding header files into your test suite class. For an example of a project that uses unit tests, see the _[Unit Testing Apps and Frameworks](../../../samplecode/Unit%20Testing%20Apps%20and%20Frameworks/Unit%20Testing%20Apps%20and%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcnzugi)_ sample-code project.

This is the structure of a test case method:

```objc
- (void)test<test_case_name> {
   ...     // Set up, call test-case subject API.
   ST...   // Report pass/fail to testing framework.
   ...     // Tear down.
}
```

When Xcode runs unit tests, it invokes each test case method independently. Therefore, each method must prepare and clean up any auxiliary variables, structures, and objects it needs to interact with the subject API. Conveniently, you can add a pair of methods to a test suite class that are called before and after each test case method is invoked: `setUp` and `tearDown`. Just like test case methods, the type of both methods is `void` and they take no arguments.

This is an example of a `setUp/tearDown` method pair:

```objc
- (void)setUp {
   test_subject = [[[MyClass alloc] init] retain];
   STAssertNotNil(test_subject, @"Could not create test subject.");
}

- (void)tearDown {
   [test_subject release];
}
```

[Next](Configuring%20a%20Scheme%20to%20Run%20Unit%20Tests.md)[Previous](Setting%20Up%20Unit-Testing%20in%20a%20Project.md)

