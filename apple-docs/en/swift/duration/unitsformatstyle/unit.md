---
title: Duration.UnitsFormatStyle.Unit
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle/unit
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/unit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/unit.json'
content_hash: 'sha256:31dc02ca1b1265b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [UnitsFormatStyle](../unitsformatstyle.md)

# Duration.UnitsFormatStyle.Unit

<sub>Structure</sub>

A unit to use in formatting a duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Unit
```

## Overview

Supported units range from hours to nanoseconds. Use these with the `allowed` parameter of the [UnitsFormatStyle](../unitsformatstyle.md) initializers to specify which units to use in a formatted string.

## Relationships

- **Conforms To**: [Decodable](../../decodable.md), [Encodable](../../encodable.md), [Equatable](../../equatable.md), [Hashable](../../hashable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Duration units

- [hours](unit/hours.md) — The hours unit, used for formatting a duration.
- [minutes](unit/minutes.md) — The minutes unit, used for formatting a duration.
- [seconds](unit/seconds.md) — The seconds unit, used for formatting a duration.
- [milliseconds](unit/milliseconds.md) — The milliseconds unit, used for formatting a duration.
- [microseconds](unit/microseconds.md) — The microseconds unit, used for formatting a duration.
- [nanoseconds](unit/nanoseconds.md) — The nanoseconds unit, used for formatting a duration.

### Type Properties

- [days](unit/days.md) — The unit for days. One day is always 86400 seconds.
- [weeks](unit/weeks.md) — The unit for weeks. One week is always 604800 seconds.

## See Also

### Working with units

- [allowedUnits](allowedunits.md) — The units that may be included in the output string.
- [maximumUnitCount](maximumunitcount.md) — The maximum number of time units to include in the output string.
- [valueLengthLimits](valuelengthlimits.md) — The padding or truncating behavior of the unit value.
