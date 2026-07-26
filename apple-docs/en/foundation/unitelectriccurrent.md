---
title: UnitElectricCurrent
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitelectriccurrent
source_url: 'https://developer.apple.com/documentation/foundation/unitelectriccurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitelectriccurrent.json'
content_hash: 'sha256:a91a2c569d982abe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitElectricCurrent

<sub>Class</sub>

A unit of measure for electric current.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitElectricCurrent
```

## Overview

You typically use instances of [UnitElectricCurrent](unitelectriccurrent.md) to represent specific quantities of electric current using the [NSMeasurement](nsmeasurement.md) class.

### Electric Current

Electric current is the flow of electric charge. The SI unit for electric current is the ampere (A), which is defined in terms the production of electromagnetic force between two parallel linear conductors. It can also be expressed as the flow of one coulomb per second (1A = 1C / s).

The [UnitElectricCurrent](unitelectriccurrent.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [amperes](unitelectriccurrent/amperes.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Megaamperes | [megaamperes](unitelectriccurrent/megaamperes.md) | MA | `1000000.0` |
| Kiloamperes | [kiloamperes](unitelectriccurrent/kiloamperes.md) | kA | `1000.0` |
| Amperes | [amperes](unitelectriccurrent/amperes.md) | A | `1.0` |
| Milliamperes | [milliamperes](unitelectriccurrent/milliamperes.md) | mA | `0.001` |
| Microamperes | [microamperes](unitelectriccurrent/microamperes.md) | µA | `0.000001` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [megaamperes](unitelectriccurrent/megaamperes.md) — The megaamperes unit of electric current.
- [kiloamperes](unitelectriccurrent/kiloamperes.md) — The kiloamperes unit of electric current.
- [amperes](unitelectriccurrent/amperes.md) — The amperes unit of electric current.
- [milliamperes](unitelectriccurrent/milliamperes.md) — The milliamperes unit of electric current.
- [microamperes](unitelectriccurrent/microamperes.md) — The microamperes unit of electric current.

## See Also

### Electricity

- [UnitElectricCharge](unitelectriccharge.md) — A unit of measure for electric charge.
- [UnitElectricPotentialDifference](unitelectricpotentialdifference.md) — A unit of measure for electric potential difference.
- [UnitElectricResistance](unitelectricresistance.md) — A unit of measure for electric resistance.
