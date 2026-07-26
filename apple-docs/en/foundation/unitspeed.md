---
title: UnitSpeed
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitspeed
source_url: 'https://developer.apple.com/documentation/foundation/unitspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitspeed.json'
content_hash: 'sha256:85f2bcfbb32542d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitSpeed

<sub>Class</sub>

A unit of measure for speed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitSpeed
```

## Overview

You typically use instances of [UnitSpeed](unitspeed.md) to represent specific quantities of speed using the [NSMeasurement](nsmeasurement.md) class.

### Speed

Speed is the magnitude of velocity, or the rate of change of position. Speed can be expressed by SI derived units in terms of meters per second (m/s), and is also commonly expressed in terms of kilometers per hour (km/h) and miles per hour (mph).

The [UnitSpeed](unitspeed.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [metersPerSecond](unitspeed/meterspersecond.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Meters Per Second | [metersPerSecond](unitspeed/meterspersecond.md) | m/s | `1.0` |
| Kilometers Per Hour | [kilometersPerHour](unitspeed/kilometersperhour.md) | km/h | `0.277778` |
| Miles Per Hour | [milesPerHour](unitspeed/milesperhour.md) | mph | `0.44704` |
| Knots | [knots](unitspeed/knots.md) | kn | `0.514444` |

The base unit is [metersPerSecond](unitspeed/meterspersecond.md) and is accessed via [+ baseUnit](<dimension/baseunit().md>) on the [Dimension](dimension.md) protocol.

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [metersPerSecond](unitspeed/meterspersecond.md) — The meter per second unit of speed.
- [kilometersPerHour](unitspeed/kilometersperhour.md) — The kilometers per hour unit of speed.
- [milesPerHour](unitspeed/milesperhour.md) — The miles per hour unit of speed.
- [knots](unitspeed/knots.md) — The knots unit of speed.

### Initializers

- [init(forLocale:usage:)](<unitspeed/init(forlocale_usage_).md>) — Creates a `UnitSpeed` which the specified `locale` prefers for the specific `usage`.

## See Also

### Time and Motion

- [UnitAcceleration](unitacceleration.md) — A unit of measure for acceleration.
- [UnitDuration](unitduration.md) — A unit of measure for a duration of time.
- [UnitFrequency](unitfrequency.md) — A unit of measure for frequency.
