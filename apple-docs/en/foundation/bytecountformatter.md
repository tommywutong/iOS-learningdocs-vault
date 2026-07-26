---
title: ByteCountFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bytecountformatter
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter.json'
content_hash: 'sha256:118af53f4bc9d109'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ByteCountFormatter

<sub>Class</sub>

A formatter that converts a byte count value into a localized description that is formatted with the appropriate byte modifier (KB, MB, GB and so on).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ByteCountFormatter
```

## Overview

> [!tip] Tip
> In Swift, you can use [ByteCountFormatStyle](bytecountformatstyle.md) or [ByteCount](measurement/formatstyle/bytecount.md) rather than [ByteCountFormatter](bytecountformatter.md). The [FormatStyle](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [FormatStyle](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Strings from Byte Count

- [+ stringFromByteCount:countStyle:](<bytecountformatter/string(frombytecount_countstyle_).md>) — Converts a byte count into the specified string format without creating an `NSNumber` object.
- [- stringFromByteCount:](<bytecountformatter/string(frombytecount_).md>) — Converts a byte count into a string without creating an `NSNumber` object.

### Setting Formatting Styles

- [formattingContext](bytecountformatter/formattingcontext.md) — Specify the formatting context for the formatted string.
- [countStyle](bytecountformatter/countstyle-swift.property.md) — Specify the number of bytes to be used for kilobytes.
- [allowsNonnumericFormatting](bytecountformatter/allowsnonnumericformatting.md) — Determines whether to allow more natural display of some values.
- [includesActualByteCount](bytecountformatter/includesactualbytecount.md) — Determines whether to include the number of bytes after the formatted string.
- [adaptive](bytecountformatter/isadaptive.md) — Determines the display style of the size representation.
- [allowedUnits](bytecountformatter/allowedunits.md) — Specify the units that can be used in the output.
- [includesCount](bytecountformatter/includescount.md) — Determines whether to include the count in the resulting formatted string.
- [includesUnit](bytecountformatter/includesunit.md) — Determines whether to include the units in the resulting formatted string.
- [zeroPadsFractionDigits](bytecountformatter/zeropadsfractiondigits.md) — Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.

### Constants

- [Units](bytecountformatter/units.md) — Specifies the units appropriate for the formatter to display. Specifying any units explicitly causes just those units to be used in showing the number.
- [CountStyle](bytecountformatter/countstyle-swift.enum.md) — Specifies display of file or storage byte counts. The display style is platform specific.

### Instance Methods

- [- stringForObjectValue:](<bytecountformatter/string(for_).md>) — Formats `obj` as a byte count (if `obj` is an `NSNumber`) or specific byte measurement (if `obj` is an `NSMeasurement`) using the receiver’s settings.
- [- stringFromMeasurement:](<bytecountformatter/string(from_).md>) — Formats the value of the given measurement using the receiver’s `countStyle`.

### Type Methods

- [+ stringFromMeasurement:countStyle:](<bytecountformatter/string(from_countstyle_).md>) — Formats the value of the given measurement using the given `countStyle`.
