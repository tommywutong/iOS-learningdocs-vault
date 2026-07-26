---
title: Duration.UnitsFormatStyle
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle.json'
content_hash: 'sha256:5e603fe9d3b3b352'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Duration](../duration.md)

# Duration.UnitsFormatStyle

<sub>Structure</sub>

A format style that shows durations with localized labeled components

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UnitsFormatStyle
```

## Overview

This style produces formatted strings that break out a duration’s individual components, like “2 min, 3 sec”.

Create a `UnitsFormatStyle` by providing a set of allowed [Unit](unitsformatstyle/unit.md) instances — such as hours, minutes, or seconds — for formatted strings to include. You also specify a width for displaying these units, which controls whether they appear as full words (“minutes”) or abbreviations (“min”). The initializers also take optional parameters to control things like the handling of zero units and fractional parts. Then create a formatted string by calling [formatted(_:)](<formatted(__).md>) on a duration, passing the style, or [format(_:)](<unitsformatstyle/format(__).md>) on the style, passing a duration. You can also use the style’s [attributed](timeformatstyle/attributed-swift.property.md) property to create a style that produces [AttributedString](../../foundation/attributedstring.md) instances, which contains attributes that indicate the unit value of formatted runs of the string.

In situations that expect a [UnitsFormatStyle](unitsformatstyle.md), such as [formatted(_:)](<formatted(__).md>), you can use the convenience function `.units(allowed:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)` to create a [UnitsFormatStyle](unitsformatstyle.md), rather than using the full initializer.

If you want to reuse a style to format many durations, call [format(_:)](<unitsformatstyle/format(__).md>) on the style, passing in a new duration each time.

The following example creates `duration` to represent 1 hour, 10 minutes, 32 seconds, and 400 milliseconds. It then creates a [UnitsFormatStyle](unitsformatstyle.md) to show the hours, minutes, seconds, and milliseconds parts, with a wide width that presents the full name of each unit.

```swift
let duration = Duration.seconds(70 * 60 + 32) + Duration.milliseconds(400)
let format = duration1.formatted(
     .units(allowed: [.hours, .minutes, .seconds, .milliseconds],
            width: .wide))
// format == "1 hour, 10 minutes, 32 seconds, 400 milliseconds"
```

The formatted string omits any units that aren’t needed to accurately represent the value. In the above example, a duration of exactly one minute would format as `1 minute`, omitting the hours, seconds, and milliseconds parts. To override this behavior and show the omitted units, use the initializer’s’ `zeroValueUnits` parameter.

## Relationships

- **Conforms To**: [Copyable](../copyable.md), [Decodable](../decodable.md), [DiscreteFormatStyle](../../foundation/discreteformatstyle.md), [Encodable](../encodable.md), [Equatable](../equatable.md), [Escapable](../escapable.md), [FormatStyle](../../foundation/formatstyle.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Creating a units format style

- [init(allowedUnits:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)](<unitsformatstyle/init(allowedunits_width_maximumunitcount_zerovalueunits_valuelength_fractionalpart_).md>) — Creates a units format style using the given parameters.
- [init(allowedUnits:width:maximumUnitCount:zeroValueUnits:valueLengthLimits:fractionalPart:)](<unitsformatstyle/init(allowedunits_width_maximumunitcount_zerovalueunits_valuelengthlimits_fractionalpart_).md>) — Creates a units format style using the given parameters.

### Formatting a duration

- [format(_:)](<unitsformatstyle/format(__).md>) — Creates a locale-aware string representation from a duration value.

### Formatting a duration as an attributed string

- [attributed](unitsformatstyle/attributed-swift.property.md) — A property that formats the duration as an attributed string.
- [Attributed](unitsformatstyle/attributed-swift.struct.md) — A format style that formats durations as attributed strings.

### Working with units

- [allowedUnits](unitsformatstyle/allowedunits.md) — The units that may be included in the output string.
- [Unit](unitsformatstyle/unit.md) — A unit to use in formatting a duration.
- [maximumUnitCount](unitsformatstyle/maximumunitcount.md) — The maximum number of time units to include in the output string.
- [valueLengthLimits](unitsformatstyle/valuelengthlimits.md) — The padding or truncating behavior of the unit value.

### Working with unit widths

- [unitWidth](unitsformatstyle/unitwidth-swift.property.md) — The width of the unit and the spacing between the value and the unit.
- [UnitWidth](unitsformatstyle/unitwidth-swift.struct.md) — The width of a unit to use in formatting a duration.

### Working with zero values

- [zeroValueUnitsDisplay](unitsformatstyle/zerovalueunitsdisplay.md) — The strategy for how zero-value units are handled.
- [ZeroValueUnitsDisplayStrategy](unitsformatstyle/zerovalueunitsdisplaystrategy.md) — A strategy that determines how to format a unit whose value is zero.

### Working with fractional values

- [fractionalPartDisplay](unitsformatstyle/fractionalpartdisplay.md) — The strategy for displaying a duration if it cannot be represented exactly with the allowed units.
- [FractionalPartDisplayStrategy](unitsformatstyle/fractionalpartdisplaystrategy.md) — A strategy that determines how to format the fractional part of a duration if the allowed units can’t represent it exactly.

### Working with locales

- [locale](unitsformatstyle/locale.md) — The locale to use when formatting the duration.
- [locale(_:)](<unitsformatstyle/locale(__).md>) — A modifier to set the locale of the format style.

## See Also

### Formatting a duration

- [formatted()](<formatted().md>) — Formats the string using a localized hour-minute-second time pattern.
- [formatted(_:)](<formatted(__).md>) — Formats the duration, using the provided format style.
- [TimeFormatStyle](timeformatstyle.md) — A format style that shows durations in a compact, localized format with separators.
