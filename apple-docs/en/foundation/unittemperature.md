---
title: UnitTemperature
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unittemperature
source_url: 'https://developer.apple.com/documentation/foundation/unittemperature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unittemperature.json'
content_hash: 'sha256:2e5a9577ddd7e9d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitTemperature

<sub>Class</sub>

A unit of measure for temperature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitTemperature
```

## Overview

You typically use instances of [UnitTemperature](unittemperature.md) to represent specific quantities of temperature using the [NSMeasurement](nsmeasurement.md) class.

### Temperature

Temperature is a comparative measure of thermal energy. The SI unit for temperature is the kelvin (K), which is defined in terms of the triple point of water. Temperature is also commonly measured by degrees of various scales, including Celsius (°C) and Fahrenheit (°F).

The [UnitTemperature](unittemperature.md) class defines its [+ baseUnit](<dimension/baseunit().md>) to be [kelvin](unittemperature/kelvin.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients and constants:

| Name | Method | Symbol | Coefficient | Constant |
|---|---|---|---|---|
| Kelvin | [kelvin](unittemperature/kelvin.md) | K | `1` | `0` |
| Degree Celsius | [celsius](unittemperature/celsius.md) | °C | `1.0` | `273.15` |
| Degree Fahrenheit | [fahrenheit](unittemperature/fahrenheit.md) | °F | `0.55555555555556` | `255.37222222222427` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [kelvin](unittemperature/kelvin.md) — The kelvin unit of temperature.
- [celsius](unittemperature/celsius.md) — The degree Celsius unit of temperature.
- [fahrenheit](unittemperature/fahrenheit.md) — The degree Fahrenheit unit of temperature.

### Initializers

- [init(forLocale:usage:)](<unittemperature/init(forlocale_usage_).md>) — Creates a `UnitTemperature` which the specified `locale` prefers for the specific `usage`.

## See Also

### Energy, Heat, and Light

- [UnitEnergy](unitenergy.md) — A unit of measure for energy.
- [UnitPower](unitpower.md) — A unit of measure for power.
- [UnitIlluminance](unitilluminance.md) — A unit of measure for illuminance.
