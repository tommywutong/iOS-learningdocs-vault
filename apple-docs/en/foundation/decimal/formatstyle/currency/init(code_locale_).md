---
title: 'init(code:locale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/formatstyle/currency/init(code:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/currency/init(code:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/currency/init%28code%3Alocale%3A%29.json'
content_hash: 'sha256:238eebaf9dda25f0'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Decimal](../../../decimal.md) · [FormatStyle](../../formatstyle.md) · [Currency](../currency.md)

# init(code:locale:)

<sub>Initializer</sub>

Creates a decimal currency format style that uses the given currency code and locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(code: String, locale: Locale = .autoupdatingCurrent)
```

## Parameters

- `code` — The currency code to use, such as `EUR` or `JPY`.

- `locale` — The locale to use when formatting or parsing decimal values. Defaults to [autoupdatingCurrent](../../../locale/autoupdatingcurrent.md).
