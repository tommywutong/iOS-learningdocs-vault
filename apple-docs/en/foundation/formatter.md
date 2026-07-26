---
title: Formatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatter
source_url: 'https://developer.apple.com/documentation/foundation/formatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter.json'
content_hash: 'sha256:839b32cf8aa6fb32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Formatter

<sub>Class</sub>

An abstract class that declares an interface for objects that create, interpret, and validate the textual representation of values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Formatter
```

## Overview

The Foundation framework provides several concrete subclasses of [Formatter](formatter.md), including [ByteCountFormatter](bytecountformatter.md), [DateFormatter](dateformatter.md), [DateComponentsFormatter](datecomponentsformatter.md), [DateIntervalFormatter](dateintervalformatter.md), [MeasurementFormatter](measurementformatter.md), [NumberFormatter](numberformatter.md), and [PersonNameComponentsFormatter](personnamecomponentsformatter.md).

> [!tip] Tip
> In Swift, you can use implementations of [FormatStyle](formatstyle.md) rather than [Formatter](formatter.md). The [FormatStyle](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [FormatStyle](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

### Subclassing Notes

[Formatter](formatter.md) is intended for subclassing. A custom formatter can restrict the input and enhance the display of data in novel ways. For example, you could have a custom formatter that ensures that serial numbers entered by a user conform to predefined formats. Before you decide to create a custom formatter, make sure that you cannot configure the public subclasses to satisfy your requirements.

For instructions on how to create your own custom formatter, see [Creating a Custom Formatter](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/Articles/CreatingACustomFormatter.html#//apple_ref/doc/uid/20000196).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [ByteCountFormatter](bytecountformatter.md), [DateComponentsFormatter](datecomponentsformatter.md), [DateFormatter](dateformatter.md), [DateIntervalFormatter](dateintervalformatter.md), [EnergyFormatter](energyformatter.md), [ISO8601DateFormatter](iso8601dateformatter.md), [LengthFormatter](lengthformatter.md), [ListFormatter](listformatter.md), [MassFormatter](massformatter.md), [MeasurementFormatter](measurementformatter.md), [NumberFormatter](numberformatter.md), [PersonNameComponentsFormatter](personnamecomponentsformatter.md), [RelativeDateTimeFormatter](relativedatetimeformatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Formatters

- [Displaying Human-Friendly Content](displaying-human-friendly-content.md) — Convert data into readable strings or Swift objects using formatters.

### Getting Textual Representations of Object Values

- [- stringForObjectValue:](<formatter/string(for_).md>) — The default implementation of this method raises an exception.
- [- attributedStringForObjectValue:withDefaultAttributes:](<formatter/attributedstring(for_withdefaultattributes_).md>) — The default implementation returns `nil` to indicate that the formatter object does not provide an attributed string.
- [- editingStringForObjectValue:](<formatter/editingstring(for_).md>) — The default implementation of this method invokes [- stringForObjectValue:](<formatter/string(for_).md>).

### Getting Object Values for Textual Representations

- [- getObjectValue:forString:errorDescription:](<formatter/getobjectvalue(__for_errordescription_).md>) — The default implementation of this method raises an exception.

### Validating Partial Strings

- [- isPartialStringValid:newEditingString:errorDescription:](<formatter/ispartialstringvalid(__neweditingstring_errordescription_).md>) — Returns a Boolean value that indicates whether a partial string is valid.
- [- isPartialStringValid:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:](<formatter/ispartialstringvalid(__proposedselectedrange_originalstring_originalselectedrange_errordescription_).md>) — This method should be implemented in subclasses that want to validate user changes to a string in a field, where the user changes are not necessarily at the end of the string, and preserve the selection (or set a different one, such as selecting the erroneous part of the string the user has typed).

### Constants

- [Context](formatter/context.md) — The formatting context for a formatter.
- [UnitStyle](formatter/unitstyle.md) — Specifies the width of the unit, determining the textual representation.

### Initializers

- [init(coder:)](<formatter/init(coder_).md>)
