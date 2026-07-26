---
title: 'measurement(width:usage:hidesScaleName:numberFormatStyle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/measurement(width:usage:hidesscalename:numberformatstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/measurement(width:usage:hidesscalename:numberformatstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/measurement%28width%3Ausage%3Ahidesscalename%3Anumberformatstyle%3A%29.json'
content_hash: 'sha256:9af1d96e12573d89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# measurement(width:usage:hidesScaleName:numberFormatStyle:)

<sub>Type Method</sub>

Returns a format style to format temperature units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func measurement(width: Measurement<UnitTemperature>.FormatStyle.UnitWidth = .abbreviated, usage: MeasurementFormatUnitUsage<UnitTemperature> = .general, hidesScaleName: Bool = false, numberFormatStyle: FloatingPointFormatStyle<Double>? = nil) -> Self where Self == Measurement<UnitTemperature>.FormatStyle
```

## Parameters

- `width` — The width — such as full names or abbreviations — with which to present units.

- `usage` — The contextual usage of the measurement unit, such as whether a temperature applies to a person or to the weather.

- `hidesScaleName` — A Boolean value that directs the formatter to hide the name of the scale (Kelvin, degrees Celsius, or degrees Fahrenheit). Defaults to `false`.

- `numberFormatStyle` — The format style with which to format the numeric part of the temperature.

## Return Value

A format style that formats measurements according to the given parameters.

## Discussion

Use this static method when the call point allows the use of [FormatStyle](../measurement/formatstyle.md) and the value type is `Measurement<UnitTemperature>`. You typically do this when calling the [formatted(_:)](<../measurement/formatted(__).md>) method of [Measurement](../measurement.md).

The following example creates an array of [Measurement](../measurement.md) values that represent body temperatures from a human patient. It then uses [formatted(_:)](<../measurement/formatted(__).md>) and the format style provided by this method to format the distances. The style specifies the [person](../measurementformatunitusage/person-4ifk7.md) usage to clarify that the temperatures refer to a person’s body temperature, as opposed to other uses like weather.

```swift
let rawTemparatures: [Double] = [36.4, 36.6, 37.0, 36.9, 36.7]
let temperatures = rawTemparatures.map { Measurement(value: $0, unit: UnitTemperature.celsius) }
let formattedTemperatures = temperatures.map { $0.formatted(
    .measurement(width: .abbreviated,
                 usage: .person,
                 hidesScaleName: false,
                 numberFormatStyle: .number)) } // ["36.4°C", "36.6°C", "37°C", "36.9°C", "36.7°C"]
```

## See Also

### Applying measurement styles

- [measurement(width:usage:numberFormatStyle:)](<measurement(width_usage_numberformatstyle_).md>) — Returns a format style to format measurement units.
