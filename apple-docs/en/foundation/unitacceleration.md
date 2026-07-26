---
title: UnitAcceleration
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitacceleration
source_url: 'https://developer.apple.com/documentation/foundation/unitacceleration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitacceleration.json'
content_hash: 'sha256:56bc9963098f863b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitAcceleration

<sub>Class</sub>

A unit of measure for acceleration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitAcceleration
```

## Overview

You typically use instances of [UnitAcceleration](unitacceleration.md) to represent specific quantities of acceleration using the [NSMeasurement](nsmeasurement.md) class.

### Acceleration

Acceleration is the rate of change of velocity. Acceleration can be expressed by SI derived units in terms of meters per second squared (m/s2).

The [UnitAcceleration](unitacceleration.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [metersPerSecondSquared](unitacceleration/meterspersecondsquared.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Meters Per Second Squared | [metersPerSecondSquared](unitacceleration/meterspersecondsquared.md) | m/s² | `1.0` |
| Gravity | [gravity](unitacceleration/gravity.md) | g | `9.81` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [metersPerSecondSquared](unitacceleration/meterspersecondsquared.md) — Returns the meter per second squared unit of acceleration.
- [gravity](unitacceleration/gravity.md) — Returns the gravity unit of acceleration.

## See Also

### Time and Motion

- [UnitDuration](unitduration.md) — A unit of measure for a duration of time.
- [UnitFrequency](unitfrequency.md) — A unit of measure for frequency.
- [UnitSpeed](unitspeed.md) — A unit of measure for speed.
