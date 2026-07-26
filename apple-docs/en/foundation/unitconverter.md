---
title: UnitConverter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitconverter
source_url: 'https://developer.apple.com/documentation/foundation/unitconverter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitconverter.json'
content_hash: 'sha256:916960e68663e182'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitConverter

<sub>Class</sub>

An abstract class that provides a description of how to convert a unit to and from the base unit of its dimension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitConverter
```

## Overview

For units that can be converted by a scale factor or linear equation, use the concrete subclass [UnitConverterLinear](unitconverterlinear.md).

### Subclassing Notes

[UnitConverter](unitconverter.md) is an abstract class that is intended for subclassing. You can implement your own subclass of [UnitConverter](unitconverter.md) to convert between units according to any desired mapping function. For example, units may be converted using a logarithmic, exponential, or quantile scale.

#### Methods to Override

All subclasses must fully implement the following methods:

- [- baseUnitValueFromValue:](<unitconverter/baseunitvalue(fromvalue_).md>)
- [- valueFromBaseUnitValue:](<unitconverter/value(frombaseunitvalue_).md>)

#### Alternatives to Subclassing

As stated above, most physical units can be converted using a linear equation with [UnitConverterLinear](unitconverterlinear.md). You should only create a custom subclass of [UnitConverter](unitconverter.md) for units that cannot be converted in this way.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UnitConverterLinear](unitconverterlinear.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Converting Between Units

- [- baseUnitValueFromValue:](<unitconverter/baseunitvalue(fromvalue_).md>) — For a given unit, returns the specified value of that unit in terms of the base unit of its dimension.
- [- valueFromBaseUnitValue:](<unitconverter/value(frombaseunitvalue_).md>) — For a given unit, returns the specified value of the base unit in terms of that unit.

## See Also

### Conversion

- [UnitConverterLinear](unitconverterlinear.md) — A description of how to convert between units using a linear equation.
