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
doc_path: /documentation/foundation/date/formatstyle/symbol/dayofyear/twodigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayofyear/twodigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/dayofyear/twodigits.json'
content_hash: 'sha256:8fd19c714740c47b'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [DayOfYear](../dayofyear.md)

# twoDigits

<sub>Type Property</sub>

Custom format style portraying the two-digit numeric day of the year, zero-padded if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var twoDigits: Date.FormatStyle.Symbol.DayOfYear { get }
```

## Discussion

For example, `01`, `18`, `317`.

## See Also

### Modifying a Day of Year Value

- [defaultDigits](defaultdigits.md) — Custom format style portraying the minimum number of digits that represents the numeric day of the year.
- [threeDigits](threedigits.md) — Custom format style portraying the three-digit numeric day of the year, zero-padded if necessary.
