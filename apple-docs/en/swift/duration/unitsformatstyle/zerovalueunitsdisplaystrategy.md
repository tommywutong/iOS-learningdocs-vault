---
title: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle/zerovalueunitsdisplaystrategy
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/zerovalueunitsdisplaystrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/zerovalueunitsdisplaystrategy.json'
content_hash: 'sha256:72b4ffeb3e5b1422'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [UnitsFormatStyle](../unitsformatstyle.md)

# Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy

<sub>Structure</sub>

A strategy that determines how to format a unit whose value is zero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ZeroValueUnitsDisplayStrategy
```

## Overview

When using a [UnitsFormatStyle](../unitsformatstyle.md), specifying a `ZeroValueUnitsDisplayStrategy` enables you to decide whether show a unit whose value is zero.

The following example creates a duration of 25 seconds, then formats it with two different styles. The first style uses the [hide](zerovalueunitsdisplaystrategy/hide.md) display strategy, which omits the hours and minutes, since their value is `0`. The second uses [show(length:)](<zerovalueunitsdisplaystrategy/show(length_).md>) to create two-digit representations of the hour and minute fields.

```swift
let duration = Duration.seconds(25)
let hide = duration.formatted(
    .units(allowed: [.hours, .minutes, .seconds],
           width: .abbreviated,
           zeroValueUnits:.hide)) // 25 sec
let showTwo = duration.formatted(
    .units(allowed: [.hours, .minutes, .seconds],
           width: .abbreviated,
           zeroValueUnits:.show(length: 2))) // 00 hr, 00 min, 25 sec
```

## Relationships

- **Conforms To**: [Decodable](../../decodable.md), [Encodable](../../encodable.md), [Equatable](../../equatable.md), [Hashable](../../hashable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Using common strategies

- [hide](zerovalueunitsdisplaystrategy/hide.md) — A display strategy that hides leading fields whose value is zero.
- [show(length:)](<zerovalueunitsdisplaystrategy/show(length_).md>) — Returns display strategy that shows leading fields whose value is zero, with a given number of digits.

## See Also

### Working with zero values

- [zeroValueUnitsDisplay](zerovalueunitsdisplay.md) — The strategy for how zero-value units are handled.
