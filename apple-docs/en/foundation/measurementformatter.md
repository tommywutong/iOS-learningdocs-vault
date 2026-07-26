---
title: MeasurementFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurementformatter
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatter.json'
content_hash: 'sha256:f214e525c725b69f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# MeasurementFormatter

<sub>Class</sub>

A formatter that provides localized representations of units and measurements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MeasurementFormatter
```

## Overview

You use the [- stringFromMeasurement:](<measurementformatter/string(from_)-wt9y.md>) method to create a localized representation of an [NSMeasurement](nsmeasurement.md) object, and you use the [- stringFromUnit:](<measurementformatter/string(from_)-4hwjz.md>) method to create a localized representation of an [Unit](unit.md) object. The formatter takes into account the specified [locale](measurementformatter/locale.md), [unitStyle](measurementformatter/unitstyle.md), and [unitOptions](measurementformatter/unitoptions-swift.property.md) when producing string representations of units and measurements.

> [!tip] Tip
> In Swift, you can use [FormatStyle](measurement/formatstyle.md) rather than [MeasurementFormatter](measurementformatter.md). The [FormatStyle](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [FormatStyle](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Specifying the Format

- [unitOptions](measurementformatter/unitoptions-swift.property.md) — The options for how the unit is formatted.
- [UnitOptions](measurementformatter/unitoptions-swift.struct.md) — Measurement formatter options.
- [unitStyle](measurementformatter/unitstyle.md) — The unit style.
- [locale](measurementformatter/locale.md) — The locale of the formatter.
- [numberFormatter](measurementformatter/numberformatter.md) — The number formatter used to format the quantity of a measurement.

### Converting Measurements

- [- stringFromMeasurement:](<measurementformatter/string(from_)-wt9y.md>) — Creates and returns a localized string representation of the provided measurement.
- [string(from:)](<measurementformatter/string(from_)-6rcb1.md>) — Creates and returns a localized string representation of the provided measurement.
- [- stringFromUnit:](<measurementformatter/string(from_)-4hwjz.md>) — Creates and returns a localized string representation of the provided unit of measure.
