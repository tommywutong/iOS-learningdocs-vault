---
title: UnitEnergy
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitenergy
source_url: 'https://developer.apple.com/documentation/foundation/unitenergy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitenergy.json'
content_hash: 'sha256:4a524aa3d544e5c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitEnergy

<sub>Class</sub>

A unit of measure for energy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitEnergy
```

## Overview

You typically use instances of [UnitEnergy](unitenergy.md) to represent specific quantities of energy using the [NSMeasurement](nsmeasurement.md) class.

### Energy

Energy is a fundamental property of matter than can be transferred and converted into different forms, such as kinetic, electric, and thermal. The SI unit for energy is the joule (J), which is derived as the work of one meter of displacement in the direction of a force of one newton (1J = 1N ∙ 1m). It can also be derived as the work required to displace an electric charge of one coulomb through an electrical potential difference of one volt (1J = 1C ∙ 1V), or the work required to produce one watt of power for one second (1J = 1W ∙ 1s). Energy is also commonly expressed in terms of the calorie (cal), or the energy needed to raise the temperature of one gram of water by one degree Celsius at a pressure of one atmosphere (1cal ≡ 4.184J).

The [UnitEnergy](unitenergy.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [joules](unitenergy/joules.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Kilojoules | [kilojoules](unitenergy/kilojoules.md) | kJ | `1000.0` |
| Joules | [joules](unitenergy/joules.md) | J | `1.0` |
| Kilocalories | [kilocalories](unitenergy/kilocalories.md) | kCal | `4184.0` |
| Calories | [calories](unitenergy/calories.md) | cal | `4.184` |
| Kilowatt Hours | [kilowattHours](unitenergy/kilowatthours.md) | kWh | `3600000.0` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [kilojoules](unitenergy/kilojoules.md) — The kilojoules unit of energy.
- [joules](unitenergy/joules.md) — The joules unit of energy.
- [kilocalories](unitenergy/kilocalories.md) — The kilocalories unit of energy.
- [calories](unitenergy/calories.md) — The calories unit of energy.
- [kilowattHours](unitenergy/kilowatthours.md) — The kilowatt hours unit of energy.

### Classes

- [EnergyKit](unitenergy/energykit.md)

### Initializers

- [init(forLocale:usage:)](<unitenergy/init(forlocale_usage_).md>) — Creates a `UnitEnergy` which the specified `locale` prefers for the specific `usage`.

## See Also

### Energy, Heat, and Light

- [UnitPower](unitpower.md) — A unit of measure for power.
- [UnitTemperature](unittemperature.md) — A unit of measure for temperature.
- [UnitIlluminance](unitilluminance.md) — A unit of measure for illuminance.
