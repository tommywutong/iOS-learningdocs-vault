---
title: EnergyFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/energyformatter
source_url: 'https://developer.apple.com/documentation/foundation/energyformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/energyformatter.json'
content_hash: 'sha256:f64598541478aee3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# EnergyFormatter

<sub>Class</sub>

A formatter that provides localized descriptions of energy values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class EnergyFormatter
```

## Overview

> [!note] Note
> As of iOS 10, macOS 10.12, tvOS 10, and watchOS 3, Foundation provides the [MeasurementFormatter](measurementformatter.md) class, which can be used to represent quantities of [UnitEnergy](unitenergy.md) to provide equivalent functionality to [EnergyFormatter](energyformatter.md). You are encouraged to transition to these new Foundation Units and Measurements APIs whenever possible.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Formatting Energy Strings

- [forFoodEnergyUse](energyformatter/isforfoodenergyuse.md) — A Boolean value that indicates whether the energy value is used to measure food energy.
- [- getObjectValue:forString:errorDescription:](<energyformatter/getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSEnergyFormatter` class.
- [numberFormatter](energyformatter/numberformatter.md) — The number formatter used to format the numbers in energy strings.
- [- stringFromJoules:](<energyformatter/string(fromjoules_).md>) — Returns an energy string for the provided value.
- [- stringFromValue:unit:](<energyformatter/string(fromvalue_unit_).md>) — Returns a properly formatted energy string for the given value and unit.
- [- unitStringFromJoules:usedUnit:](<energyformatter/unitstring(fromjoules_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<energyformatter/unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](energyformatter/unitstyle.md) — The unit style used by this formatter.

### Constants

- [Unit](energyformatter/unit.md) — The units supported by the `NSEnergyFormatter` class.

## See Also

### Deprecated

- [LengthFormatter](lengthformatter.md) — A formatter that provides localized descriptions of linear distances, such as length and height measurements.
- [MassFormatter](massformatter.md) — A formatter that provides localized descriptions of mass and weight values.
