---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/formatstyle/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/format%28_%3A%29.json'
content_hash: 'sha256:08c64c0b158e116d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Decimal](../../decimal.md) · [FormatStyle](../formatstyle.md)

# format(_:)

<sub>Instance Method</sub>

Formats a decimal value using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Decimal) -> String
```

## Parameters

- `value` — The decimal value to format.

## Return Value

A string representation of `value` formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance and then use it to format multiple decimal values. The following example creates a style that uses the `en_US` locale and then adds the [scientific](../../numberformatstyleconfiguration/notation/scientific.md) modifier. It then applies this style to all of the decimal values in an array.

```swift
let scientificStyle = Decimal.FormatStyle(
    locale: Locale(identifier: "en_US"))
    .notation(.scientific)
let nums: [Decimal] = [100.1, 1000.2, 10000.3, 100000.4, 1000000.5]
let formattedNums = nums.map { scientificStyle.format($0) } // ["1.001E2", "1.0002E3", "1.00003E4", "1.000004E5", "1E6"]
```

To format a single floating-point value, use the [Decimal](../../decimal.md) instance method [formatted(_:)](<../formatted(__).md>), passing in an instance of [FormatStyle](../formatstyle.md), or [formatted()](<../formatted().md>) to use a default style.
