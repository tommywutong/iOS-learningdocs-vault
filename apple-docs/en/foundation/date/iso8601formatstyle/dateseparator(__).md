---
title: 'dateSeparator(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/iso8601formatstyle/dateseparator(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/dateseparator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/dateseparator%28_%3A%29.json'
content_hash: 'sha256:0d5042175240985a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# dateSeparator(_:)

<sub>Instance Method</sub>

Modifies the ISO 8601 date format style to use the specified date separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dateSeparator(_ separator: Date.ISO8601FormatStyle.DateSeparator) -> Date.ISO8601FormatStyle
```

## Parameters

- `separator` — Character used to separate the year, month, and day in a date.

## Return Value

An ISO 8601 date format style modified to include the specified date separator style.

## Discussion

Possible values of [DateSeparator](dateseparator-swift.enum.md) are [Date.ISO8601FormatStyle.DateSeparator.dash](dateseparator-swift.enum/dash.md) and [Date.ISO8601FormatStyle.DateSeparator.omitted](dateseparator-swift.enum/omitted.md).

The following example shows a variety of [DateSeparator](dateseparator-swift.enum.md) formats applied to an ISO 8601 date format.

```swift
let meetingDate = Date() // Jun 23, 2021 at 6:13 AM
meetingDate.formatted(.iso8601.dateSeparator(.omitted)) // 20210623T111325Z
meetingDate.formatted(.iso8601.dateSeparator(.dash)) // 2021-06-23T111325Z
meetingDate.formatted(.iso8601) // 20210623T111325Z
```

If no format is specified as a parameter, the [Date.ISO8601FormatStyle.DateSeparator.omitted](dateseparator-swift.enum/omitted.md) case is the default format.

For more information about ISO 8601 formatted dates, see the [ISO8601FormatStyle](../iso8601formatstyle.md).

## See Also

### Modifying Dates in an ISO 8601 Format Style

- [year()](<year().md>) — Modifies the ISO 8601 date format style to include the year in the formatted output.
- [month()](<month().md>) — Modifies the ISO 8601 date format style to include the month in the formatted output.
- [weekOfYear()](<weekofyear().md>) — Modifies the ISO 8601 date format style to include the week of the year in the formatted output.
- [day()](<day().md>) — Modifies the ISO 8601 date format style to include the day in the formatted output.
