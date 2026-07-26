---
title: DateIntervalFormatter.Style.long
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateintervalformatter/style/long
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter/style/long'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter/style/long.json'
content_hash: 'sha256:430ce7cf216a890b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DateIntervalFormatter](../../dateintervalformatter.md) · [Style](../style.md)

# DateIntervalFormatter.Style.long

<sub>Case</sub>

A long length date or time format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case long
```

## Discussion

For dates, this style displays the numerical day and year and a spelled out version of the month using a format appropriate for the current locale. For example, formatting the date January 15, 2015 with this style results in the value “January 15, 2015” for US English and the value “15. Januar 2015” for German.

For times, this style displays hours, minutes, seconds, and time zone information using a format appropriate for the current locale. For example, 12 hours, 33 minutes, and 29 seconds in the afternoon using a 12-hour clock and the Pacific Time Zone results in the value “12:33:29 PM PST” for US English without daylight savings in effect and “12:33:29 GMT-8” for German.

## See Also

### Constants

- [NSDateIntervalFormatterNoStyle](none.md) — No information for the date or time. Use this style when you do not want to include date or time information in the resulting string.
- [NSDateIntervalFormatterShortStyle](short.md) — An abbreviated date or time format.
- [NSDateIntervalFormatterMediumStyle](medium.md) — A medium length date or time format.
- [NSDateIntervalFormatterFullStyle](full.md) — A fully spelled out date or time format.
