---
title: 'init(roundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumberhandler/init(roundingmode:scale:raiseonexactness:raiseonoverflow:raiseonunderflow:raiseondividebyzero:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumberhandler/init(roundingmode:scale:raiseonexactness:raiseonoverflow:raiseonunderflow:raiseondividebyzero:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumberhandler/init%28roundingmode%3Ascale%3Araiseonexactness%3Araiseonoverflow%3Araiseonunderflow%3Araiseondividebyzero%3A%29.json'
content_hash: 'sha256:479301488c9b7ccb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumberHandler](../nsdecimalnumberhandler.md)

# init(roundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:)

<sub>Initializer</sub>

Returns an `NSDecimalNumberHandler` object initialized so it behaves as specified by the method’s arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(roundingMode: NSDecimalNumber.RoundingMode, scale: Int16, raiseOnExactness exact: Bool, raiseOnOverflow overflow: Bool, raiseOnUnderflow underflow: Bool, raiseOnDivideByZero divideByZero: Bool)
```

## Parameters

- `roundingMode` — The rounding mode to use. There are four possible values: `NSRoundUp`, `NSRoundDown`, `NSRoundPlain`, and `NSRoundBankers`.

- `scale` — The number of digits a rounded value should have after its decimal point.

- `exact` — If [true](../../swift/true.md), in the event of an exactness error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method.

- `overflow` — If [true](../../swift/true.md), in the event of an overflow error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method

- `underflow` — If [true](../../swift/true.md), in the event of an underflow error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method

- `divideByZero` — If [true](../../swift/true.md), in the event of a divide by zero error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method

## Return Value

An initialized `NSDecimalNumberHandler` object initialized with customized behavior. The returned object might be different than the original receiver.

## Discussion

See the [NSDecimalNumberBehaviors](../nsdecimalnumberbehaviors.md) protocol specification for a complete explanation of the possible behaviors.
