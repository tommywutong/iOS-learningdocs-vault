---
title: MassFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/massformatter
source_url: 'https://developer.apple.com/documentation/foundation/massformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/massformatter.json'
content_hash: 'sha256:829794a00066d79e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# MassFormatter

<sub>Class</sub>

A formatter that provides localized descriptions of mass and weight values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MassFormatter
```

## Overview

> [!note] Note
> As of iOS 10, macOS 10.12, tvOS 10, and watchOS 3, Foundation provides the [MeasurementFormatter](measurementformatter.md) class, which can be used to represent quantities of [UnitMass](unitmass.md) to provide equivalent functionality to [MassFormatter](massformatter.md). You are encouraged to transition to these new Foundation Units and Measurements APIs whenever possible.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Formatting Mass Strings

- [forPersonMassUse](massformatter/isforpersonmassuse.md) — A Boolean value that indicates whether the resulting string represents a person’s mass.
- [- getObjectValue:forString:errorDescription:](<massformatter/getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSMassFormatter` class.
- [numberFormatter](massformatter/numberformatter.md) — The number formatter used to format the numbers in a mass strings.
- [- stringFromKilograms:](<massformatter/string(fromkilograms_).md>) — Returns a mass string for the provided value.
- [- stringFromValue:unit:](<massformatter/string(fromvalue_unit_).md>) — Returns a properly formatted mass string for the given value and unit.
- [- unitStringFromKilograms:usedUnit:](<massformatter/unitstring(fromkilograms_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<massformatter/unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](massformatter/unitstyle.md) — The unit style used by this formatter.

### Constants

- [Unit](massformatter/unit.md) — The units supported by the `NSMassFormatter` class.

## See Also

### Deprecated

- [LengthFormatter](lengthformatter.md) — A formatter that provides localized descriptions of linear distances, such as length and height measurements.
- [EnergyFormatter](energyformatter.md) — A formatter that provides localized descriptions of energy values.
