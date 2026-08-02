---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Debug12.html
archived_at: '2026-07-18T01:20:02.838378Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Previous Section](Debug11.md)

# Programming Pitfalls to Avoid

This section describes some things to look out for as you debug your application.

## WebScript Programming Pitfalls

Because WebScript looks so much like Objective-C and C, it's easy to forget that WebScript isn't either of these languages. When you're debugging WebScript code, watch out for the following tricky spots:

- WebScript supports only objects that inherit from NSObject. As most objects inherit from NSObject, this limitation is easy to overlook. Notably, EOFault does not inherit from NSObject, so you cannot use it in WebScript code.
- The == operator is supported only for NSNumber objects. If you use == to compare two objects of any other class, the operator compares the addresses of the two objects, not the values of the two objects. To test the equality of two objects, use the __isEqual:__ or __isEqualToString:__ methods.

```
NSString *string1, *string2;

// WRONG!
if (aString1 == aString2) ...

// Right
if ([aString1 isEqualToString:string2]) ...
```

- The postincrement and postdecrement operators are not supported. If you use them, you won't receive an error message. Instead, they behave like preincrement and predecrement operators.

```
i = 0;
if (i++ < 1 )
    // This code never gets executed.
```


For more information, see the chapter ["The WebScript Language"](WebScript9.md#apple-geytanbs).

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Next Section](Debug13.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
