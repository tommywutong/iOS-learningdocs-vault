---
title: 'init(allowedUnits:width:maximumUnitCount:zeroValueUnits:valueLengthLimits:fractionalPart:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/unitsformatstyle/init(allowedunits:width:maximumunitcount:zerovalueunits:valuelengthlimits:fractionalpart:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/init(allowedunits:width:maximumunitcount:zerovalueunits:valuelengthlimits:fractionalpart:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/init%28allowedunits%3Awidth%3Amaximumunitcount%3Azerovalueunits%3Avaluelengthlimits%3Afractionalpart%3A%29.json'
content_hash: 'sha256:ec1ae1a1fa9f234d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [UnitsFormatStyle](../unitsformatstyle.md)

# init(allowedUnits:width:maximumUnitCount:zeroValueUnits:valueLengthLimits:fractionalPart:)

<sub>Initializer</sub>

Creates a units format style using the given parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<ValueRange>(allowedUnits: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int? = nil, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy = .hide, valueLengthLimits: ValueRange, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy = .hide) where ValueRange : RangeExpression, ValueRange.Bound == Int
```

## Parameters

- `allowedUnits` — The units that the formatted string may include.

- `width` — The width of the unit and the spacing between the value and the unit.

- `maximumUnitCount` — The maximum number of duration units to include in the output string.

- `zeroValueUnits` — The strategy for handling leading units with zero values.

- `valueLengthLimits` — The padding or truncating behavior of the unit value, as a bounded range of `Int` values.

- `fractionalPart` — The strategy for displaying a duration if a formatted string can’t represent it exactly with the allowed units.

## Discussion

Use this convenience function in situations that expect a [UnitsFormatStyle](../unitsformatstyle.md), such as [formatted(_:)](<../formatted(__).md>), as an alternative to using the full initializer.

## See Also

### Creating a units format style

- [init(allowedUnits:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)](<init(allowedunits_width_maximumunitcount_zerovalueunits_valuelength_fractionalpart_).md>) — Creates a units format style using the given parameters.
