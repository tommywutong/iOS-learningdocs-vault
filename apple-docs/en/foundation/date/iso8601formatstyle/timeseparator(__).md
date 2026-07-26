---
title: 'timeSeparator(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/iso8601formatstyle/timeseparator(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/timeseparator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/timeseparator%28_%3A%29.json'
content_hash: 'sha256:5d0baaf8208ea3a4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# timeSeparator(_:)

<sub>Instance Method</sub>

Modifies the ISO 8601 date format style to use the specified time separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func timeSeparator(_ separator: Date.ISO8601FormatStyle.TimeSeparator) -> Date.ISO8601FormatStyle
```

## Parameters

- `separator` — Character used to separate the hour and minute in a date.

## Return Value

An ISO 8601 date format style modified to include the specified time separator style.

## Discussion

Possible values of [TimeSeparator](timeseparator-swift.enum.md) are [Date.ISO8601FormatStyle.TimeSeparator.colon](timeseparator-swift.enum/colon.md) and [Date.ISO8601FormatStyle.TimeSeparator.omitted](timeseparator-swift.enum/omitted.md).

This example shows a variety of ISO 8601 time separator formats applied to an ISO 8601 date format:

```swift
let meetingDate = Date() // Jun 23, 2021 at 1:41 PM
meetingDate.formatted(.iso8601.timeSeparator(.omitted)) // 20210623T184148Z
meetingDate.formatted(.iso8601.timeSeparator(.colon)) // 20210623T18:41:48Z
meetingDate.formatted(.iso8601) // 20210623T184148Z
```

If no format is specified as a parameter, the [Date.ISO8601FormatStyle.DateSeparator.omitted](dateseparator-swift.enum/omitted.md) case is the default format.

For more information about ISO 8601 formatted dates, see the [ISO8601FormatStyle](../iso8601formatstyle.md).

## See Also

### Modifying Times in an ISO 8601 Format Style

- [time(includingFractionalSeconds:)](<time(includingfractionalseconds_).md>) — Modifies the ISO 8601 date format style to include the time in the formatted output.
- [timeZone(separator:)](<timezone(separator_).md>) — Modifies the ISO 8601 date format style to include the time zone in the formatted output.
- [timeZoneSeparator(_:)](<timezoneseparator(__).md>) — Modifies the ISO 8601 date format style to use the specified time zone separator.
