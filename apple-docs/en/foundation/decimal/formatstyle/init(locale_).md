---
title: 'init(locale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/formatstyle/init(locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/init(locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/init%28locale%3A%29.json'
content_hash: 'sha256:6628d7da12f23c9b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Decimal](../../decimal.md) · [FormatStyle](../formatstyle.md)

# init(locale:)

<sub>Initializer</sub>

Creates a decimal format style that uses the given locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(locale: Locale = .autoupdatingCurrent)
```

## Parameters

- `locale` — The locale to use when formatting or parsing decimal values. Defaults to [autoupdatingCurrent](../../locale/autoupdatingcurrent.md).

## Discussion

Create a [FormatStyle](../formatstyle.md) instance when you intend to apply a given style to multiple decimal values. The following example creates a style that uses the `en_US` locale, which uses three-based grouping and comma separators. It then applies this style to all the [Decimal](../../decimal.md) values in an array.

```swift
let enUSstyle = Decimal.FormatStyle(locale: Locale(identifier: "en_US"))
let decimals: [Decimal] = [100.1, 1000.2, 10000.3, 100000.4, 1000000.5]
let formattedDecimals = decimals.map { enUSstyle.format($0) } // ["100.1", "1,000.2", "10,000.3", "100,000.4", "1,000,000.5"]
```

To format a single integer, you can use the [Decimal](../../decimal.md) instance method [formatted(_:)](<../formatted(__).md>) passing in an instance of [FormatStyle](../formatstyle.md).
