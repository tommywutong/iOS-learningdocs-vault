---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/MakingAssignments.html
archived_at: '2026-07-15T07:48:01.905303Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](idDataType.md)

# Making Assignments

The basic syntax for making assignments in WebScript is straightforward:

```
myVar = aValue;
```

The value you assign to a variable can be either a constant or another variable. For example:

```
// assign another variable to a variable
myVar = anotherVar;

// assign a string constant to a variable
myString = @"This is my string.";
```

The syntax `myString = @"This is my string";` is a way of creating instances of the class NSString. For more discussion of this syntax, see the section "[Creating Constant NSStrings, NSArrays, and NSDictionaries](CreatingObjects.md#apple-kjcumnrvha2te)."

WebScript only supports one data type: objects (__id__s). However, if you assign a literal integer or floating point value to a variable:

`id myInt = 167;`

WebScript represents it as an NSNumber object. In this sense WebScript can be said to support integers and floats.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](Messaging.md)
