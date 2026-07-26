---
title: NSDecimalNumberBehaviors
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumberbehaviors
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumberbehaviors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumberbehaviors.json'
content_hash: 'sha256:b01c1312ed16a504'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalNumberBehaviors

<sub>Protocol</sub>

A protocol that declares three methods that control the discretionary aspects of working with decimal numbers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSDecimalNumberBehaviors
```

## Overview

The [- scale](<nsdecimalnumberbehaviors/scale().md>) and [- roundingMode](<nsdecimalnumberbehaviors/roundingmode().md>) methods determine the precision of `NSDecimalNumber`’s return values and the way in which those values should be rounded to fit that precision. The [- exceptionDuringOperation:error:leftOperand:rightOperand:](<nsdecimalnumberbehaviors/exceptionduringoperation(__error_leftoperand_rightoperand_).md>) method determines the way in which an `NSDecimalNumber` object should handle different calculation errors.

For an example of a class that adopts the `NSDecimalBehaviors` protocol, see the specification for [NSDecimalNumberHandler](nsdecimalnumberhandler.md).

## Relationships

- **Conforming Types**: [NSDecimalNumberHandler](nsdecimalnumberhandler.md)

## Topics

### Rounding

- [- roundingMode](<nsdecimalnumberbehaviors/roundingmode().md>) — Returns the way that `NSDecimalNumber`’s `decimalNumberBy...` methods round their return values.
- [- scale](<nsdecimalnumberbehaviors/scale().md>) — Returns the number of digits allowed after the decimal separator.

### Handling errors

- [- exceptionDuringOperation:error:leftOperand:rightOperand:](<nsdecimalnumberbehaviors/exceptionduringoperation(__error_leftoperand_rightoperand_).md>) — Specifies what an `NSDecimalNumber` object will do when it encounters an error.

### Constants

- [RoundingMode](nsdecimalnumber/roundingmode.md) — These constants specify rounding behaviors.
- [CalculationError](nsdecimalnumber/calculationerror.md) — Calculation error constants used to describe an error in [- exceptionDuringOperation:error:leftOperand:rightOperand:](<nsdecimalnumberbehaviors/exceptionduringoperation(__error_leftoperand_rightoperand_).md>).

## See Also

### Managing Behavior

- [defaultBehavior](nsdecimalnumber/defaultbehavior.md) — The way arithmetic methods round off and handle error conditions.
- [NSDecimalNumberHandler](nsdecimalnumberhandler.md) — A class that adopts the decimal number behaviors protocol.
