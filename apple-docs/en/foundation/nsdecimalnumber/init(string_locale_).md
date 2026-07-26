---
title: 'init(string:locale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/init(string:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/init(string:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/init%28string%3Alocale%3A%29.json'
content_hash: 'sha256:03362733598b9712'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# init(string:locale:)

<sub>Initializer</sub>

Initializes a decimal number so that its value is equivalent to that in a given numeric string, interpreted using a given locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(string numberValue: String?, locale: Any?)
```

## Parameters

- `numberValue` — A numeric string. Besides digits, `numberValue` can include an initial `+` or `–`; a single `E` or `e`, to indicate the exponent of a number in scientific notation; and a single decimal separator character to divide the fractional from the integral part of the number.

- `locale` — A dictionary that defines the locale (specifically the [NSLocaleDecimalSeparator](../nslocale/key/decimalseparator.md)) to use to interpret the number in `numberValue`.

## Discussion

The locale parameter determines whether the `decimalSeparator` is a period (like in the United States) or a comma (like in France).

The following strings show examples of acceptable values for `numberValue`:

- `2500.6` (or `2500,6`, depending on locale)
- `–2500.6` (or `–2500,6`)
- `–2.5006e3` (or `–2,5006e3`)
- `–2.5006E3` (or `–2,5006E3`)

The following strings are unacceptable:

- `2,500.6`
- `2500 3/5`
- `2.5006x10e3`
- `two thousand five hundred and six tenths`

## See Also

### Initializing a Decimal Number

- [- initWithDecimal:](<init(decimal_).md>) — Initializes a decimal number to represent a given decimal.
- [- initWithMantissa:exponent:isNegative:](<init(mantissa_exponent_isnegative_).md>) — Initializes a decimal number using the given mantissa, exponent, and sign.
- [- initWithString:](<init(string_).md>) — Initializes a decimal number so that its value is equivalent to that in a given numeric string.
