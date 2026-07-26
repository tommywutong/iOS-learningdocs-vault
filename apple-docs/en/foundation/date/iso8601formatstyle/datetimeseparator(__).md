---
title: 'dateTimeSeparator(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/iso8601formatstyle/datetimeseparator(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/datetimeseparator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/datetimeseparator%28_%3A%29.json'
content_hash: 'sha256:e27fa402ed21bb68'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# dateTimeSeparator(_:)

<sub>Instance Method</sub>

Sets the character that specifies the date and time components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dateTimeSeparator(_ separator: Date.ISO8601FormatStyle.DateTimeSeparator) -> Date.ISO8601FormatStyle
```

## Parameters

- `separator` — Possible values are `space` and `standard`.

## Return Value

An ISO 8601 date format style with the provided date and time component separator.

## Discussion

Possible values of [DateTimeSeparator](datetimeseparator-swift.enum.md) are [Date.ISO8601FormatStyle.DateTimeSeparator.space](datetimeseparator-swift.enum/space.md) and [Date.ISO8601FormatStyle.DateTimeSeparator.standard](datetimeseparator-swift.enum/standard.md).

The following example shows a variety of [DateTimeSeparator](datetimeseparator-swift.enum.md) formats applied to an ISO 8601 date format.

```swift
let meetingDate = Date() // Jun 23, 2021 at 10:21 AM
meetingDate.formatted(.iso8601.dateSeparator(.omitted)) // 20210623 152135Z
meetingDate.formatted(.iso8601.dateSeparator(.dash)) // 20210623T152135Z
meetingDate.formatted(.iso8601) // 20210623T152135Z
```

If no format is specified as a parameter, the [Date.ISO8601FormatStyle.DateTimeSeparator.standard](datetimeseparator-swift.enum/standard.md) case is the default format.

For more information about ISO 8601 formatted dates, see the [ISO8601FormatStyle](../iso8601formatstyle.md).

## See Also

### Modifying an ISO 8601 Format Style

- [dateSeparator](dateseparator-swift.property.md) — The character used to separate the components of a date.
- [dateTimeSeparator](datetimeseparator-swift.property.md) — The character used to separate the date and time components of an ISO 8601 string representation of a date.
- [timeZone](timezone.md) — The time zone used to create and parse date representations.
