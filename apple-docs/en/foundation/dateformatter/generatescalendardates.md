---
title: generatesCalendarDates
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/generatescalendardates
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/generatescalendardates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/generatescalendardates.json'
content_hash: 'sha256:c4daf84d200a200c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# generatesCalendarDates

<sub>Instance Property</sub>

Indicates whether the formatter generates the deprecated calendar date type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var generatesCalendarDates: Bool { get set }
```

## Discussion

This property is [true](../../swift/true.md) if the formatter generates the deprecated [NSCalendarDate](../nscalendardate.md) type, and is [false](../../swift/false.md) otherwise. You should use [Date](../date.md) and [Calendar](../calendar.md) rather than [NSCalendarDate](../nscalendardate.md).
