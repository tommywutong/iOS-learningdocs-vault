---
title: DateComponents.ISO8601FormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponents/iso8601formatstyle
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/iso8601formatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/iso8601formatstyle.json'
content_hash: 'sha256:40e4d685563f8d99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# DateComponents.ISO8601FormatStyle

<sub>Structure</sub>

Options for generating and parsing string representations of dates following the ISO 8601 standard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ISO8601FormatStyle
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomConsumingRegexComponent](../../swift/customconsumingregexcomponent.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [ParseStrategy](../parsestrategy.md), [ParseableFormatStyle](../parseableformatstyle.md), [RegexComponent](../../swift/regexcomponent.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:includingFractionalSeconds:timeZone:)](<iso8601formatstyle/init(dateseparator_datetimeseparator_timeseparator_timezoneseparator_includingfractionalseconds_timezone_).md>)

### Instance Properties

- [dateSeparator](iso8601formatstyle/dateseparator.md)
- [dateTimeSeparator](iso8601formatstyle/datetimeseparator.md)
- [includingFractionalSeconds](iso8601formatstyle/includingfractionalseconds.md) — If set, fractional seconds will be present in formatted output. Fractional seconds may be present in parsing regardless of the setting of this property.
- [timeSeparator](iso8601formatstyle/timeseparator.md)
- [timeZone](iso8601formatstyle/timezone.md) — The time zone to use to create and parse date representations.
- [timeZoneSeparator](iso8601formatstyle/timezoneseparator.md)

### Instance Methods

- [dateSeparator(_:)](<iso8601formatstyle/dateseparator(__).md>)
- [dateTimeSeparator(_:)](<iso8601formatstyle/datetimeseparator(__).md>)
- [day()](<iso8601formatstyle/day().md>)
- [month()](<iso8601formatstyle/month().md>)
- [time(includingFractionalSeconds:)](<iso8601formatstyle/time(includingfractionalseconds_).md>)
- [timeSeparator(_:)](<iso8601formatstyle/timeseparator(__).md>)
- [timeZone(separator:)](<iso8601formatstyle/timezone(separator_).md>)
- [timeZoneSeparator(_:)](<iso8601formatstyle/timezoneseparator(__).md>)
- [weekOfYear()](<iso8601formatstyle/weekofyear().md>)
- [year()](<iso8601formatstyle/year().md>)
