---
title: 'init(mantissa:exponent:isNegative:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/init(mantissa:exponent:isnegative:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/init(mantissa:exponent:isnegative:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/init%28mantissa%3Aexponent%3Aisnegative%3A%29.json'
content_hash: 'sha256:ba12b84fd15098c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# init(mantissa:exponent:isNegative:)

<sub>Initializer</sub>

Initializes a decimal number using the given mantissa, exponent, and sign.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(mantissa: UInt64, exponent: Int16, isNegative flag: Bool)
```

## Parameters

- `mantissa` — The mantissa for the new decimal number object.

- `exponent` — The exponent for the new decimal number object.

- `flag` — A Boolean value that specifies whether the sign of the number is negative.

## Return Value

An `NSDecimalNumber` object initialized using the given mantissa, exponent, and sign.

## Discussion

The arguments express a number in a type of scientific notation that requires the mantissa to be an integer. So, for example, if the number to be represented is 1.23, it is expressed as 123x10^–2—`mantissa` is 123; `exponent` is –2; and `isNegative`, which refers to the sign of the mantissa, is [false](../../swift/false.md).

## See Also

### Initializing a Decimal Number

- [- initWithDecimal:](<init(decimal_).md>) — Initializes a decimal number to represent a given decimal.
- [- initWithString:](<init(string_).md>) — Initializes a decimal number so that its value is equivalent to that in a given numeric string.
- [- initWithString:locale:](<init(string_locale_).md>) — Initializes a decimal number so that its value is equivalent to that in a given numeric string, interpreted using a given locale.
