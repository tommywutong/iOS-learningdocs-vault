---
title: 'string(from:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dateintervalformatter/string(from:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter/string(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter/string%28from%3Ato%3A%29.json'
content_hash: 'sha256:2a4d70e9859ee37c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateIntervalFormatter](../dateintervalformatter.md)

# string(from:to:)

<sub>Instance Method</sub>

Returns a formatted string based on the specified start and end dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from fromDate: Date, to toDate: Date) -> String
```

## Parameters

- `fromDate` — The start date. This date appears first in the resulting string.

- `toDate` — The end date. This date appears last after the hyphen in the resulting string.

## Return Value

A formatted string representing the specified date interval.

## Discussion

The formatter includes both `fromDate` and `toDate` in the resulting string only when there is enough of a difference in their values to warrant the inclusion of both. If the date and time difference cannot be adequately displayed, the formatter displays one date value. For example, if the [timeStyle](timestyle.md) property was set to [NSDateIntervalFormatterNoStyle](style/none.md), the two dates would need to be at least one day apart in order for both to be displayed.
