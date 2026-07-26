---
title: 'formatted(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatted%28_%3A%29.json'
content_hash: 'sha256:d6fa75b97caa9205'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# formatted(_:)

<sub>Instance Method</sub>

Generates a locale-aware string representation of a measurement using the provided measurement format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ style: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Measurement<UnitType>
```

## Parameters

- `style` — The measurement format style to apply to the measurement.

## Return Value

A string, formatted according to the provided style.

## Discussion

Use the [formatted(_:)](<formatted(__).md>) method to create a string representation of a measurement using a custom measurement format style. You can specify the width of the unit name, the numeric formatting of the value, and the intended usage type of the measurement. You can use the [FormatStyle](formatstyle.md) static factory method `measurement(width:usage:numberFormat:)` to create a custom format style as a parameter to the method, such as in the following example:

```swift
let temp = Measurement<UnitTemperature>(value: 38, unit: .celsius)
let formattedTemp = temp.formatted(.measurement(width: .wide, usage: .weather, numberFormat: .numeric(precision: .fractionLength(1))))
// For locale: en_US: 100.4 degrees Fahrenheit
```

## See Also

### Formatting a Measurement

- [formatted()](<formatted().md>) — Generates a locale-aware string representation of a measurement using the default measurement format style.
- [FormatStyle](formatstyle.md) — A type that provides localized representations of measurements.
- [AttributedStyle](attributedstyle.md) — A type that provides localized representations of measurements with an attributed string.
