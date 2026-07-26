---
title: dayOfYear
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponents/dayofyear
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/dayofyear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/dayofyear.json'
content_hash: 'sha256:9fc873dd5b9e1ce3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# dayOfYear

<sub>Instance Property</sub>

A day of the year. For example, in the Gregorian calendar, can go from 1 to 365 or 1 to 366 in leap years.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dayOfYear: Int? { get set }
```

## Discussion

> [!note] Note
> This value is interpreted in the context of the calendar in which it is used.
