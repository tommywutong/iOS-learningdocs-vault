---
title: RelativeDateTimeFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/relativedatetimeformatter
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter.json'
content_hash: 'sha256:6ab74b0c5a2c5048'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# RelativeDateTimeFormatter

<sub>Class</sub>

A formatter that creates locale-aware string representations of a relative date or time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class RelativeDateTimeFormatter
```

## Overview

Use the strings that the formatter produces, such as “1 hour ago”, “in 2 weeks”, “yesterday”, and “tomorrow” as standalone strings. Embedding them in other strings may not be grammatically correct.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Converting Dates to Formatted Strings

- [- localizedStringForDate:relativeToDate:](<relativedatetimeformatter/localizedstring(for_relativeto_).md>) — Formats the date interval from the reference date to the specified date using the formatter’s calendar.
- [- localizedStringFromDateComponents:](<relativedatetimeformatter/localizedstring(from_).md>) — Formats a relative time represented by the specified date components.
- [- localizedStringFromTimeInterval:](<relativedatetimeformatter/localizedstring(fromtimeinterval_).md>) — Formats the specified time interval using the formatter’s calendar.
- [- stringForObjectValue:](<relativedatetimeformatter/string(for_).md>) — Creates a formatted string for a date relative to the current date and time.

### Configuring Formatter Options

- [calendar](relativedatetimeformatter/calendar.md) — The calendar to use for formatting values that don’t have an inherent calendar of their own.
- [locale](relativedatetimeformatter/locale.md) — The locale to use when formatting the date.
- [dateTimeStyle](relativedatetimeformatter/datetimestyle-swift.property.md) — The style to use when describing a relative date, for example “yesterday” or “1 day ago”.
- [DateTimeStyle](relativedatetimeformatter/datetimestyle-swift.enum.md) — A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.
- [unitsStyle](relativedatetimeformatter/unitsstyle-swift.property.md) — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [UnitsStyle](relativedatetimeformatter/unitsstyle-swift.enum.md) — A type that represents the style to use when formatting the units of relative dates.
- [formattingContext](relativedatetimeformatter/formattingcontext.md) — A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.

## See Also

### Dates and times

- [DateFormatter](dateformatter.md) — A formatter that converts between dates and their textual representations.
- [DateComponentsFormatter](datecomponentsformatter.md) — A formatter that creates string representations of quantities of time.
- [DateIntervalFormatter](dateintervalformatter.md) — A formatter that creates string representations of time intervals.
- [ISO8601DateFormatter](iso8601dateformatter.md) — A formatter that converts between dates and their ISO 8601 string representations.
