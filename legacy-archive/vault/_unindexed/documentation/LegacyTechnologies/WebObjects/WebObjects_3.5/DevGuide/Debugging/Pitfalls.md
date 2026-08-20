---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Debugging/Pitfalls.html
archived_at: '2026-07-15T07:51:21.494151Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DebuggingTOC.md) [!Previous Section](Techniques.md)

# Programming Pitfalls to Avoid

This section describes some things to look out for as you debug your application.

## WebScript Programming Pitfalls

Because WebScript looks so much like Objective-C and C, it's easy to forget that WebScript isn't either of these languages. When you're debugging WebScript code, watch out for the following tricky spots:

- WebScript supports only objects that inherit from NSObject. As most objects inherit from NSObject, this limitation is easy to overlook. Notably, EOFault does not inherit from NSObject, so you cannot use it in WebScript code.
- The == operator is supported only for NSNumber objects. If you use == to compare two objects of any other class, the operator compares the addresses of the two objects, not the values of the two objects. To test the equality of two objects, use the __isEqual:__ method.

```
    NSString *string1, *string2;

    // WRONG!
    if (aString1 == aString2) ...

    // Right
    if ([aString1 isEqual:string2]) ...
```

- The postincrement and postdecrement operators are not supported. If you use them, you won't receive an error message. Instead, they behave like preincrement and predecrement operators.

```
    i = 0;
    if (i++ < 1 )
        // This code never gets executed.
```

- WebScript always evaluates both sides of a Boolean expression (such as && and ||). You should make sure that the second half of an expression does not produce an error.

```
    // WRONG! produces a divide by 0 if a is 0.
    if ((a == 0) || (b / a) > 5) ...
```


For more information, see the chapter ["The WebScript Language"](../WebScript/WebScript.md#apple-gu4tmna).

[!Table of Contents](DebuggingTOC.md) [!Next Section](JavaPitfalls.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
