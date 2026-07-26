---
title: 'locale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/formatstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/locale%28_%3A%29.json'
content_hash: 'sha256:9a914271b56679e9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [FormatStyle](../formatstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the measurement format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> Measurement<UnitType>.FormatStyle
```

## Parameters

- `locale` — The locale to use when formatting a measurement.

## Return Value

A measurement format style with the specified locale.

## See Also

### Modifying a measurement format style

- [width](width.md) — The width of the measurement unit.
- [UnitWidth](unitwidth.md) — Specifies the width of the unit, determining the textual representation.
- [numberFormatStyle](numberformatstyle.md) — The formatting of the measurement value.
- [usage](usage.md) — The intended purpose of the formatted measurement.
- [hidesScaleName](hidesscalename.md) — The visibility of the unit name of a temperature.
- [locale](locale.md) — The locale of the format style.
