---
title: 'decimalNumberWithDecimal:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/decimalnumberwithdecimal:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/decimalnumberwithdecimal:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/decimalnumberwithdecimal%3A.json'
content_hash: 'sha256:11397cab4ecf785b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# decimalNumberWithDecimal:

<sub>Type Method</sub>

Creates and returns a decimal number equivalent to a given decimal structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSDecimalNumber *) decimalNumberWithDecimal:(NSDecimal) dcm;
```

## Parameters

- `dcm` — An `NSDecimal` structure that specifies the value for the new decimal number object.

## Return Value

An `NSDecimalNumber` object  equivalent to `dcm`.

## Discussion

You can initialize `dcm` programmatically or generate it using the `NSScanner` method, [- scanDecimal:](<../scanner/scandecimal(__).md>)

## See Also

### Related Documentation

- [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i)

### Creating a Decimal Number

- [decimalNumberWithMantissa:exponent:isNegative:](decimalnumberwithmantissa_exponent_isnegative_.md) — Creates and returns a decimal number equivalent to the number specified by the arguments.
- [decimalNumberWithString:](decimalnumberwithstring_.md) — Creates a decimal number whose value is equivalent to that in a given numeric string.
- [decimalNumberWithString:locale:](decimalnumberwithstring_locale_.md) — Creates a decimal number whose value is equivalent to that in a given numeric string, interpreted using a given locale.
- [one](one.md) — A decimal number equivalent to the number 1.0.
- [zero](zero.md) — A decimal number equivalent to the number 0.0.
- [notANumber](notanumber.md) — A decimal number that specifies no number.
