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
doc_path: /documentation/foundation/date/formatstyle/symbol/minute/twodigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/minute/twodigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/minute/twodigits.json'
content_hash: 'sha256:6aa2c6ab76cb96fa'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Minute](../minute.md)

# twoDigits

<sub>Type Property</sub>

The custom format style that shows the two-digit numeric minute, zero-padded if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var twoDigits: Date.FormatStyle.Symbol.Minute { get }
```

## Discussion

For example, this style represents one minute past the hour as `01`, and eighteen past as `18`.

## See Also

### Modifying a Minute

- [defaultDigits](defaultdigits.md) — The custom minute format style showing the minimum number of digits that represents the numeric minute.
