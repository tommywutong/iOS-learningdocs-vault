---
title: 'init(coefficient:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/unitconverterlinear/init(coefficient:)'
source_url: 'https://developer.apple.com/documentation/foundation/unitconverterlinear/init(coefficient:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitconverterlinear/init%28coefficient%3A%29.json'
content_hash: 'sha256:6e636124f6c0cc6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UnitConverterLinear](../unitconverterlinear.md)

# init(coefficient:)

<sub>Initializer</sub>

Initializes the unit converter with the coefficient you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(coefficient: Double)
```

## Parameters

- `coefficient` — The coefficient used in the linear unit conversion calculation.

## Return Value

A unit converter initialized with the specified coefficient.

## Discussion

Calling this initializer is equivalent to calling [- initWithCoefficient:constant:](<init(coefficient_constant_).md>), passing `0` for the `constant` parameter.

## See Also

### Creating Unit Converters

- [- initWithCoefficient:constant:](<init(coefficient_constant_).md>) — Creates a unit converter with the coefficient and constant you specify.
