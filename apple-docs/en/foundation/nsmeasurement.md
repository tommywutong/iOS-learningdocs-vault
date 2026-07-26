---
title: NSMeasurement
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmeasurement
source_url: 'https://developer.apple.com/documentation/foundation/nsmeasurement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmeasurement.json'
content_hash: 'sha256:1e46bcb78b3d0de3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMeasurement

<sub>Class</sub>

A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMeasurement
```

## Overview

Use this object in Swift when you need reference semantics or other Foundation-specific behavior.

An [NSMeasurement](nsmeasurement.md) object represents a quantity and unit of measure. The [NSMeasurement](nsmeasurement.md) class provides a programmatic interface to converting measurements into different units, as well as calculating the sum or difference between two measurements.

[NSMeasurement](nsmeasurement.md) objects are initialized with an [Unit](unit.md) object and `double` value. [NSMeasurement](nsmeasurement.md) objects are immutable, and cannot be changed after being created.

You can use the [MeasurementFormatter](measurementformatter.md) class to create localized string representations of [NSMeasurement](nsmeasurement.md) objects.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [Measurement](measurement.md) structure, which bridges to the [NSMeasurement](nsmeasurement.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating Measurements

- [- initWithDoubleValue:unit:](<nsmeasurement/init(doublevalue_unit_).md>) — Initializes a new measurement with a specified double-precision floating-point value and unit.

### Accessing Unit and Value

- [unit](nsmeasurement/unit.md) — The unit of measure.
- [doubleValue](nsmeasurement/doublevalue.md) — The measurement value, represented as a double-precision floating-point number.

### Converting to Other Units

- [- canBeConvertedToUnit:](<nsmeasurement/canbeconverted(to_).md>) — Indicates whether the measurement can be converted to the given unit.
- [- measurementByConvertingToUnit:](<nsmeasurement/converting(to_).md>) — Returns a measurement created by converting the receiver to the specified unit.

### Operating on Measurements

- [- measurementByAddingMeasurement:](<nsmeasurement/adding(__).md>) — Returns a new measurement by adding the receiver to the specified measurement.
- [- measurementBySubtractingMeasurement:](<nsmeasurement/subtracting(__).md>) — Returns a new measurement by subtracting the specified measurement from the receiver.

### Initializers

- [init(coder:)](<nsmeasurement/init(coder_).md>)

## See Also

### Essentials

- [Measurement](measurement.md) — A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [Unit](unit.md) — An abstract class representing a unit of measure.
- [Dimension](dimension.md) — An abstract class representing a dimensional unit of measure.
