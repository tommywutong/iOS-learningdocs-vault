---
title: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy.json'
content_hash: 'sha256:872aafb91fb6031a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [UnitsFormatStyle](../unitsformatstyle.md)

# Duration.UnitsFormatStyle.FractionalPartDisplayStrategy

<sub>Structure</sub>

A strategy that determines how to format the fractional part of a duration if the allowed units can’t represent it exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FractionalPartDisplayStrategy
```

## Overview

When using a [UnitsFormatStyle](../unitsformatstyle.md), specifying a `FractionalPartDisplayStrategy` enables you to decide how to balance between accuracy and verbosity when you’re not using all of the available units (hours, minutes, and seconds). When a formatted duration has a fractional part, you can hide it entirely, round the unit up or down while hiding the fractional part, or show the unit with a fraction.

The following example shows different display strategies used with a duration of 1 hour, 15 minutes and unit format styles that only show hours.

```swift
let duration = Duration.seconds(75 * 60) // 1 minute, 15 seconds
let hide = duration.formatted(
    .units(allowed: [.hours],
           width: .wide,
           fractionalPart: .hide)) // 1 hour
let hideRounded = duration.formatted(
    .units(allowed: [.hours],
           width: .wide,
           fractionalPart: .hide(rounded:.up))) // 2 hours
let show = duration.formatted(
    .units(allowed: [.hours],
           width: .wide,
           fractionalPart: .show(length: 2))) // 1.25 hours
```

## Relationships

- **Conforms To**: [Decodable](../../decodable.md), [Encodable](../../encodable.md), [Equatable](../../equatable.md), [Hashable](../../hashable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Creating a fractional part display strategy

- [init(lengthLimits:roundingRule:roundingIncrement:)](<fractionalpartdisplaystrategy/init(lengthlimits_roundingrule_roundingincrement_).md>) — Creates a fractional part display strategy that uses the provided behaviors.

### Using common strategies

- [hide](fractionalpartdisplaystrategy/hide.md) — A display strategy that hides any fractional part by truncating it.
- [hide(rounded:)](<fractionalpartdisplaystrategy/hide(rounded_).md>) — Creates a display strategy that hides any fractional part rounding the unit value.
- [show(length:rounded:increment:)](<fractionalpartdisplaystrategy/show(length_rounded_increment_).md>) — Creates a display strategy that shows a fractional part.

### Working with strategy properties

- [minimumLength](fractionalpartdisplaystrategy/minimumlength.md) — The minimum length of the fractional part, if shown.
- [maximumLength](fractionalpartdisplaystrategy/maximumlength.md) — The maximum length of the fractional part, if shown.
- [roundingIncrement](fractionalpartdisplaystrategy/roundingincrement.md) — A multiple by which a formatter rounds a fractional part of a duration.
- [roundingRule](fractionalpartdisplaystrategy/roundingrule.md) — The rule for rounding a unit up or down if it has a fractional part.

## See Also

### Working with fractional values

- [fractionalPartDisplay](fractionalpartdisplay.md) — The strategy for displaying a duration if it cannot be represented exactly with the allowed units.
