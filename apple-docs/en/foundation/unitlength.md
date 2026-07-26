---
title: UnitLength
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitlength
source_url: 'https://developer.apple.com/documentation/foundation/unitlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitlength.json'
content_hash: 'sha256:37492573f4a523d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitLength

<sub>Class</sub>

A unit of measure for length.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitLength
```

## Overview

You typically use instances of [UnitLength](unitlength.md) to represent specific quantities of length using the [NSMeasurement](nsmeasurement.md) class.

### Length

Length is the dimensional extent of matter. The SI unit for length is the meter (m), which is defined in terms of the distance traveled by light in a vacuum.

The [UnitLength](unitlength.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [meters](unitlength/meters.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Megameters | [megameters](unitlength/megameters.md) | Mm | `1000000.0` |
| Kilometers | [kilometers](unitlength/kilometers.md) | kM | `1000.0` |
| Hectometers | [hectometers](unitlength/hectometers.md) | hm | `100.0` |
| Decameters | [decameters](unitlength/decameters.md) | dam | `10.0` |
| Meters | [meters](unitlength/meters.md) | m | `1.0` |
| Decimeters | [decimeters](unitlength/decimeters.md) | dm | `0.1` |
| Centimeters | [centimeters](unitlength/centimeters.md) | cm | `0.01` |
| Millimeters | [millimeters](unitlength/millimeters.md) | mm | `0.001` |
| Micrometers | [micrometers](unitlength/micrometers.md) | µm | `0.000001` |
| Nanometers | [nanometers](unitlength/nanometers.md) | nm | `1e-9` |
| Picometers | [picometers](unitlength/picometers.md) | pm | `1e-12` |
| Inches | [inches](unitlength/inches.md) | in | `0.0254` |
| Feet | [feet](unitlength/feet.md) | ft | `0.3048` |
| Yards | [yards](unitlength/yards.md) | yd | `0.9144` |
| Miles | [miles](unitlength/miles.md) | mi | `1609.34` |
| Scandinavian Miles | [scandinavianMiles](unitlength/scandinavianmiles.md) | smi | `10000` |
| Light Years | [lightyears](unitlength/lightyears.md) | ly | `9.461e+15` |
| Nautical Miles | [nauticalMiles](unitlength/nauticalmiles.md) | NM | `1852` |
| Fathoms | [fathoms](unitlength/fathoms.md) | ftm | `1.8288` |
| Furlongs | [furlongs](unitlength/furlongs.md) | fur | `201.168` |
| Astronomical Units | [astronomicalUnits](unitlength/astronomicalunits.md) | au | `1.496e+11` |
| Parsecs | [parsecs](unitlength/parsecs.md) | pc | `3.086e+16` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [megameters](unitlength/megameters.md) — The megameters unit of length.
- [kilometers](unitlength/kilometers.md) — The kilometers unit of length.
- [hectometers](unitlength/hectometers.md) — The hectometers unit of length.
- [decameters](unitlength/decameters.md) — The decameters unit of length.
- [meters](unitlength/meters.md) — The meters unit of length.
- [decimeters](unitlength/decimeters.md) — The decimeters unit of length.
- [centimeters](unitlength/centimeters.md) — The centimeters unit of length.
- [millimeters](unitlength/millimeters.md) — The millimeters unit of length.
- [micrometers](unitlength/micrometers.md) — The micrometers unit of length.
- [nanometers](unitlength/nanometers.md) — The nanometers unit of length.
- [picometers](unitlength/picometers.md) — The picometers unit of length.
- [inches](unitlength/inches.md) — The inches unit of length.
- [feet](unitlength/feet.md) — The feet unit of length.
- [yards](unitlength/yards.md) — The yards unit of length.
- [miles](unitlength/miles.md) — The miles unit of length.
- [scandinavianMiles](unitlength/scandinavianmiles.md) — The Scandinavian miles unit of length.
- [lightyears](unitlength/lightyears.md) — The light years unit of length.
- [nauticalMiles](unitlength/nauticalmiles.md) — The nautical miles unit of length.
- [fathoms](unitlength/fathoms.md) — The fathoms unit of length.
- [furlongs](unitlength/furlongs.md) — The furlongs unit of length.
- [astronomicalUnits](unitlength/astronomicalunits.md) — The astronomical units unit of length.
- [parsecs](unitlength/parsecs.md) — The parsecs unit of length.

### Initializers

- [init(forLocale:usage:)](<unitlength/init(forlocale_usage_).md>) — Creates a `UnitLength` which the specified `locale` prefers for the specific `usage`.

## See Also

### Physical Dimension

- [UnitArea](unitarea.md) — A unit of measure for area.
- [UnitVolume](unitvolume.md) — A unit of measure for volume.
- [UnitAngle](unitangle.md) — A unit of measure for planar angle and rotation.
