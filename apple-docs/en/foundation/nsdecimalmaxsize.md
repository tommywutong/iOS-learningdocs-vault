---
title: NSDecimalMaxSize
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalmaxsize
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalmaxsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalmaxsize.json'
content_hash: 'sha256:66363b1a605ad8ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalMaxSize

<sub>Global Variable</sub>

The maximum size of [Decimal](decimal.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSDecimalMaxSize: Int32 { get }
```

## Discussion

Gives a precision of at least 38 decimal digits, 128 binary positions.

## See Also

### Getting particular decimals

- [greatestFiniteMagnitude](decimal/greatestfinitemagnitude.md) — The decimal that contains the largest possible non-infinite magnitude for the underlying representation.
- [leastFiniteMagnitude](decimal/leastfinitemagnitude.md) — The decimal that contains the smallest possible non-infinite magnitude for the underlying representation.
- [leastNonzeroMagnitude](decimal/leastnonzeromagnitude.md) — The decimal value that represents the smallest possible non-zero value for the underlying representation.
- [leastNormalMagnitude](decimal/leastnormalmagnitude.md) — The decimal value that represents the smallest possible normal magnitude for the underlying representation.
- [pi](decimal/pi.md) — The mathematical constant pi.
- [nan](decimal/nan.md) — The value that represents “not a number.”
- [quietNaN](decimal/quietnan.md) — A quiet representation of not-a-number.
- [radix](decimal/radix.md) — The radix used by decimal numbers.
- [NSDecimalNoScale](nsdecimalnoscale.md) — Specifies that the number of digits allowed after the decimal separator in a decimal number should not be limited.
