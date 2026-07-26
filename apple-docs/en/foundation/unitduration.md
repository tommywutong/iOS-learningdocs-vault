---
title: UnitDuration
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitduration
source_url: 'https://developer.apple.com/documentation/foundation/unitduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitduration.json'
content_hash: 'sha256:97ebb91b62532089'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitDuration

<sub>Class</sub>

A unit of measure for a duration of time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitDuration
```

## Overview

You typically use instances of [UnitDuration](unitduration.md) to represent specific quantities of planar angle using the [NSMeasurement](nsmeasurement.md) class.

### Duration

Duration is a quantity of time. The SI unit for time is the second (sec), which is defined in terms of the radioactivity of a cesium-133 atom. Duration is also commonly expressed in terms of minutes (min) and hours (hr).

> [!note] Note
> Use the [NSDateComponents](nsdatecomponents.md) class to represent quantities of calendrical units, such as days, weeks, months, and years.

The [UnitDuration](unitduration.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [seconds](unitduration/seconds.md), and provides the following units, which [UnitConverterLinear](unitconverterlinear.md) converters initialize with the given coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Seconds | [seconds](unitduration/seconds.md) | sec | `1` |
| Minutes | [minutes](unitduration/minutes.md) | min | `60` |
| Hours | [hours](unitduration/hours.md) | hr | `3600` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [hours](unitduration/hours.md) — The hour unit of duration.
- [minutes](unitduration/minutes.md) — The minute unit of duration.
- [seconds](unitduration/seconds.md) — The second unit of duration.
- [milliseconds](unitduration/milliseconds.md) — The millisecond unit of duration.
- [microseconds](unitduration/microseconds.md) — The microsecond unit of duration.
- [nanoseconds](unitduration/nanoseconds.md) — The nanosecond unit of duration.
- [picoseconds](unitduration/picoseconds.md) — The picosecond unit of duration.

## See Also

### Time and Motion

- [UnitAcceleration](unitacceleration.md) — A unit of measure for acceleration.
- [UnitFrequency](unitfrequency.md) — A unit of measure for frequency.
- [UnitSpeed](unitspeed.md) — A unit of measure for speed.
