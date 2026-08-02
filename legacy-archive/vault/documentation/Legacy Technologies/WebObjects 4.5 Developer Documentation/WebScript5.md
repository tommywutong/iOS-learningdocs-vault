---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript5.html
archived_at: '2026-07-15T08:06:35.778000Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript4.md)

### Assigning Values to Variables

You assign values to variables using the following syntax:

```
myVar = aValue;
```


A value can be assigned to a variable at the time it is declared or after it is declared. For example:

```
NSNumber *myVar1;
id myVar2 = 77;

myVar1 = 76;
```


The value you assign to a variable can be either a constant or another variable. For example:

```
// assign another variable to a variable
myVar = anotherVar;
// assign a string constant to a variable
myString = @"This is my string.";
```


__Note:__  The // syntax denotes a comment.
You can assign constant values to objects of four of the most commonly used classes in WebScript: NSNumber, NSString, NSArray, and NSDictionary. These classes are defined in the Foundation framework. To learn how to initialize objects of all other classes, see ["Creating Instances of Classes"](WebScript10.md#apple-gq4dgni) in this chapter.

NSNumber is the easiest class to initialize. You just assign a number to the variable, like this:

```
NSNumber *myNumber = 77;
```


For the remaining three classes, WebScript provides a convenient syntax for initializing constant objects. In such an assignment statement, the value you're assigning to the constant object is preceded by an at sign (@). You use parentheses to enclose the elements of an NSArray and curly braces to enclose the key-value pairs of an NSDictionary. The following are examples of how you use this syntax to assign values to constant NSString, NSArray, and NSDictionary objects in WebScript:

```
myString = @"hello world";
myArray = @("hello", "goodbye");
myDictionary = @{"key" = 16};
anotherArray = @(1, 2, 3, "hello");
aDict = @{ "a" = 1; "b" = "hello world"; "c" = (1,2,3);
        "d" = { "x" = 1; "r" = 2 }};
```


The following rules apply when you use this syntax to create constant objects:

- The value you assign must be a constant (that is, it can't include variables). For example, the following is not allowed:

```
    // This is not allowed!!
    myArray = @("hello", aVariable);
```

- You shouldn't use @ to identify an NSString, NSArray, or NSDictionary inside the value being assigned. For example:

```
    // This is not allowed!!
    myDictionary = @(@"value" = 3);

    // Do this instead
    myDictionary = @("value" = 3);
```


For more information on NSNumber, NSString, NSDictionary, and NSArray, see the chapter ["WebScript Programmer's Quick Reference to Foundation Classes"](WebScript%20Programmer%27s%20Quick%20Reference%20to%20Foundation%20Classes.md#apple-gu3dsnq).

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript6.md)
