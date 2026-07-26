---
title: defaultDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/minute/defaultdigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/minute/defaultdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/minute/defaultdigits.json'
content_hash: 'sha256:f148d94cc8812019'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Minute](../minute.md)

# defaultDigits

<sub>Type Property</sub>

The custom minute format style showing the minimum number of digits that represents the numeric minute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultDigits: Date.FormatStyle.Symbol.Minute { get }
```

## Discussion

For example, this style represents one minute past the hour as `1`, and eighteen past as `18`.

## See Also

### Modifying a Minute

- [twoDigits](twodigits.md) — The custom format style that shows the two-digit numeric minute, zero-padded if necessary.
