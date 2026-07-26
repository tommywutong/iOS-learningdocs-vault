---
title: twoDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/second/twodigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/second/twodigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/second/twodigits.json'
content_hash: 'sha256:171fd92678787e52'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Second](../second.md)

# twoDigits

<sub>Type Property</sub>

The custom format style that conveys a two-digit numeric second, zero-padded if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var twoDigits: Date.FormatStyle.Symbol.Second { get }
```

## Discussion

This style represents the seconds field like `01` or `18`.

## See Also

### Modifying a Second

- [defaultDigits](defaultdigits.md) — The custom format style that conveys the minimum number of digits that represents the numeric second.
