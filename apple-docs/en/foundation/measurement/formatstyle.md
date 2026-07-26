---
title: Measurement.FormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle.json'
content_hash: 'sha256:59c8cfee1f27e572'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# Measurement.FormatStyle

<sub>Structure</sub>

A type that provides localized representations of measurements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FormatStyle
```

## Overview

A measurement format style creates human-readable text from a [Measurement](../measurement.md). You can customize the formatting behavior of the format style using the [width](formatstyle/width.md), `numberFormat`, [usage](formatstyle/usage.md), and [locale](formatstyle/locale.md) properties. The system automatically caches unique configurations of [FormatStyle](formatstyle.md) to enhance performance.

Use either the [formatted()](<formatted().md>) or the [formatted(_:)](<formatted(__).md>) instance method of [Measurement](../measurement.md) to create a string representation of a measurement.

The [formatted()](<formatted().md>) method generates a string using the default measurement format style.

```swift
let temperature = Measurement<UnitTemperature>(value: 38, unit: .celsius)
temperature.formatted()
// For locale: en_US: 100°F
// For locale: fr_FR: 38°C
```

The default format style in the previous example abbreviates the measurement unit. To customize any of the properties of the formatted measurement, you provide a measurement format style to the [formatted(_:)](<formatted(__).md>) method. For example, to create a string with the full name of the unit, the code might resemble the following:

```swift
temperature.formatted(.measurement(width: .wide))
// For locale: en_US: 100 degrees Fahrenheit
// For locale: fr_FR: 38 degrés Celsius
```

The previous example uses a static factory method to create a measurement format style within the call to the [formatted(_:)](<formatted(__).md>) method. You can also create a measurement format style and pass it to the method, such as in the following example:

```swift
let distance = Measurement<UnitLength>(value: 36, unit: .miles)
let distanceStyle = Measurement<UnitLength>.FormatStyle(width: .wide, usage: .road)
distanceStyle.format(distance)
// for locale: en_US: 36 miles
// for locale: fr_FR: 58 kilomètres

```

After you create an instance of a format style, you can use it to format measurements of the same unit type.

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a measurement format style

- [init(width:locale:usage:numberFormatStyle:)](<formatstyle/init(width_locale_usage_numberformatstyle_).md>) — Creates an instance using the provided width, locale, usage type, and number format.
- [init(width:locale:usage:hidesScaleName:numberFormatStyle:)](<formatstyle/init(width_locale_usage_hidesscalename_numberformatstyle_).md>) — Creates an instance using the provided width, locale, usage type, number format, and the option to hide the unit name.

### Modifying a measurement format style

- [width](formatstyle/width.md) — The width of the measurement unit.
- [UnitWidth](formatstyle/unitwidth.md) — Specifies the width of the unit, determining the textual representation.
- [numberFormatStyle](formatstyle/numberformatstyle.md) — The formatting of the measurement value.
- [usage](formatstyle/usage.md) — The intended purpose of the formatted measurement.
- [hidesScaleName](formatstyle/hidesscalename.md) — The visibility of the unit name of a temperature.
- [locale](formatstyle/locale.md) — The locale of the format style.
- [locale(_:)](<formatstyle/locale(__).md>) — Modifies the measurement format style to use the specified locale.

### Inspecting a measurement format style

- [attributed](formatstyle/attributed.md) — The attributed style for the measurement format style.

### Formatting a measurement

- [format(_:)](<formatstyle/format(__).md>) — Creates a string representation of a measurement.

### Applying byte count styles

- [ByteCount](formatstyle/bytecount.md) — A format style that provides string representations of byte counts, expressed as measurements of information storage.
