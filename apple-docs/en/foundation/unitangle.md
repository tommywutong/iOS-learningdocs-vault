---
title: UnitAngle
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitangle
source_url: 'https://developer.apple.com/documentation/foundation/unitangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitangle.json'
content_hash: 'sha256:f4056c09b3ffe949'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitAngle

<sub>Class</sub>

A unit of measure for planar angle and rotation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitAngle
```

## Overview

You typically use instances of [UnitAngle](unitangle.md) to represent specific quantities of planar angle using the [NSMeasurement](nsmeasurement.md) class.

### Angle

Angle is a quantity of rotation. The SI unit for angle is the radian (rad), which is dimensionless and defined to be the angle subtended by an arc that is equal in length to the radius of a circle. Angle is also commonly expressed in terms of degrees (°) and revolutions (rev).

The [UnitAngle](unitangle.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [degrees](unitangle/degrees.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Definition |
|---|---|---|---|
| Degrees | [degrees](unitangle/degrees.md) | ° | `1.0` |
| Arc Minutes | [arcMinutes](unitangle/arcminutes.md) | ʹ | `0.016667` |
| Arc Seconds | [arcSeconds](unitangle/arcseconds.md) | ʺ | `0.00027778` |
| Radians | [radians](unitangle/radians.md) | rad | `57.2958` |
| Gradians | [gradians](unitangle/gradians.md) | grad | `0.9` |
| Revolutions | [revolutions](unitangle/revolutions.md) | rev | `360` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [degrees](unitangle/degrees.md) — The degrees unit of angle.
- [arcMinutes](unitangle/arcminutes.md) — The arc minutes unit of angle.
- [arcSeconds](unitangle/arcseconds.md) — The arc seconds unit of angle.
- [radians](unitangle/radians.md) — The radians unit of angle.
- [gradians](unitangle/gradians.md) — The gradians unit of angle.
- [revolutions](unitangle/revolutions.md) — The revolutions unit of angle.

## See Also

### Physical Dimension

- [UnitArea](unitarea.md) — A unit of measure for area.
- [UnitLength](unitlength.md) — A unit of measure for length.
- [UnitVolume](unitvolume.md) — A unit of measure for volume.
