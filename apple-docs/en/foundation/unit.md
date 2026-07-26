---
title: Unit
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unit
source_url: 'https://developer.apple.com/documentation/foundation/unit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unit.json'
content_hash: 'sha256:db96669020bf6db9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Unit

<sub>Class</sub>

An abstract class representing a unit of measure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Unit
```

## Overview

Each instance of an [Unit](unit.md) subclass consists of a [symbol](unit/symbol.md), which can be used to create string representations of [NSMeasurement](nsmeasurement.md) objects with the [MeasurementFormatter](measurementformatter.md) class.

The [Dimension](dimension.md) subclass is an abstract class that represents a dimensional unit, which can be converted into different units of the same type. The Foundation framework provides several concrete [Dimension](dimension.md) subclasses to represent the most common physical quantities, including mass, length, duration, and speed.

### Subclassing Notes

[Unit](unit.md) is intended for subclassing. For dimensional units, you should use one of the Apple provided [Dimension](dimension.md) subclasses listed in Table 1 of [Dimension](dimension.md), or create a custom subclass of [Dimension](dimension.md). You can create a direct subclass of [Unit](unit.md) to represent a custom dimensionless unit, such as a count, score, or ratio.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [Dimension](dimension.md), [EnergyKit](unitenergy/energykit.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing Properties

- [symbol](unit/symbol.md) — The symbolic representation of the unit.

### Creating Units

- [- initWithSymbol:](<unit/init(symbol_).md>) — Initializes a new unit with the specified symbol.

### Initializers

- [init(coder:)](<unit/init(coder_).md>)

## See Also

### Essentials

- [Measurement](measurement.md) — A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [NSMeasurement](nsmeasurement.md) — A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [Dimension](dimension.md) — An abstract class representing a dimensional unit of measure.
