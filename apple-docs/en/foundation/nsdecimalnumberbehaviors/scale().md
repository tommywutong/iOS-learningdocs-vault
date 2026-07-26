---
title: scale()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumberbehaviors/scale()
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors/scale()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumberbehaviors/scale%28%29.json'
content_hash: 'sha256:b432c90cd588ea29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumberBehaviors](../nsdecimalnumberbehaviors.md)

# scale()

<sub>Instance Method</sub>

Returns the number of digits allowed after the decimal separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scale() -> Int16
```

## Return Value

The number of digits allowed after the decimal separator.

## Discussion

This method limits the precision of the values returned by `NSDecimalNumber`’s `decimalNumberBy...` methods. If [- scale](<scale().md>) returns a negative value, it affects the digits before the decimal separator as well. If [- scale](<scale().md>) returns `NSDecimalNoScale`, the number of digits is unlimited.

Assuming that [- roundingMode](<roundingmode().md>) returns `NSRoundPlain`, different values of [- scale](<scale().md>) have the following effects on the number 123.456:

| Scale | Return Value |
|---|---|
| `NSDecimalNoScale` | 123.456 |
| 2 | 123.45 |
| 0 | 123 |
| –2 | 100 |

## See Also

### Rounding

- [- roundingMode](<roundingmode().md>) — Returns the way that `NSDecimalNumber`’s `decimalNumberBy...` methods round their return values.
