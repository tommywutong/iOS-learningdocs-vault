---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/NoteToObjCDev.html
archived_at: '2026-07-15T07:48:03.443934Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](LanguageSummary.md)

# A Note to Objective-C Developers

WebScript uses a subset of Objective-C syntax, but its role within an application is significantly different. The following table summarizes some of the differences.

| Objective-C | WebScript |
| --- | --- |
| Supports primitive C data types | Only supports the __id__ data type |
| Requires method prototyping | Doesn't require method prototyping (that is, you don't declare methods before you use them) |
| Usually includes a .h and a .m file | Usually has corresponding declarations and HTML template files (unless it is an application script) |
| Supports all C language features | Has limited support for C language features; for example, doesn't support structures, pointers, enumerators, or unions |
| Methods not declared to return void must include a return statement | Methods aren't required to include a return statement |
| Has preprocessor support | Has no preprocessor support---that is, doesn't support the #import or #include statements |

Perhaps the most significant difference between Objective-C and WebScript is that in WebScript, the only valid data type is __id__. Some of the less obvious implications of this are:

- You can't use methods that take non-object arguments (unless those arguments are integers or floats, which WebScript converts to NSNumbers). For example, in WebScript the following statement is invalid:

```
      // NO!! This won't work.
      string = [NSString stringWithCString:"my string"];
```

- You can only use the "at sign" character (@) as a conversion character with methods that take a format string as an argument:

```
      // This is fine.
      [self logWithFormat:@"The value is %@", myVar];
      // NO!! This won't work.
      [self logWithFormat:@"The values are %d and %s", var1, var2];
```

- You shouldn't supply any type information for a method's arguments and return types. These types are assumed to be __id__, and if you supply any type information, you will get an error.

```objc
      // This is fine.
      - aMethod:anArg {
      // NO!! This won't work.
      - (void) aMethod:(NSString *)anArg {
      // This won't work either
      - (id)aMethod:(id)anArg {
```

- You need to substitute integer values for enumerated types.

: For example, suppose you want to compare two numeric values using the enumerated type NSComparisonResult. This is how you might do it in Objective-C:

```
      result = [num1 compare:num2];
      if(result == NSOrderedAscending)            /* This won't work in WebScript */
          /* num1 is less than num2 */
```

: But this won't work in WebScript. Instead, you have to use the integer value of NSOrderedAscending, as follows:

```
      result = [num1 compare:num2];
      if(result == -1)
          /* num1 is less than num2 */
```

: For a listing of the integer values of enumerated types, see the "Types and Constants" section in the _Foundation Framework Reference_.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](OOoverview.md)
