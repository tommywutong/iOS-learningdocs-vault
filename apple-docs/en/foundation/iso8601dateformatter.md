---
title: ISO8601DateFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/iso8601dateformatter
source_url: 'https://developer.apple.com/documentation/foundation/iso8601dateformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/iso8601dateformatter.json'
content_hash: 'sha256:2bada079898236fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ISO8601DateFormatter

<sub>Class</sub>

A formatter that converts between dates and their ISO 8601 string representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ISO8601DateFormatter
```

## Overview

The [ISO8601DateFormatter](iso8601dateformatter.md) class generates and parses string representations of dates following the [ISO 8601](http://www.iso.org/iso/home/standards/iso8601) standard. Use this class to create ISO 8601 representations of dates and create dates from text strings in ISO 8601 format.

> [!tip] Tip
> In Swift, you can use [ISO8601FormatStyle](date/iso8601formatstyle.md) rather than [ISO8601DateFormatter](iso8601dateformatter.md). The [FormatStyle](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [FormatStyle](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Configuring the Formatter

- [formatOptions](iso8601dateformatter/formatoptions.md) — Options for generating and parsing ISO 8601 date representations. See [Options](iso8601dateformatter/options.md) for possible values.
- [timeZone](iso8601dateformatter/timezone.md) — The time zone used to create and parse date representations. When unspecified, GMT is used.

### Creating ISO 8601 Date Formatters

- [- init](<iso8601dateformatter/init().md>) — Initializes an ISO 8601 date formatter with default format, time zone, and options.

### Converting ISO 8601 Dates

- [- stringFromDate:](<iso8601dateformatter/string(from_).md>) — Creates and returns an ISO 8601 formatted string representation of the specified date.
- [- dateFromString:](<iso8601dateformatter/date(from_).md>) — Creates and returns a date object from the specified ISO 8601 formatted string representation.
- [+ stringFromDate:timeZone:formatOptions:](<iso8601dateformatter/string(from_timezone_formatoptions_).md>) — Creates a representation of the specified date with a given time zone and format options.

### Constants

- [Options](iso8601dateformatter/options.md) — Options used to generate and parse ISO 8601 date representations.

## See Also

### Dates and times

- [DateFormatter](dateformatter.md) — A formatter that converts between dates and their textual representations.
- [DateComponentsFormatter](datecomponentsformatter.md) — A formatter that creates string representations of quantities of time.
- [RelativeDateTimeFormatter](relativedatetimeformatter.md) — A formatter that creates locale-aware string representations of a relative date or time.
- [DateIntervalFormatter](dateintervalformatter.md) — A formatter that creates string representations of time intervals.
