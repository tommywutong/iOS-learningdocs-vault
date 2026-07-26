---
title: day()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/iso8601formatstyle/day()
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/day()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/day%28%29.json'
content_hash: 'sha256:e6fd89a33570ddc7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# day()

<sub>Instance Method</sub>

Modifies the ISO 8601 date format style to include the day in the formatted output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func day() -> Date.ISO8601FormatStyle
```

## Return Value

An ISO 8601 date format style modified to include the day.

## Discussion

The following example shows an ISO 8601 format with, and without, a day.

```swift
let meetingDate = Date() // Jun 23, 2021 at 12:51 PM
meetingDate.formatted(.iso8601
    .year()
    .month()
)
// 202106

meetingDate.formatted(.iso8601
    .year()
    .day()
) 
// 2021174

meetingDate.formatted(.iso8601
    .year()
    .month()
    .day()
) 
// 20210623
```

If `month()` isn’t included in the format and `day()` is, the format represents the day as the ordinal date.

The default [ISO8601FormatStyle](../iso8601formatstyle.md) includes the day.

For more information about formatting dates, see the [FormatStyle](../formatstyle.md).

## See Also

### Modifying Dates in an ISO 8601 Format Style

- [dateSeparator(_:)](<dateseparator(__).md>) — Modifies the ISO 8601 date format style to use the specified date separator.
- [year()](<year().md>) — Modifies the ISO 8601 date format style to include the year in the formatted output.
- [month()](<month().md>) — Modifies the ISO 8601 date format style to include the month in the formatted output.
- [weekOfYear()](<weekofyear().md>) — Modifies the ISO 8601 date format style to include the week of the year in the formatted output.
