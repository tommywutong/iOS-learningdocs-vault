---
title: UnitFrequency
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitfrequency
source_url: 'https://developer.apple.com/documentation/foundation/unitfrequency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitfrequency.json'
content_hash: 'sha256:9044fff398a70076'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitFrequency

<sub>Class</sub>

A unit of measure for frequency.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitFrequency
```

## Overview

You typically use instances of [UnitFrequency](unitfrequency.md) to represent specific quantities of frequency using the [NSMeasurement](nsmeasurement.md) class.

### Frequency

Frequency is a quantity of occurrences for a repeating event over time. The SI unit for frequency is the hertz (Hz), which is a derived as one occurrence per second (`1 Hz = 1 / 1s`).

The [UnitFrequency](unitfrequency.md) class defines its [+ baseUnit](<dimension/baseunit().md>) as [hertz](unitfrequency/hertz.md), and provides the following units, which are initialized using [UnitConverterLinear](unitconverterlinear.md) converters with the specified coefficients:

| Name | Method | Symbol | Coefficient |
|---|---|---|---|
| Terahertz | [terahertz](unitfrequency/terahertz.md) | THz | `1e12` |
| Gigahertz | [gigahertz](unitfrequency/gigahertz.md) | GHz | `1e9` |
| Megahertz | [megahertz](unitfrequency/megahertz.md) | MHz | `1000000.0` |
| Kilohertz | [kilohertz](unitfrequency/kilohertz.md) | kHz | `1000.0` |
| Hertz | [hertz](unitfrequency/hertz.md) | Hz | `1` |
| Millihertz | [millihertz](unitfrequency/millihertz.md) | mHz | `0.001` |
| Microhertz | [microhertz](unitfrequency/microhertz.md) | µHz | `0.000001` |
| Nanohertz | [nanohertz](unitfrequency/nanohertz.md) | nHz | `1e-9` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the Base Unit

- [+ baseUnit](<dimension/baseunit().md>) — Returns the base unit.

### Accessing Predefined Units

- [terahertz](unitfrequency/terahertz.md) — The terahertz unit of frequency.
- [gigahertz](unitfrequency/gigahertz.md) — The gigahertz unit of frequency.
- [megahertz](unitfrequency/megahertz.md) — The megahertz unit of frequency.
- [kilohertz](unitfrequency/kilohertz.md) — The kilohertz unit of frequency.
- [hertz](unitfrequency/hertz.md) — The hertz unit of frequency.
- [millihertz](unitfrequency/millihertz.md) — The millihertz unit of frequency.
- [microhertz](unitfrequency/microhertz.md) — The microhertz unit of frequency.
- [nanohertz](unitfrequency/nanohertz.md) — The nanohertz unit of frequency.
- [framesPerSecond](unitfrequency/framespersecond.md) — The frames per second unit of frequency.

## See Also

### Time and Motion

- [UnitAcceleration](unitacceleration.md) — A unit of measure for acceleration.
- [UnitDuration](unitduration.md) — A unit of measure for a duration of time.
- [UnitSpeed](unitspeed.md) — A unit of measure for speed.
