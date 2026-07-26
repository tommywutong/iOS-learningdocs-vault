---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/formatstyle/bytecount/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/bytecount/format%28_%3A%29.json'
content_hash: 'sha256:0a14ae597a58fdba'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Measurement](../../../measurement.md) · [FormatStyle](../../formatstyle.md) · [ByteCount](../bytecount.md)

# format(_:)

<sub>Instance Method</sub>

Formats a byte count measurment, using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Measurement<UnitInformationStorage>) -> String
```

## Parameters

- `value` — The byte count measurement to format.

## Return Value

A formatted representation of `value`, formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values. The following example creates a [ByteCount](../bytecount.md) instance to format values as kilobyte counts, then applies this style to an array of [Measurement](../../../measurement.md) values.

```swift
let style = Measurement.FormatStyle.ByteCount(style: .memory,                                              
                                              allowedUnits: [.kb],
                                              spellsOutZero: true,
                                              includesActualByteCount: false,
                                              locale: Locale(identifier: "en_US"))
let counts: [Measurement] = [
    Measurement(value: 0, unit: UnitInformationStorage.bytes),
    Measurement(value: 1024, unit: UnitInformationStorage.bytes),
    Measurement(value: 2048, unit: UnitInformationStorage.bytes),
    Measurement(value: 4096, unit: UnitInformationStorage.bytes),
    Measurement(value: 8192, unit: UnitInformationStorage.bytes),
    Measurement(value: 16384, unit: UnitInformationStorage.bytes),
    Measurement(value: 32768, unit: UnitInformationStorage.bytes),
    Measurement(value: 65536, unit: UnitInformationStorage.bytes)
]
let formatted = counts.map ( {style.format($0) } ) // ["Zero kB", "1 kB", "2 kB", "4 kB", "8 kB", "16 kB", "32 kB", "64 kB"]
```

To format a single data-storage measurement, use the Measurement instance method [formatted(_:)](<../../formatted(__).md>), passing in an instance of [ByteCount](../bytecount.md), or [formatted()](<../../formatted().md>) to use a default style.
