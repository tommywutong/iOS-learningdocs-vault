---
title: Measurement
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement
source_url: 'https://developer.apple.com/documentation/foundation/measurement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement.json'
content_hash: 'sha256:95dfdb5033b6ce4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Measurement

<sub>Structure</sub>

A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Measurement<UnitType> where UnitType : Unit
```

## Overview

A [Measurement](measurement.md) object represents a quantity and unit of measure. The [Measurement](measurement.md) type provides a programmatic interface to converting measurements into different units, as well as calculating the sum or difference between two measurements.

[Measurement](measurement.md) objects are initialized with a [Unit](unit.md) object and double value. [Measurement](measurement.md) objects are immutable, and cannot be changed after being created.

Measurements support a large set of operators, including `+`, `-`, `*`, `/`, and a full set of comparison operators.

## Relationships

- **Conforms To**: [Comparable](../swift/comparable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [ElectricityInsightMeasure](../energykit/electricityinsightmeasure.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [IntentValueConvertible](../appintents/intentvalueconvertible.md), [IntentValueExpressing](../appintents/intentvalueexpressing.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Measurement

- [init(value:unit:)](<measurement/init(value_unit_).md>) — Create a `Measurement` given a specified value and unit.

### Accessing the Value and Units

- [unit](measurement/unit.md) — The unit component of the measurement.
- [value](measurement/value.md) — The value component of the measurement.

### Converting to Other Units

- [convert(to:)](<measurement/convert(to_).md>) — Converts the measurement to the specified unit.
- [converted(to:)](<measurement/converted(to_).md>) — Returns a new measurement created by converting to the specified unit.

### Operating on a Measurement

- [*(_:_:)](<measurement/_(____)-1d26c.md>) — Multiply a scalar value by a measurement.
- [*(_:_:)](<measurement/_(____)-5tv8a.md>) — Multiply a measurement by a scalar value.
- [+(_:_:)](<measurement/+(____)-9lejn.md>) — Add two measurements.
- [+(_:_:)](<measurement/+(____)-4fsbl.md>) — Adds two measurements of the same dimension.
- [-(_:_:)](<measurement/-(____)-2nnoy.md>) — Subtract two measurements of the same Unit.
- [-(_:_:)](<measurement/-(____)-1a47h.md>) — Subtract two measurements of the same Dimension.
- [/(_:_:)](<measurement/_(____)-98s40.md>) — Divide a scalar value by a measurement.
- [/(_:_:)](<measurement/_(____)-71kwk.md>) — Divide a measurement by a scalar value.

### Formatting a Measurement

- [formatted()](<measurement/formatted().md>) — Generates a locale-aware string representation of a measurement using the default measurement format style.
- [formatted(_:)](<measurement/formatted(__).md>) — Generates a locale-aware string representation of a measurement using the provided measurement format style.
- [FormatStyle](measurement/formatstyle.md) — A type that provides localized representations of measurements.
- [AttributedStyle](measurement/attributedstyle.md) — A type that provides localized representations of measurements with an attributed string.

### Comparing Measurements

- [\<(_:_:)](<measurement/_(____)-7pou4.md>) — Compare two measurements of the same `Unit`.

### Using Reference Types

- [NSMeasurement](nsmeasurement.md) — A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.

### Type Aliases

- [Specification](measurement/specification.md)
- [UnwrappedType](measurement/unwrappedtype.md)
- [ValueType](measurement/valuetype.md)

### Type Properties

- [defaultResolverSpecification](measurement/defaultresolverspecification.md)

### Default Implementations

- [Comparable Implementations](measurement/comparable-implementations.md)
- [Equatable Implementations](measurement/equatable-implementations.md)

## See Also

### Essentials

- [NSMeasurement](nsmeasurement.md) — A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [Unit](unit.md) — An abstract class representing a unit of measure.
- [Dimension](dimension.md) — An abstract class representing a dimensional unit of measure.
