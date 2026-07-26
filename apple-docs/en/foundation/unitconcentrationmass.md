---
title: UnitConcentrationMass
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitconcentrationmass
source_url: 'https://developer.apple.com/documentation/foundation/unitconcentrationmass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitconcentrationmass.json'
content_hash: 'sha256:c9058071e7701a09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitConcentrationMass

<sub>Class</sub>

A unit of measure for concentration of mass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitConcentrationMass
```

## Overview

You typically use instances of [UnitConcentrationMass](unitconcentrationmass.md) to represent specific quantities of concentration using the [NSMeasurement](nsmeasurement.md) class.

### Concentration of Mass

Concentration is the abundance of a constituent within a volume. Concentration can be expressed by SI derived units in terms of kilograms per cubic meter (kg/m3).

The [UnitConcentrationMass](unitconcentrationmass.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [gramsPerLiter](unitconcentrationmass/gramsperliter.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Grams Per Liter | [gramsPerLiter](unitconcentrationmass/gramsperliter.md) | g/L | `1` |
| Milligrams Per Deciliter | [milligramsPerDeciliter](unitconcentrationmass/milligramsperdeciliter.md) | mg/dL | `0.01` |
| Millimoles Per Liter | [+ millimolesPerLiterWithGramsPerMole:](<unitconcentrationmass/millimolesperliter(withgramspermole_).md>) | mmol/L | `18 * gramsPerMole` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [gramsPerLiter](unitconcentrationmass/gramsperliter.md) — The grams per liter unit of concentration.
- [milligramsPerDeciliter](unitconcentrationmass/milligramsperdeciliter.md) — The milligrams per deciliter unit of concentration.
- [+ millimolesPerLiterWithGramsPerMole:](<unitconcentrationmass/millimolesperliter(withgramspermole_).md>) — Returns the millimoles per liter unit with the specified number of grams per mole.

## See Also

### Concentration and Dispersion

- [UnitDispersion](unitdispersion.md) — A unit of measure for specific quantities of dispersion.
