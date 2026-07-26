---
title: RelativeDateTimeFormatter.UnitsStyle
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/relativedatetimeformatter/unitsstyle-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter/unitsstyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter/unitsstyle-swift.enum.json'
content_hash: 'sha256:a1f281d093c3b9f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RelativeDateTimeFormatter](../relativedatetimeformatter.md)

# RelativeDateTimeFormatter.UnitsStyle

<sub>Enumeration</sub>

A type that represents the style to use when formatting the units of relative dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum UnitsStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Formatting Date and Time Units

- [NSRelativeDateTimeFormatterUnitsStyleAbbreviated](unitsstyle-swift.enum/abbreviated.md) — A style that uses abbreviated units, such as “2 mo. ago”.
- [NSRelativeDateTimeFormatterUnitsStyleFull](unitsstyle-swift.enum/full.md) — A style that uses full units, such as “2 months ago”.
- [NSRelativeDateTimeFormatterUnitsStyleShort](unitsstyle-swift.enum/short.md) — A style that uses shortened units, such as “2 mo. ago”.
- [NSRelativeDateTimeFormatterUnitsStyleSpellOut](unitsstyle-swift.enum/spellout.md) — A style that spells out units such as “two months ago”.

### Initializers

- [init(rawValue:)](<unitsstyle-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring Formatter Options

- [calendar](calendar.md) — The calendar to use for formatting values that don’t have an inherent calendar of their own.
- [locale](locale.md) — The locale to use when formatting the date.
- [dateTimeStyle](datetimestyle-swift.property.md) — The style to use when describing a relative date, for example “yesterday” or “1 day ago”.
- [DateTimeStyle](datetimestyle-swift.enum.md) — A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.
- [unitsStyle](unitsstyle-swift.property.md) — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [formattingContext](formattingcontext.md) — A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.
