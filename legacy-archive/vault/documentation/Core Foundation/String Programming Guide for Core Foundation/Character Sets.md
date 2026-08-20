---
title: String Programming Guide for Core Foundation
apple_id: 10000131i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/Articles/CharacterSets.html
archived_at: '2026-07-15T07:22:51.537039Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [String Programming Guide for Core Foundation](Introduction%20to%20Strings%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](String%20Format%20Specifiers.md)[Previous](Creating%20and%20Using%20Ranges.md)

# Character Sets

In Core Foundation, a _character set_, as represented by a CFCharacterSet object, represents a set of Unicode characters. Functions can use character sets to group characters together for searching and parsing operations, so that they can find or exclude any of a particular set of characters during a search. Aside from testing for membership in a character set, a character-set object simply holds a set of character values to limit operations on strings.

You use character sets in search, parsing, and comparison operations involving strings. Programmatic interfaces that require references to CFCharacterSet objects are currently under development in both Core Foundation and Carbon.

To obtain a CFCharacterSet object that can be passed into a function, you can either use one of the predefined character sets or create your own. To use one of the predefined sets—including such things as whitespace, alphanumeric characters, and decimal digits—call `CFCharacterSetGetPredefined` with one of the `CFCharacterSetPredefinedSet` constants. Several CFCharacterSet functions create character sets from strings and bitmapped data and others allow you to create mutable character sets. You can use a predefined character set as a starting point for building a custom set by making a mutable copy of it and changing that.

Because character sets often participate in performance-critical code, you should be aware of the aspects of their use that can affect the performance of your application. Mutable character sets are generally much more expensive than immutable character sets. They consume more memory and are costly to invert (an operation often performed in scanning a string). Because of this, you should follow these guidelines:

- Create as few mutable character sets as possible.
- Cache character sets (in a global dictionary, perhaps) instead of continually recreating them.
- When creating a custom set that doesn't need to change after creation, make an immutable copy of the final character set for actual use, and dispose of the working mutable character set.

[Next](String%20Format%20Specifiers.md)[Previous](Creating%20and%20Using%20Ranges.md)

