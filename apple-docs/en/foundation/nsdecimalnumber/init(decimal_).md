---
title: 'init(decimal:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/init(decimal:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/init(decimal:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/init%28decimal%3A%29.json'
content_hash: 'sha256:f4a8911d16330570'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# init(decimal:)

<sub>Initializer</sub>

Initializes a decimal number to represent a given decimal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(decimal dcm: Decimal)
```

## Parameters

- `dcm` — The value of the new object.

## Return Value

An `NSDecimalNumber` object initialized to represent `dcm`.

## Discussion

This method is the designated initializer for `NSDecimalNumber`.

## See Also

### Initializing a Decimal Number

- [- initWithMantissa:exponent:isNegative:](<init(mantissa_exponent_isnegative_).md>) — Initializes a decimal number using the given mantissa, exponent, and sign.
- [- initWithString:](<init(string_).md>) — Initializes a decimal number so that its value is equivalent to that in a given numeric string.
- [- initWithString:locale:](<init(string_locale_).md>) — Initializes a decimal number so that its value is equivalent to that in a given numeric string, interpreted using a given locale.
