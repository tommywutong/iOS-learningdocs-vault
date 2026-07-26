---
title: LengthFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/lengthformatter
source_url: 'https://developer.apple.com/documentation/foundation/lengthformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/lengthformatter.json'
content_hash: 'sha256:88e02384df3c4f24'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# LengthFormatter

<sub>Class</sub>

A formatter that provides localized descriptions of linear distances, such as length and height measurements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class LengthFormatter
```

## Overview

> [!note] Note
> As of iOS 10, macOS 10.12, tvOS 10, and watchOS 3, Foundation provides the [MeasurementFormatter](measurementformatter.md) class, which can be used to represent quantities of [UnitLength](unitlength.md) to provide equivalent functionality to [LengthFormatter](lengthformatter.md). You are encouraged to transition to these new Foundation Units and Measurements APIs whenever possible.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Formatting Length Strings

- [forPersonHeightUse](lengthformatter/isforpersonheightuse.md) — A Boolean value that indicates whether the resulting string represents a person’s height.
- [- getObjectValue:forString:errorDescription:](<lengthformatter/getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSLengthFormatter` class.
- [numberFormatter](lengthformatter/numberformatter.md) — The number formatter used to format the numbers in length strings.
- [- stringFromMeters:](<lengthformatter/string(frommeters_).md>) — Returns a length string for the provided value.
- [- stringFromValue:unit:](<lengthformatter/string(fromvalue_unit_).md>) — Returns a properly formatted length string for the given value and unit.
- [- unitStringFromMeters:usedUnit:](<lengthformatter/unitstring(frommeters_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<lengthformatter/unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](lengthformatter/unitstyle.md) — The unit style used by this formatter.

### Constants

- [Unit](lengthformatter/unit.md) — The units supported by the `NSLengthFormatter` class.

## See Also

### Deprecated

- [MassFormatter](massformatter.md) — A formatter that provides localized descriptions of mass and weight values.
- [EnergyFormatter](energyformatter.md) — A formatter that provides localized descriptions of energy values.
