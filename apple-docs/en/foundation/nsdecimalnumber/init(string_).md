---
title: 'init(string:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/init(string:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/init(string:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/init%28string%3A%29.json'
content_hash: 'sha256:9ae6aebab66b127a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# init(string:)

<sub>Initializer</sub>

Initializes a decimal number so that its value is equivalent to that in a given numeric string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(string numberValue: String?)
```

## Parameters

- `numberValue` — A numeric string. Besides digits, `numberValue` can include an initial `+` or `–`; a single `E` or `e`, to indicate the exponent of a number in scientific notation; and a single decimal separator character to divide the fractional from the integral part of the number. For a listing of acceptable and unacceptable strings, see [- initWithString:locale:](<init(string_locale_).md>).

## Discussion

Don’t use this initializer if `numberValue` has a fractional part, since the lack of a locale makes handling the decimal separator ambiguous. The separator is a period in some locales (like in the United States) and a comma in others (such as France).

To parse a numeric string with a fractional part, use [- initWithString:locale:](<init(string_locale_).md>) instead. When working with numeric representations with a known format, pass a fixed locale to ensure consistent results independent of the user’s current device settings. For localized parsing that uses the user’s current device settings, pass [currentLocale](../nslocale/current.md).

## See Also

### Initializing a Decimal Number

- [- initWithDecimal:](<init(decimal_).md>) — Initializes a decimal number to represent a given decimal.
- [- initWithMantissa:exponent:isNegative:](<init(mantissa_exponent_isnegative_).md>) — Initializes a decimal number using the given mantissa, exponent, and sign.
- [- initWithString:locale:](<init(string_locale_).md>) — Initializes a decimal number so that its value is equivalent to that in a given numeric string, interpreted using a given locale.
