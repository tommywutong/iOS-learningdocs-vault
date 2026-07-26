---
title: roundingMode()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumberbehaviors/roundingmode()
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors/roundingmode()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumberbehaviors/roundingmode%28%29.json'
content_hash: 'sha256:f04c8ac8ff13d5d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumberBehaviors](../nsdecimalnumberbehaviors.md)

# roundingMode()

<sub>Instance Method</sub>

Returns the way that `NSDecimalNumber`’s `decimalNumberBy...` methods round their return values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func roundingMode() -> NSDecimalNumber.RoundingMode
```

## Return Value

Returns the current rounding mode. See [RoundingMode](../nsdecimalnumber/roundingmode.md) for possible values.

## See Also

### Related Documentation

- [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i)

### Rounding

- [- scale](<scale().md>) — Returns the number of digits allowed after the decimal separator.
