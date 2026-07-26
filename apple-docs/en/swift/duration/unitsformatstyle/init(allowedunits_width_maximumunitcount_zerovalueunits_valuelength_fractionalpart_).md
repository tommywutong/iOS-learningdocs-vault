---
title: 'init(allowedUnits:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/duration/unitsformatstyle/init(allowedunits:width:maximumunitcount:zerovalueunits:valuelength:fractionalpart:)'
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/init(allowedunits:width:maximumunitcount:zerovalueunits:valuelength:fractionalpart:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/init%28allowedunits%3Awidth%3Amaximumunitcount%3Azerovalueunits%3Avaluelength%3Afractionalpart%3A%29.json'
content_hash: 'sha256:f240536fe1ac8e5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [UnitsFormatStyle](../unitsformatstyle.md)

# init(allowedUnits:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)

<sub>Initializer</sub>

Creates a units format style using the given parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(allowedUnits: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int? = nil, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy = .hide, valueLength: Int? = nil, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy = .hide)
```

## Parameters

- `allowedUnits` — The units that the formatted string may include.

- `width` — The width of the unit and the spacing between the value and the unit.

- `maximumUnitCount` — The maximum number of duration units to include in the output string.

- `zeroValueUnits` — The strategy for handling leading units with zero values.

- `valueLength` — The padding or truncating behavior of the unit value, as an `Int`.

- `fractionalPart` — The strategy for displaying a duration if a formatted string can’t represent it exactly with the allowed units.

## Discussion

Use this convenience function in situations that expect a [UnitsFormatStyle](../unitsformatstyle.md), such as [formatted(_:)](<../formatted(__).md>), as an alternative to using the full initializer.

## See Also

### Creating a units format style

- [init(allowedUnits:width:maximumUnitCount:zeroValueUnits:valueLengthLimits:fractionalPart:)](<init(allowedunits_width_maximumunitcount_zerovalueunits_valuelengthlimits_fractionalpart_).md>) — Creates a units format style using the given parameters.
