---
title: UnitElectricPotentialDifference
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitelectricpotentialdifference
source_url: 'https://developer.apple.com/documentation/foundation/unitelectricpotentialdifference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitelectricpotentialdifference.json'
content_hash: 'sha256:6dcac180b8291dbb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitElectricPotentialDifference

<sub>Class</sub>

A unit of measure for electric potential difference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitElectricPotentialDifference
```

## Overview

You typically use instances of [UnitElectricPotentialDifference](unitelectricpotentialdifference.md) to represent specific quantities of electric potential difference using the [NSMeasurement](nsmeasurement.md) class.

### Electric Potential Difference

Electric potential difference is the amount of electric potential energy of a point charge at a point in space. The SI unit for electric potential difference is the volt (V), which is derived as the difference in electric potential energy between two points of a linear conductor when an electric current of one ampere dissipates one watt of power between those points (1V = 1W/1A).

The [UnitElectricPotentialDifference](unitelectricpotentialdifference.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [volts](unitelectricpotentialdifference/volts.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Megavolts | [megavolts](unitelectricpotentialdifference/megavolts.md) | MV | `1000000.0` |
| Kilovolts | [kilovolts](unitelectricpotentialdifference/kilovolts.md) | kV | `1000.0` |
| Volts | [volts](unitelectricpotentialdifference/volts.md) | V | `1.0` |
| Millivolts | [millivolts](unitelectricpotentialdifference/millivolts.md) | mV | `0.001` |
| Microvolts | [microvolts](unitelectricpotentialdifference/microvolts.md) | µV | `0.000001` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [megavolts](unitelectricpotentialdifference/megavolts.md) — The megavolts unit of electric potential difference.
- [kilovolts](unitelectricpotentialdifference/kilovolts.md) — The kilovolts unit of electric potential difference.
- [volts](unitelectricpotentialdifference/volts.md) — The volts unit of electric potential difference.
- [millivolts](unitelectricpotentialdifference/millivolts.md) — The millivolts unit of electric potential difference.
- [microvolts](unitelectricpotentialdifference/microvolts.md) — The microvolts unit of electric potential difference.

## See Also

### Electricity

- [UnitElectricCharge](unitelectriccharge.md) — A unit of measure for electric charge.
- [UnitElectricCurrent](unitelectriccurrent.md) — A unit of measure for electric current.
- [UnitElectricResistance](unitelectricresistance.md) — A unit of measure for electric resistance.
