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
doc_path: '/documentation/foundation/decimal/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatted%28_%3A%29.json'
content_hash: 'sha256:01d6bb3f50a01075'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Decimal](../decimal.md)

# formatted(_:)

<sub>Instance Method</sub>

Formats the decimal using the provided format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ format: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Decimal
```

## Parameters

- `format` — The format style to apply when formatting the decimal.

## Return Value

A localized, formatted string representation of the decimal.

## Discussion

Use this method when you want to format a single decimal value with a specific format style or multiple format styles. The following example shows the results of formatting a given decimal value with format styles for the `en_US` and `fr_FR` locales:

```swift
let decimal: Decimal = 123456.789
let usStyle = Decimal.FormatStyle(locale: Locale(identifier: "en_US"))
let frStyle = Decimal.FormatStyle(locale: Locale(identifier: "fr_FR"))
let formattedUS = decimal.formatted(usStyle) // 123,456.789
let formattedFR = decimal.formatted(frStyle) // 123 456,789
```

## See Also

### Formatting decimals

- [formatted()](<formatted().md>) — Formats the decimal using a default localized format style.
- [FormatStyle](formatstyle.md) — A structure that converts between decimal values and their textual representations.
