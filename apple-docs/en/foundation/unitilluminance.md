---
title: UnitIlluminance
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitilluminance
source_url: 'https://developer.apple.com/documentation/foundation/unitilluminance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitilluminance.json'
content_hash: 'sha256:daa1f0c9481350a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitIlluminance

<sub>Class</sub>

A unit of measure for illuminance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitIlluminance
```

## Overview

You typically use instances of [UnitIlluminance](unitilluminance.md) to represent specific quantities of illuminance using the [NSMeasurement](nsmeasurement.md) class.

### Illuminance

Illuminance is the luminous flux incident on a surface. The SI unit for illuminance is the lux (lx), which is derived as one lumen per square meter (1lm / 1m2).

The [UnitIlluminance](unitilluminance.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [lux](unitilluminance/lux.md).

| Name | Method | Symbol |
|---|---|---|
| Lux | [lux](unitilluminance/lux.md) | lx |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accesing Predefined Units

- [lux](unitilluminance/lux.md) — The lux unit of illuminance.

## See Also

### Energy, Heat, and Light

- [UnitEnergy](unitenergy.md) — A unit of measure for energy.
- [UnitPower](unitpower.md) — A unit of measure for power.
- [UnitTemperature](unittemperature.md) — A unit of measure for temperature.
