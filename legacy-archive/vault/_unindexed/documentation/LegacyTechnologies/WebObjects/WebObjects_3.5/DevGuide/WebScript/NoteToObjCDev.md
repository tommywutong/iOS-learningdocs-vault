---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/NoteToObjCDev.html
archived_at: '2026-07-15T07:52:32.777960Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](Categories.md)

# WebScript for Objective-C Developers

WebScript uses a subset of Objective-C syntax, but its role within an application is significantly different. The following table summarizes some of the differences.

| __ __Objective-C____ | __ WebScript__ |
|  Is compiled |  Is interpreted |
|  Supports primitive C data types |  Supports only the class type |
|  Performs type checking at compiled time |  Never performs type checking |
|  Requires method prototyping |  Doesn't require method prototyping (that is, you don't declare methods before you use them) |
|  Usually involves a .h and a .m file |  Stands alone (unless inside of a component directory) |
|  Supports all C language features |  Has limited support for C language features; for example, doesn't support structures, pointers, enumerations, or unions |
|  Methods not declared to return void must include a return statement |  Methods aren't required to include a return statement |
|  Has preprocessor support |  Has no preprocessor support-that is, doesn't support the #define, #import, or #include statements |
|  Uses reference counting to determine when to release instance variables |  Automatically retains all instance variables for the life of the object that owns them. Automatically releases instance variables when the object is released. |

```
```


Here are some of the more subtle differences between WebScript and Objective-C:

- You don't need to retain instance variables in the __init__ method or release them in the __dealloc__ method. In general, you never have to worry about releasing variables. One exception: if you perform a __mutableCopy__ on an object, you must release that copy.
- Categories must not have an __@interface__ declaration in WebScript.
- The @ in WebScript signifies the initialization of an NSString, NSDictionary, or NSArray.
- Instead of using operators like __@selector__, you simply enclose the selector in double quotes ("").
- Certain operators from the C language aren't available in WebScript, notably the postdecrement, postincrement, and cast operators.
- Boolean expressions never short-circuit.

Of course, the most significant difference between Objective-C and WebScript is that in WebScript, all variables must be objects. Some of the less obvious implications of this are:

- You can't use methods that take non-object arguments (unless those arguments are integers or floats, which WebScript converts to NSNumbers). For example, in WebScript the following statement is invalid:

```
    // NO!! This won't work.NSRange is a structure.
    string = [NSString substringWithRange:aRange];
```

- You can only use the "at sign" character (@) as a conversion character with methods that take a format string as an argument:

```
    // This is fine.
    [self logWithFormat:@"The value is %@", myVar];

    // NO!! This won't work. It prints the address of var1.
    [self logWithFormat:@"The values are %d and %s", var1, var2];
```

- You need to substitute integer values for enumerated types.

For example, suppose you want to compare two numeric values using the enumerated type NSComparisonResult. This is how you might do it in Objective-C:

```
    result = [num1 compare:num2];
    if(result == NSOrderedAscending) /* This won't work in WebScript */
        /* num1 is less than num2 */
```


But this won't work in WebScript. Instead, you have to use the integer value of NSOrderedAscending, as follows:

```
    result = [num1 compare:num2];
    if(result == -1)
        /* num1 is less than num2 */
```


For a listing of the integer values of enumerated types, see the "Types and Constants" section in the _Foundation Framework Reference_.

[!Table of Contents](WebScript.md) [!Next Section](WebScriptFromObjC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
