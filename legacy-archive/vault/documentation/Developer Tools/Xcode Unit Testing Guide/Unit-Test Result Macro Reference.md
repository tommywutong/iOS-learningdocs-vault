---
title: Xcode Unit Testing Guide
apple_id: TP40002143
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/UnitTesting/AB-Unit-Test_Result_Macro_Reference/result_macro_reference.html
archived_at: '2026-07-15T07:27:07.345386Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Unit Testing Guide](About%20Unit%20Testing.md)


[Next](Glossary.md)[Previous](Writing%20Testable%20Code.md)

# Unit-Test Result Macro Reference

The SenTestingKit framework defines a set of test case result macros that report test case results to the framework. When a test fails, the framework sends a test-failure message, which Xcode displays in the log and issue navigators.

The following sections describe the test result macros you can use in your test case methods. These macros are declared in `SenTestCase.h`.

Fails the test case.

```
STFail(failure_description, ...)
```

__Parameters__

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

Fails the test case when two objects are different.

```
STAssertEqualObjects(object_1, object_2, failure_description, ...)
```

__Parameters__

`object_1`

- An object.

`object_2`

- An object.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

__Detail__

The test fails when `[object_1 isEqualTo:object_2]` is false.

Fails the test case when two values are different.

```
STAssertEquals(value_1, value_2, failure_description, ...)
```

__Parameters__

`value_1`

- A scalar, structure, or union.

`value_2`

- A scalar, structure, or union.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

__Detail__

The test fails when `value_1` is not equal to `value_2`.

Fails the test case when the difference between two values is greater than a given value.

```
STAssertEqualsWithAccuracy(value_1, value_2, accuracy, failure_description, ...)
```

__Parameters__

`value_1`

- An integer or a floating-point value.

`value_2`

- An integer or a floating-point value.

`accuracy`

- An integer or a floating-point value.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

__Detail__

The test fails when the difference between `value_1` and `value_2` is greater than `accuracy`.

Fails the test case when a given expression is not nil.

```
STAssertNil(expression, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

Fails the test case when a given expression is nil.

```
STAssertNotNil(expression, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

Fails the test case when a given expression is false.

```
STAssertTrue(expression, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

Fails the test case when a given expression is true.

```
STAssertFalse(expression, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

Fails the test case when an expression doesn’t raise an exception.

```
STAssertThrows(expression, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

Fails the test case when an expression doesn’t raise an exception of a particular class.

```
STAssertThrowsSpecific(expression, exception_class, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`exception_class`

- An exception class.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

__Detail__

The test fails when `expression` doesn’t raise an exception of the class `exception_class`.

Fails the test case when an expression doesn’t raise an exception of a particular class with a given name.

```
STAssertThrowsSpecificNamed(expression, exception_class, exception_name, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`exception_class`

- An exception class.

`exception_name`

- A string with the name of an exception.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

__Detail__

The test fails when `expression` doesn’t raise an exception of the class `exception_class` with the name `exception_name`.

Fails the test case when an expression raises an exception.

```
STAssertNoThrow(expression, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

Fails the test case when an expression raises an exception of a particular class.

```
STAssertNoThrowSpecific(expression, exception_class, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`exception_class`

- An exception class.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

__Detail__

The test fails when `expression` raises an exception of the class `exception_class`.

Fails the test case when an expression doesn’t raise an exception of a particular class with a given name.

```
STAssertNoThrowSpecificNamed(expression, exception_class, exception_name, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`exception_class`

- An exception class.

`exception_name`

- A string with the name of an exception.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

__Detail__

The test fails when the `expression` raises an exception of the class `exception_class` with the name `exception_name`.

Fails the test case when an expression is false or raises an exception.

```
STAssertTrueNoThrow(expression, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

Fails the test case when an expression is true or raises an exception.

```
STAssertFalseNoThrow(expression, failure_description, ...)
```

__Parameters__

`expression`

- Expression to test.

`failure_description`

- Format string specifying error message. Can be `nil`.

`...`

- (Optional) A comma-separated list of arguments to substitute into `failure_description`.

[Next](Glossary.md)[Previous](Writing%20Testable%20Code.md)

