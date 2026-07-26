---
title: 'decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumberhandler/decimalnumberhandlerwithroundingmode:scale:raiseonexactness:raiseonoverflow:raiseonunderflow:raiseondividebyzero:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumberhandler/decimalnumberhandlerwithroundingmode:scale:raiseonexactness:raiseonoverflow:raiseonunderflow:raiseondividebyzero:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumberhandler/decimalnumberhandlerwithroundingmode%3Ascale%3Araiseonexactness%3Araiseonoverflow%3Araiseonunderflow%3Araiseondividebyzero%3A.json'
content_hash: 'sha256:3a5c1662741f9784'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumberHandler](../nsdecimalnumberhandler.md)

# decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:

<sub>Type Method</sub>

Returns an `NSDecimalNumberHandler` object with customized behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) decimalNumberHandlerWithRoundingMode:(NSRoundingMode) roundingMode scale:(short) scale raiseOnExactness:(BOOL) exact raiseOnOverflow:(BOOL) overflow raiseOnUnderflow:(BOOL) underflow raiseOnDivideByZero:(BOOL) divideByZero;
```

## Parameters

- `roundingMode` — The rounding mode to use. There are four possible values: `NSRoundUp`, `NSRoundDown`, `NSRoundPlain`, and `NSRoundBankers`.

- `scale` — The number of digits a rounded value should have after its decimal point.

- `exact` — If [true](../../swift/true.md), in the event of an exactness error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method.

- `overflow` — If [true](../../swift/true.md), in the event of an overflow error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method

- `underflow` — If [true](../../swift/true.md), in the event of an underflow error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method

- `divideByZero` — If [true](../../swift/true.md), in the event of a divide by zero error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method

## Return Value

An `NSDecimalNumberHandler` object with customized behavior.

## Discussion

See the [NSDecimalNumberBehaviors](../nsdecimalnumberbehaviors.md) protocol specification for a complete explanation of the possible behaviors.

## See Also

### Creating a Decimal Number Handler

- [defaultDecimalNumberHandler](default.md) — Returns the default instance of `NSDecimalNumberHandler`.
