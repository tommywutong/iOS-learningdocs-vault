---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/Articles/about.html
archived_at: '2026-07-15T07:22:58.430098Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [String Programming Guide for Core Foundation](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](The%20Unicode%20Basis%20of%20CFString%20Objects.md)[Previous](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)

# About Strings

One of the biggest challenges of developing software for a global market is that posed by text—or, in programming terms, “strings,” which denotes the characters of a language in a form suitable for computerized representation. Most of the difficulty with strings is historical; over the years (since computers have been around), various encoding schemes have been devised to represent strings in one script or another. Some encodings are intended for a language or family of languages (Shift-JIS, for example) while others are specific to a particular computer system (Windows Latin 1, for example). The proliferation of encodings complicates the burdens of cross-platform compatibility and internationalization.

Core Foundation string objects give software developers a solid foundation for easy, robust, and consistent internationalization. String objects offers a full suite of fast and efficient string functionality, including utilities for converting among various encodings and buffer formats.

String objects are implemented by the `CFString` opaque type. A `CFString` “object” represents a string as an array of Unicode characters; its only other property aside from this array is an integer indicating the number of characters. It is flexible enough to hold up to several megabytes worth of characters. Yet it is simple and fundamental enough for use in all programming interfaces that communicate character data. In Core Foundation, string operations take place with performance characteristics not much different from standard C strings. `CFString` objects come in immutable and mutable variants.

The Unicode basis of `CFString` along with comprehensive encoding-conversion facilities make string objects an essential vehicle for internationalizing programs. String objects also allow you to convert strings among C, byte buffer, and native Unicode buffer formats. Taken together, these features make it possible for programs to pass each other string data despite differing programming languages, libraries, frameworks, or platforms.

String objects also includes the `CFCharacterSet` opaque type. Programming interfaces can use `CFCharacterSet` objects to specify characters to include or exclude in parsing, comparison, or search operations.

`CFString` objects are fundamental in that they represent strings but they do not carry any display or supplemental information, such as text styles, formatting attributes, or language tags. If you want this functionality, use an attributed string (see _[CFAttributedString Reference](https://developer.apple.com/documentation/corefoundation/cfattributedstring-s1s)_). In addition, a `CFString` object cannot be used to hold random bytes because it attaches semantic value to its contents (interpreting it as Unicode characters or even characters in other encodings). If you need a Core Foundation object to hold non-character data, use an object based on the `CFData` opaque type (see _[CFData Reference](https://developer.apple.com/documentation/corefoundation/cfdata)_).

String objects provide functions that perform a variety of operations with `CFString` objects, such as

- Converting between `CFString` objects and strings in other encodings and buffer formats
- Comparing and searching strings
- Manipulating mutable strings by appending string data to them, inserting and deleting characters, and padding and trimming characters
- Disclosing the contents of `CFString` objects in supported debuggers

`CFString` and other Core Foundation objects do not provide more advanced string-handling utilities such as drawing, text layout, font handling, and sophisticated search and comparison functionality. Higher software layers provide these facilities. Nonetheless, these higher layers communicate string data using `CFString` objects, or their “toll-free bridged” Cocoa equivalent, [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString).

[Next](The%20Unicode%20Basis%20of%20CFString%20Objects.md)[Previous](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)

