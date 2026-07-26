---
title: UnitMass
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitmass
source_url: 'https://developer.apple.com/documentation/foundation/unitmass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitmass.json'
content_hash: 'sha256:bd86e2abae20a592'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitMass

<sub>Class</sub>

A unit of measure for mass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitMass
```

## Overview

You typically use instances of [UnitMass](unitmass.md) to represent specific quantities of mass using the [NSMeasurement](nsmeasurement.md) class.

### Mass

Mass is a fundamental property of matter that causes it to resist a force accelerating it. The SI unit for mass is the kilogram (kg), which defined in terms of the mass of the international prototype kilogram.

The [UnitMass](unitmass.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [kilograms](unitmass/kilograms.md), and provides the following units, which [UnitConverterLinear](unitconverterlinear.md) converters initialize with the given coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Kilograms | [kilograms](unitmass/kilograms.md) | kg | `1.0` |
| Grams | [grams](unitmass/grams.md) | g | `0.001` |
| Decigrams | [decigrams](unitmass/decigrams.md) | dg | `0.0001` |
| Centigrams | [centigrams](unitmass/centigrams.md) | cg | `0.00001` |
| Milligrams | [milligrams](unitmass/milligrams.md) | mg | `0.000001` |
| Micrograms | [micrograms](unitmass/micrograms.md) | µg | `1e-9` |
| Nanograms | [nanograms](unitmass/nanograms.md) | ng | `1e-12` |
| Picograms | [picograms](unitmass/picograms.md) | pg | `1e-15` |
| Ounces | [ounces](unitmass/ounces.md) | oz | `0.0283495` |
| Pounds | [poundsMass](unitmass/pounds.md) | lb | `0.453592` |
| Stones | [stones](unitmass/stones.md) | st | `0.157473` |
| Metric Tons | [metricTons](unitmass/metrictons.md) | t | `1000` |
| Short Tons | [shortTons](unitmass/shorttons.md) | ton | `907.185` |
| Carats | [carats](unitmass/carats.md) | ct | `0.0002` |
| Ounces Troy | [ouncesTroy](unitmass/ouncestroy.md) | oz t | `0.03110348` |
| Slugs | [slugs](unitmass/slugs.md) | slug | `14.5939` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [kilograms](unitmass/kilograms.md) — The kilograms unit of mass.
- [grams](unitmass/grams.md) — The grams unit of mass.
- [decigrams](unitmass/decigrams.md) — The decigrams unit of mass.
- [centigrams](unitmass/centigrams.md) — The centigrams unit of mass.
- [milligrams](unitmass/milligrams.md) — The milligrams unit of mass.
- [micrograms](unitmass/micrograms.md) — The micrograms unit of mass.
- [nanograms](unitmass/nanograms.md) — The nanograms unit of mass.
- [picograms](unitmass/picograms.md) — The picograms unit of mass.
- [ounces](unitmass/ounces.md) — The ounces unit of mass.
- [pounds](1808594-pounds.md) — Returns the pounds unit of mass.
- [poundsMass](unitmass/pounds.md) — The pounds unit of mass.
- [stones](unitmass/stones.md) — The stone unit of mass.
- [metricTons](unitmass/metrictons.md) — The metric tons unit of mass.
- [shortTons](unitmass/shorttons.md) — The short tons unit of mass.
- [carats](unitmass/carats.md) — The carats unit of mass.
- [ouncesTroy](unitmass/ouncestroy.md) — The ounces troy unit of mass.
- [slugs](unitmass/slugs.md) — The slugs unit of mass.

### Initializers

- [init(forLocale:usage:)](<unitmass/init(forlocale_usage_).md>) — Creates a `UnitMass` which the specified `locale` prefers for the specific `usage`.

## See Also

### Mass, Weight, and Force

- [UnitPressure](unitpressure.md) — A unit of measure for pressure.
