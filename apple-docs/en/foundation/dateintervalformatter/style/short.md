---
title: DateIntervalFormatter.Style.short
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateintervalformatter/style/short
source_url: 'https://developer.apple.com/documentation/foundation/dateintervalformatter/style/short'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateintervalformatter/style/short.json'
content_hash: 'sha256:4d23f272686c17f7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DateIntervalFormatter](../../dateintervalformatter.md) · [Style](../style.md)

# DateIntervalFormatter.Style.short

<sub>Case</sub>

An abbreviated date or time format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case short
```

## Discussion

For dates, this style displays the day, month, and year in numerical form using a format appropriate for the current locale. For example, formatting the date January 15, 2015 with this style results in the value “1/15/15” for US English and the value “15.1.15” for German.

For times, this style displays hours and minutes using a format appropriate for the current locale. For example, 12 hours and 33 minutes in the afternoon using a 12-hour clock results in the value “12:33 PM” for US English format and “12:33 nachm.” for German.

## See Also

### Constants

- [NSDateIntervalFormatterNoStyle](none.md) — No information for the date or time. Use this style when you do not want to include date or time information in the resulting string.
- [NSDateIntervalFormatterMediumStyle](medium.md) — A medium length date or time format.
- [NSDateIntervalFormatterLongStyle](long.md) — A long length date or time format.
- [NSDateIntervalFormatterFullStyle](full.md) — A fully spelled out date or time format.
