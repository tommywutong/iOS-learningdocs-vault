---
title: 'decimalNumberWithMantissa:exponent:isNegative:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/decimalnumberwithmantissa:exponent:isnegative:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/decimalnumberwithmantissa:exponent:isnegative:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/decimalnumberwithmantissa%3Aexponent%3Aisnegative%3A.json'
content_hash: 'sha256:24a0287e726d2d46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# decimalNumberWithMantissa:exponent:isNegative:

<sub>Type Method</sub>

Creates and returns a decimal number equivalent to the number specified by the arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSDecimalNumber *) decimalNumberWithMantissa:(unsigned long long) mantissa exponent:(short) exponent isNegative:(BOOL) flag;
```

## Parameters

- `mantissa` — The mantissa for the new decimal number object.

- `exponent` — The exponent for the new decimal number object.

- `flag` — A Boolean value that specifies whether the sign of the number is negative.

## Discussion

The arguments express a number in a kind of scientific notation that requires the mantissa to be an integer. So, for example, if the number to be represented is `–12.345`, it is expressed as `12345x10^–3`—`mantissa` is `12345`; `exponent` is `–3`; and `flag` is [true](../../swift/true.md), as illustrated by the following example.

```objc
NSDecimalNumber *number = [NSDecimalNumber decimalNumberWithMantissa:12345
                                           exponent:-3
                                           isNegative:YES];
```

> [!important] Important
> `NSDecimalNumber` cannot represent negative zero. Initializing an `NSDecimalNumber` by passing 0 to `mantissa` and `exponent` and [true](../../swift/true.md) to `flag` returns [notANumber](notanumber.md) (`NaN`).

## See Also

### Creating a Decimal Number

- [decimalNumberWithDecimal:](decimalnumberwithdecimal_.md) — Creates and returns a decimal number equivalent to a given decimal structure.
- [decimalNumberWithString:](decimalnumberwithstring_.md) — Creates a decimal number whose value is equivalent to that in a given numeric string.
- [decimalNumberWithString:locale:](decimalnumberwithstring_locale_.md) — Creates a decimal number whose value is equivalent to that in a given numeric string, interpreted using a given locale.
- [one](one.md) — A decimal number equivalent to the number 1.0.
- [zero](zero.md) — A decimal number equivalent to the number 0.0.
- [notANumber](notanumber.md) — A decimal number that specifies no number.
