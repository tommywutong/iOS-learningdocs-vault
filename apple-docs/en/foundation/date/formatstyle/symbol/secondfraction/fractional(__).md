---
title: 'fractional(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/symbol/secondfraction/fractional(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/secondfraction/fractional(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/secondfraction/fractional%28_%3A%29.json'
content_hash: 'sha256:41f03585613cfc6b'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [SecondFraction](../secondfraction.md)

# fractional(_:)

<sub>Type Method</sub>

Creates a custom format style representing the fractional seconds component of a date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func fractional(_ val: Int) -> Date.FormatStyle.Symbol.SecondFraction
```

## Parameters

- `val` — Length of the string representation of the fractional seconds component.

## Return Value

Returns the numerical representation of the fractional component of the second.

## See Also

### Modifying a Second Fraction

- [milliseconds(_:)](<milliseconds(__).md>) — Creates a custom format style representing the milliseconds elapsed in a day.
