---
title: UnitElectricResistance
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitelectricresistance
source_url: 'https://developer.apple.com/documentation/foundation/unitelectricresistance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitelectricresistance.json'
content_hash: 'sha256:cdb4ecc1d5fa1d58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitElectricResistance

<sub>Class</sub>

A unit of measure for electric resistance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitElectricResistance
```

## Overview

You typically use instances of [UnitElectricResistance](unitelectricresistance.md) to represent specific quantities of electric resistance using the [NSMeasurement](nsmeasurement.md) class.

### Electric Resistance

Electric resistance is the difficulty of passing an electric current through a conductor. The SI unit for electric resistance is the ohm (Ω), which is derived as the electric resistance that produces one ampere of current between two points in conductor with one volt of electric potential difference (1Ω = 1V/1A).

The [UnitElectricResistance](unitelectricresistance.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [ohms](unitelectricresistance/ohms.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Megaohms | [megaohms](unitelectricresistance/megaohms.md) | MΩ | `1000000.0` |
| Kiloohms | [kiloohms](unitelectricresistance/kiloohms.md) | kΩ | `1000.0` |
| Ohms | [ohms](unitelectricresistance/ohms.md) | Ω | `1.0` |
| Milliohms | [milliohms](unitelectricresistance/milliohms.md) | mΩ | `0.001` |
| Microohms | [microohms](unitelectricresistance/microohms.md) | µΩ | `0.000001` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [megaohms](unitelectricresistance/megaohms.md) — The megaohms unit of electric resistance.
- [kiloohms](unitelectricresistance/kiloohms.md) — The kiloohms unit of electric resistance.
- [ohms](unitelectricresistance/ohms.md) — The ohms unit of electric resistance.
- [milliohms](unitelectricresistance/milliohms.md) — The milliohms unit of electric resistance.
- [microohms](unitelectricresistance/microohms.md) — The microohms unit of electric resistance.

## See Also

### Electricity

- [UnitElectricCharge](unitelectriccharge.md) — A unit of measure for electric charge.
- [UnitElectricCurrent](unitelectriccurrent.md) — A unit of measure for electric current.
- [UnitElectricPotentialDifference](unitelectricpotentialdifference.md) — A unit of measure for electric potential difference.
