---
title: Date.VerbatimFormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/verbatimformatstyle
source_url: 'https://developer.apple.com/documentation/foundation/date/verbatimformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/verbatimformatstyle.json'
content_hash: 'sha256:ea3ef060b0ce3424'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# Date.VerbatimFormatStyle

<sub>Structure</sub>

A style that formats a date with an explicitly-specified style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct VerbatimFormatStyle
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomConsumingRegexComponent](../../swift/customconsumingregexcomponent.md), [Decodable](../../swift/decodable.md), [DiscreteFormatStyle](../discreteformatstyle.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [ParseableFormatStyle](../parseableformatstyle.md), [RegexComponent](../../swift/regexcomponent.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Structures

- [Attributed](verbatimformatstyle/attributed-swift.struct.md) — The type preserving attributed variant of this style.

### Initializers

- [init(format:locale:timeZone:calendar:)](<verbatimformatstyle/init(format_locale_timezone_calendar_).md>)

### Instance Properties

- [attributed](verbatimformatstyle/attributed-swift.property.md) — Returns a type erased attributed variant of this style. _(deprecated)_
- [attributedStyle](verbatimformatstyle/attributedstyle.md) — Return the type preserving attributed variant of this style.
- [calendar](verbatimformatstyle/calendar.md)
- [locale](verbatimformatstyle/locale.md) — Use system locale if nil or unspecified.
- [timeZone](verbatimformatstyle/timezone.md)

## See Also

### Applying date and time styles

- [dateTime](../formatstyle/datetime.md) — A style for formatting a date and time.
- [FormatStyle](formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [ISO8601FormatStyle](iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
- [verbatim(_:locale:timeZone:calendar:)](<../formatstyle/verbatim(__locale_timezone_calendar_).md>) — Returns a style for formatting a date with an explicitly-specified style.
- [interval](../formatstyle/interval.md) — A style for formatting a date interval.
- [IntervalFormatStyle](intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [relative(presentation:unitsStyle:)](<../formatstyle/relative(presentation_unitsstyle_).md>) — Returns a style for formatting a date as relative to the current date.
- [RelativeFormatStyle](relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [components(style:fields:)](<../formatstyle/components(style_fields_).md>) — Returns a style for formatting a date interval in terms of specific date components.
- [ComponentsFormatStyle](componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
