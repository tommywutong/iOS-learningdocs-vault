---
title: 'timeZone(separator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/iso8601formatstyle/timezone(separator:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/timezone(separator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/timezone%28separator%3A%29.json'
content_hash: 'sha256:25b651ae79a02414'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# timeZone(separator:)

<sub>Instance Method</sub>

Modifies the ISO 8601 date format style to include the time zone in the formatted output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func timeZone(separator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Date.ISO8601FormatStyle
```

## Parameters

- `separator` — Character used to separate the time and time zone in a date.

## Return Value

An ISO 8601 date format style modified to include the time zone.

## Discussion

The default [ISO8601FormatStyle](../iso8601formatstyle.md) doesn’t include the time zone.

For more information about formatting dates, see the [FormatStyle](../formatstyle.md).

## See Also

### Modifying Times in an ISO 8601 Format Style

- [time(includingFractionalSeconds:)](<time(includingfractionalseconds_).md>) — Modifies the ISO 8601 date format style to include the time in the formatted output.
- [timeSeparator(_:)](<timeseparator(__).md>) — Modifies the ISO 8601 date format style to use the specified time separator.
- [timeZoneSeparator(_:)](<timezoneseparator(__).md>) — Modifies the ISO 8601 date format style to use the specified time zone separator.
