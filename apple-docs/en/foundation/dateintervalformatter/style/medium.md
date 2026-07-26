---
title: DateIntervalFormatter.Style.medium
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateintervalformatter/style/medium
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter/style/medium'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter/style/medium.json'
content_hash: 'sha256:f3e9498d31f3ee7c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DateIntervalFormatter](../../dateintervalformatter.md) · [Style](../style.md)

# DateIntervalFormatter.Style.medium

<sub>Case</sub>

A medium length date or time format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case medium
```

## Discussion

For dates, this style displays the numerical day and year and an abbreviated spelling of the month using a format appropriate for the current locale. For example, formatting the date January 15, 2015 with this style results in the value “Jan 15, 2015” for US English and the value “15. Jan. 2015” for German.

For times, this style displays hours, minutes, and seconds using a format appropriate for the current locale. For example, 12 hours, 33 minutes, and 29 seconds in the afternoon using a 12-hour clock results in the value “12:33:29 PM” for US English 12-hour format and “12:33:29 nachm.” for German.

## See Also

### Constants

- [NSDateIntervalFormatterNoStyle](none.md) — No information for the date or time. Use this style when you do not want to include date or time information in the resulting string.
- [NSDateIntervalFormatterShortStyle](short.md) — An abbreviated date or time format.
- [NSDateIntervalFormatterLongStyle](long.md) — A long length date or time format.
- [NSDateIntervalFormatterFullStyle](full.md) — A fully spelled out date or time format.
