---
title: UnitArea
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitarea
source_url: 'https://developer.apple.com/documentation/foundation/unitarea'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitarea.json'
content_hash: 'sha256:63872d753c695f72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitArea

<sub>Class</sub>

A unit of measure for area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitArea
```

## Overview

You typically use instances of [UnitArea](unitarea.md) to represent specific quantities of area using the [NSMeasurement](nsmeasurement.md) class.

### Area

Area is a quantity of extent in two dimensions. Area can be expressed by SI derived units in terms of square meters (m2). Area is also commonly measured in square feet (ft2) and acres (ac).

The [UnitArea](unitarea.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [squareMeters](unitarea/squaremeters.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Square Megameters | [squareMegameters](unitarea/squaremegameters.md) | Mm² | `1e12` |
| Square Kilometers | [squareKilometers](unitarea/squarekilometers.md) | km² | `1000000.0` |
| Square Meters | [squareMeters](unitarea/squaremeters.md) | m² | `1.0` |
| Square Centimeter | [squareCentimeters](unitarea/squarecentimeters.md) | cm² | `0.0001` |
| Square Millimeters | [squareMillimeters](unitarea/squaremillimeters.md) | mm² | `0.000001` |
| Square Micrometers | [squareMicrometers](unitarea/squaremicrometers.md) | µm² | `1e-12` |
| Square Nanometers | [squareNanometers](unitarea/squarenanometers.md) | nm² | `1e-18` |
| Square Inches | [squareInches](unitarea/squareinches.md) | in² | `0.00064516` |
| Square Feet | [squareFeet](unitarea/squarefeet.md) | ft² | `0.092903` |
| Square Yards | [squareYards](unitarea/squareyards.md) | yd² | `0.836127` |
| Square Miles | [squareMiles](unitarea/squaremiles.md) | mi² | `2.59e+6` |
| Acres | [acres](unitarea/acres.md) | ac | `4046.86` |
| Ares | [ares](unitarea/ares.md) | a | `100` |
| Hectares | [hectares](unitarea/hectares.md) | ha | `10000` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [squareMegameters](unitarea/squaremegameters.md) — The square megameters unit of area.
- [squareKilometers](unitarea/squarekilometers.md) — The square kilometers unit of area.
- [squareMeters](unitarea/squaremeters.md) — The square meters unit of area.
- [squareCentimeters](unitarea/squarecentimeters.md) — The square centimeters unit of area.
- [squareMillimeters](unitarea/squaremillimeters.md) — The square millimeters unit of area.
- [squareMicrometers](unitarea/squaremicrometers.md) — The square micrometers unit of area.
- [squareNanometers](unitarea/squarenanometers.md) — The square nanometers unit of area.
- [squareInches](unitarea/squareinches.md) — The square inches unit of area.
- [squareFeet](unitarea/squarefeet.md) — The square feet unit of area.
- [squareYards](unitarea/squareyards.md) — The square yards unit of area.
- [squareMiles](unitarea/squaremiles.md) — The square miles unit of area.
- [acres](unitarea/acres.md) — The acres unit of area.
- [ares](unitarea/ares.md) — The ares unit of area.
- [hectares](unitarea/hectares.md) — The hectares unit of area.

## See Also

### Physical Dimension

- [UnitLength](unitlength.md) — A unit of measure for length.
- [UnitVolume](unitvolume.md) — A unit of measure for volume.
- [UnitAngle](unitangle.md) — A unit of measure for planar angle and rotation.
