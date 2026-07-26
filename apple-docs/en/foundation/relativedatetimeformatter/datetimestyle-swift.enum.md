---
title: RelativeDateTimeFormatter.DateTimeStyle
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/relativedatetimeformatter/datetimestyle-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter/datetimestyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter/datetimestyle-swift.enum.json'
content_hash: 'sha256:17ae705e9d0d4fab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RelativeDateTimeFormatter](../relativedatetimeformatter.md)

# RelativeDateTimeFormatter.DateTimeStyle

<sub>Enumeration</sub>

A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DateTimeStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Formatting Dates and Times

- [NSRelativeDateTimeFormatterStyleNamed](datetimestyle-swift.enum/named.md) — A style that uses named styles to describe relative dates, such as “yesterday”, “last week”, or “next week”.
- [NSRelativeDateTimeFormatterStyleNumeric](datetimestyle-swift.enum/numeric.md) — A style that uses a numeric style to describe relative dates, such as “1 day ago” or “in 3 weeks”.

### Initializers

- [init(rawValue:)](<datetimestyle-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring Formatter Options

- [calendar](calendar.md) — The calendar to use for formatting values that don’t have an inherent calendar of their own.
- [locale](locale.md) — The locale to use when formatting the date.
- [dateTimeStyle](datetimestyle-swift.property.md) — The style to use when describing a relative date, for example “yesterday” or “1 day ago”.
- [unitsStyle](unitsstyle-swift.property.md) — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [UnitsStyle](unitsstyle-swift.enum.md) — A type that represents the style to use when formatting the units of relative dates.
- [formattingContext](formattingcontext.md) — A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.
