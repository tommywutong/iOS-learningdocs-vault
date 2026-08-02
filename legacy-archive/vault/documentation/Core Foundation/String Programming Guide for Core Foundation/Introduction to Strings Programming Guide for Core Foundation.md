---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html
archived_at: '2026-07-15T07:22:59.476381Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Strings.md)

# Introduction to Strings Programming Guide for Core Foundation

Core Foundation string objects give software developers a solid foundation for easy, robust, and consistent internationalization. String objects offer a full suite of fast and efficient string functionality, including utilities for converting among various encodings and buffer formats.

Read this document to learn how to use Core Foundation strings. If you are writing a program using Objective-C, you should consider using `NSString` objects instead (see _[String Programming Guide](../../Cocoa/String%20Programming%20Guide/Introduction%20to%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztk2i)_).

This document contains the following articles:

- [About Strings](About%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tolkdjjbeksscjbea) describes issues related to managing and representing string
- [The Unicode Basis of CFString Objects](The%20Unicode%20Basis%20of%20CFString%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tqlkdjjbeksscjbea) describes the conceptual basis for the representation of strings in Core Foundation
- [String Storage](String%20Storage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tslkdjjbeksscjbea) describes how string data is stored in Core Foundation
- [Creating and Copying Strings](Creating%20and%20Copying%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dglkdjjbekscbifdq) describes how to create and copy string objects
- [Accessing the Contents of String Objects](Accessing%20the%20Contents%20of%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dilkdjjbekscbifdq) describes how to access the contents of CFString objects as a C or Unicode string, and how to iterate over the contents of a string one character at a time
- [Comparing, Sorting, and Searching String Objects](Comparing%2C%20Sorting%2C%20and%20Searching%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dklkdjjbekscbifdq) describes how to search the contents of a string and how to compare two strings
- [Manipulating Mutable String Objects](Manipulating%20Mutable%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dmlkdjjbekscbifdq) describes operations such as combining strings and padding the contents of a string.
- [Converting Between String Encodings](Converting%20Between%20String%20Encodings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dolkdjjbekscbifdq) describes how to convert between different string encodings, and what encodings are supported by CFString
- [Handling External Representations of Strings](Handling%20External%20Representations%20of%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4dqlkdjjbekscbifdq) describes how to represent a string in a form that can be written to disk and read back in on the same platform or on a different platform
- [Creating and Using Ranges](Creating%20and%20Using%20Ranges.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3delkdjjbekscbifdq) describes how to create and use CFRange structures
- [Character Sets](Character%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge4delkdjjbeksscjbea) describes the basics of CFCharacterSet
- [String Format Specifiers](String%20Format%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denrvfvjvomi) describes `printf`-style format specifiers supported by CFString

Not all functions are described. Some of the functions not discussed in detail are:

- `CFStringGetLength` lets you obtain the number of Unicode characters represented by a `CFString` object.
- `CFStringGetLineBounds` tells you how many lines a string (or a range of the string) spans.
- `CFStringCreateByCombiningStrings` creates a single string from an array (`CFArray`) of strings; the counterpart of this function, `CFStringCreateArrayBySeparatingStrings`, creates a `CFArray` object from a single string, using a delimiter character to separate the substrings.
- `CFStringGetIntValue` and `CFStringGetDoubleValue` convert a `CFString` object representing a number to the actual numeric value.

[Next](About%20Strings.md)

