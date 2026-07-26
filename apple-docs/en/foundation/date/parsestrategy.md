---
title: Date.ParseStrategy
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/parsestrategy
source_url: 'https://developer.apple.com/documentation/foundation/date/parsestrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/parsestrategy.json'
content_hash: 'sha256:3a9d42f009b68a7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# Date.ParseStrategy

<sub>Structure</sub>

Options for parsing string representations of dates to create a `Date` instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ParseStrategy
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomConsumingRegexComponent](../../swift/customconsumingregexcomponent.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [ParseStrategy](../parsestrategy.md), [RegexComponent](../../swift/regexcomponent.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(format:locale:timeZone:calendar:isLenient:twoDigitStartDate:)](<parsestrategy/init(format_locale_timezone_calendar_islenient_twodigitstartdate_).md>) — Creates a new `ParseStrategy` with the given configurations.

### Instance Properties

- [calendar](parsestrategy/calendar.md) — The calendar to use when parsing date strings and creating the date.
- [format](parsestrategy/format.md) — The string representation of the fixed format conforming to Unicode Technical Standard #35.
- [isLenient](parsestrategy/islenient.md) — Indicates whether to use heuristics when parsing the representation.
- [locale](parsestrategy/locale.md) — The locale to use when parsing date strings with the specified format. Use system locale if unspecified.
- [timeZone](parsestrategy/timezone.md) — The time zone to use for creating the date.
- [twoDigitStartDate](parsestrategy/twodigitstartdate.md) — The earliest date that can be denoted by a two-digit year specifier.

### Default Implementations

- [CustomConsumingRegexComponent Implementations](parsestrategy/customconsumingregexcomponent-implementations.md)
- [ParseStrategy Implementations](parsestrategy/parsestrategy-implementations.md)
- [RegexComponent Implementations](parsestrategy/regexcomponent-implementations.md)

## See Also

### Parsing Dates

- [parse(_:)](<formatstyle/parse(__).md>) — Parses a string into a date.
- [parseStrategy](formatstyle/parsestrategy.md) — The strategy used to parse a string into a date.
