---
title: baseUnit()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dimension/baseunit()
source_url: 'https://developer.apple.com/documentation/foundation/dimension/baseunit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dimension/baseunit%28%29.json'
content_hash: 'sha256:27010d36997a7642'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Dimension](../dimension.md)

# baseUnit()

<sub>Type Method</sub>

Returns the base unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func baseUnit() -> Self
```

## Return Value

An `NSDimension` subclass object from which all other units provided by the subclass are defined.

## Discussion

The default implementation returns `nil` to indicate that the `NSDimension` class should not be used directly.

When implementing a subclass, you should return a unit converter that returns the inputted value for both the `baseUnitValueFromValue:` and `valueFromBaseUnitValue:` methods. You can create a unit converter for a base unit using the [UnitConverterLinear](../unitconverterlinear.md) [- initWithCoefficient:](<../unitconverterlinear/init(coefficient_).md>) initializer, passing `1` as the coefficient.
