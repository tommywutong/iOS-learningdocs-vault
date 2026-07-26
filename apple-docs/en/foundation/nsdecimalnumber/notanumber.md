---
title: notANumber
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumber/notanumber
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/notanumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/notanumber.json'
content_hash: 'sha256:bc2af9bc3cf8320e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# notANumber

<sub>Type Property</sub>

A decimal number that specifies no number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying class var notANumber: NSDecimalNumber { get }
```

## Return Value

An `NSDecimalNumber` object that specifies no number.

## Discussion

Any arithmetic method receiving [notANumber](notanumber.md) as an argument returns [notANumber](notanumber.md).

This value can be a useful way of handling non-numeric data in an input file. This method can also be a useful response to calculation errors. For more information on calculation errors, see the [- exceptionDuringOperation:error:leftOperand:rightOperand:](<../nsdecimalnumberbehaviors/exceptionduringoperation(__error_leftoperand_rightoperand_).md>) method description in the [NSDecimalNumberBehaviors](../nsdecimalnumberbehaviors.md) protocol specification.

## See Also

### Creating a Decimal Number

- [one](one.md) — A decimal number equivalent to the number 1.0.
- [zero](zero.md) — A decimal number equivalent to the number 0.0.
