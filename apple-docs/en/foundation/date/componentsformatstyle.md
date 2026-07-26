---
title: Date.ComponentsFormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/componentsformatstyle
source_url: 'https://developer.apple.com/documentation/foundation/date/componentsformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/componentsformatstyle.json'
content_hash: 'sha256:0465b7007d203970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# Date.ComponentsFormatStyle

<sub>Structure</sub>

A style for formatting a date interval in terms of specific date components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ComponentsFormatStyle
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [DiscreteFormatStyle](../discreteformatstyle.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Structures

- [Field](componentsformatstyle/field.md)
- [Style](componentsformatstyle/style-swift.struct.md)

### Initializers

- [init(style:locale:calendar:fields:)](<componentsformatstyle/init(style_locale_calendar_fields_).md>) — Shows the date interval with the specified style and the specified date and time fields.

### Instance Properties

- [calendar](componentsformatstyle/calendar.md)
- [fields](componentsformatstyle/fields.md)
- [isPositive](componentsformatstyle/ispositive.md) — Controls whether the format input is formatted as a positive or negative range.
- [locale](componentsformatstyle/locale.md)
- [style](componentsformatstyle/style-swift.property.md)

### Instance Methods

- [calendar(_:)](<componentsformatstyle/calendar(__).md>)

### Default Implementations

- [DiscreteFormatStyle Implementations](componentsformatstyle/discreteformatstyle-implementations.md)

## See Also

### Applying date and time styles

- [dateTime](../formatstyle/datetime.md) — A style for formatting a date and time.
- [FormatStyle](formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [ISO8601FormatStyle](iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
- [verbatim(_:locale:timeZone:calendar:)](<../formatstyle/verbatim(__locale_timezone_calendar_).md>) — Returns a style for formatting a date with an explicitly-specified style.
- [VerbatimFormatStyle](verbatimformatstyle.md) — A style that formats a date with an explicitly-specified style.
- [interval](../formatstyle/interval.md) — A style for formatting a date interval.
- [IntervalFormatStyle](intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [relative(presentation:unitsStyle:)](<../formatstyle/relative(presentation_unitsstyle_).md>) — Returns a style for formatting a date as relative to the current date.
- [RelativeFormatStyle](relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [components(style:fields:)](<../formatstyle/components(style_fields_).md>) — Returns a style for formatting a date interval in terms of specific date components.
