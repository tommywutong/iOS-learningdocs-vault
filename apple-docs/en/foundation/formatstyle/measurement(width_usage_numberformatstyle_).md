---
title: 'measurement(width:usage:numberFormatStyle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/measurement(width:usage:numberformatstyle:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/measurement(width:usage:numberformatstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/measurement%28width%3Ausage%3Anumberformatstyle%3A%29.json'
content_hash: 'sha256:8bffd79c0e5e3d93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# measurement(width:usage:numberFormatStyle:)

<sub>Type Method</sub>

Returns a format style to format measurement units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func measurement<UnitType>(width: Measurement<UnitType>.FormatStyle.UnitWidth, usage: MeasurementFormatUnitUsage<UnitType> = .general, numberFormatStyle: FloatingPointFormatStyle<Double>? = nil) -> Self where Self == Measurement<UnitType>.FormatStyle, UnitType : Dimension
```

## Parameters

- `width` — The width — such as full names or abbreviations — with which to present units.

- `usage` — The contextual usage of the measurement unit, such as whether a length measurement applies to a road distance or a person’s height.

- `numberFormatStyle` — The format style with which to format the numeric part of the measurement.

## Return Value

A format style that formats measurements according to the given parameters.

## Discussion

Use the dot-notation form of this type method when the call point allows the use of [FormatStyle](../measurement/formatstyle.md). You typically do this when calling the [formatted(_:)](<../measurement/formatted(__).md>) method of [Measurement](../measurement.md).

The following example creates an array of [Measurement](../measurement.md) values that represent distances measured in kilometers. It then uses [formatted(_:)](<../measurement/formatted(__).md>) and the format style provided by this method to format the distances. The style specifies the [asProvided](../measurementformatunitusage/asprovided.md) usage to keep the formatted measurements in kilometers. Without this, a non-Metric locale such as the US would convert the kilometers to a locale-appropriate unit, such as miles.

```swift
let rawDistances: [Double] = [100, 1000, 10000, 100000, 1000000]
let distances = rawDistances.map { Measurement(value: $0, unit: UnitLength.kilometers) }
let formattedDistances = distances.map { $0.formatted(
    .measurement(width: .narrow,
                 usage: .asProvided,
                 numberFormatStyle: .number)) } // ["100km", "1,000km", "10,000km", "100,000km", "1,000,000km"]
```

## See Also

### Applying measurement styles

- [measurement(width:usage:hidesScaleName:numberFormatStyle:)](<measurement(width_usage_hidesscalename_numberformatstyle_).md>) — Returns a format style to format temperature units.
