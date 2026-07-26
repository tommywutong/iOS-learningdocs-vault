---
title: formatted()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatted()
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatted%28%29.json'
content_hash: 'sha256:85275e8f38b74cbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# formatted()

<sub>Instance Method</sub>

Generates a locale-aware string representation of a measurement using the default measurement format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted() -> String
```

## Return Value

A string, formatted according to the default style.

## Discussion

Use the [formatted()](<formatted().md>) method to apply the default format style to a measurement, such as in the following example:

```swift
let string = Measurement<UnitTemperature>(value: 38, unit: .celsius).formatted()
// For locale: en_US: 100.4°F
```

The default measurement format style uses an [abbreviated](formatstyle/unitwidth/abbreviated.md) unit width, the general usage type, and the default number format style. To customize the formatted measurement string, use the [formatted(_:)](<formatted(__).md>) method and include a [FormatStyle](formatstyle.md).

## See Also

### Formatting a Measurement

- [formatted(_:)](<formatted(__).md>) — Generates a locale-aware string representation of a measurement using the provided measurement format style.
- [FormatStyle](formatstyle.md) — A type that provides localized representations of measurements.
- [AttributedStyle](attributedstyle.md) — A type that provides localized representations of measurements with an attributed string.
