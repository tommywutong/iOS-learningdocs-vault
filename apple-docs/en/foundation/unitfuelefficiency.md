---
title: UnitFuelEfficiency
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitfuelefficiency
source_url: 'https://developer.apple.com/documentation/foundation/unitfuelefficiency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitfuelefficiency.json'
content_hash: 'sha256:9de00bc343851f40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitFuelEfficiency

<sub>Class</sub>

A unit of measure for fuel efficiency.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitFuelEfficiency
```

## Overview

You typically use instances of [UnitFuelEfficiency](unitfuelefficiency.md) to represent specific quantities of fuel efficiency using the [NSMeasurement](nsmeasurement.md) class.

### Fuel Efficiency

Fuel efficiency corresponds to the thermal efficiency of a process that converts the chemical potential energy of a fuel into kinetic energy. Fuel efficiency can be expressed by SI derived units in terms of cubic meters per meter (m3/m), but is more commonly expressed in terms of liters per kilometer (L/km) and miles per gallon (mpg).

The [UnitFuelEfficiency](unitfuelefficiency.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [litersPer100Kilometers](unitfuelefficiency/litersper100kilometers.md), and provides the following units:

| Name | Method | Symbol |
|---|---|---|
| Liters Per 100 Kilometers | [litersPer100Kilometers](unitfuelefficiency/litersper100kilometers.md) | L/100km |
| Miles Per Gallon | [milesPerGallon](unitfuelefficiency/milespergallon.md) | mpg |
| Miles Per Imperial Gallon | [milesPerImperialGallon](unitfuelefficiency/milesperimperialgallon.md) | mpg |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [milesPerImperialGallon](unitfuelefficiency/milesperimperialgallon.md) — The miles per imperial gallon unit of fuel efficiency.
- [litersPer100Kilometers](unitfuelefficiency/litersper100kilometers.md) — The liters per 100 kilometers unit of fuel efficiency.
- [milesPerGallon](unitfuelefficiency/milespergallon.md) — The miles per gallon unit of fuel efficiency.
