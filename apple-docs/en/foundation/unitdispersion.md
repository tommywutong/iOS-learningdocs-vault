---
title: UnitDispersion
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitdispersion
source_url: 'https://developer.apple.com/documentation/foundation/unitdispersion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitdispersion.json'
content_hash: 'sha256:62ab89ce7f8ea0c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitDispersion

<sub>Class</sub>

A unit of measure for specific quantities of dispersion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitDispersion
```

## Overview

You typically use instances of [UnitDispersion](unitdispersion.md) to represent specific quantities of dispersion using the [NSMeasurement](nsmeasurement.md) class.

### Dispersion

Dispersion describes the amount of a constituent divided by the amount of all other constituents in a mixture. Dispersion is a dimensionless quantity that is commonly expressed in “parts-per” notation, such as “parts per million” (ppm), to describe small relative quantities.

The [UnitDispersion](unitdispersion.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [partsPerMillion](unitdispersion/partspermillion.md).

| Name | Method | Abbreviation |
|---|---|---|
| Parts Per Million | [partsPerMillion](unitdispersion/partspermillion.md) | ppm |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [partsPerMillion](unitdispersion/partspermillion.md) — The parts per million unit.

## See Also

### Concentration and Dispersion

- [UnitConcentrationMass](unitconcentrationmass.md) — A unit of measure for concentration of mass.
