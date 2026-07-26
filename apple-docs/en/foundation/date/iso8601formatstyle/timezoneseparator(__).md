---
title: 'timeZoneSeparator(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/iso8601formatstyle/timezoneseparator(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/timezoneseparator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/timezoneseparator%28_%3A%29.json'
content_hash: 'sha256:d6761d8d0518b1f8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# timeZoneSeparator(_:)

<sub>Instance Method</sub>

Modifies the ISO 8601 date format style to use the specified time zone separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func timeZoneSeparator(_ separator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle
```

## Parameters

- `separator` — Character used to separate the time and time zone in a date.

## Return Value

An ISO 8601 date format style modified to include the specified time zone separator style.

## Discussion

Possible values of [TimeZoneSeparator](timezoneseparator-swift.enum.md) are [Date.ISO8601FormatStyle.TimeZoneSeparator.colon](timezoneseparator-swift.enum/colon.md) and [Date.ISO8601FormatStyle.TimeZoneSeparator.omitted](timezoneseparator-swift.enum/omitted.md).

For more information about ISO 8601 formatted dates, see the [ISO8601FormatStyle](../iso8601formatstyle.md).

## See Also

### Modifying Times in an ISO 8601 Format Style

- [time(includingFractionalSeconds:)](<time(includingfractionalseconds_).md>) — Modifies the ISO 8601 date format style to include the time in the formatted output.
- [timeSeparator(_:)](<timeseparator(__).md>) — Modifies the ISO 8601 date format style to use the specified time separator.
- [timeZone(separator:)](<timezone(separator_).md>) — Modifies the ISO 8601 date format style to include the time zone in the formatted output.
