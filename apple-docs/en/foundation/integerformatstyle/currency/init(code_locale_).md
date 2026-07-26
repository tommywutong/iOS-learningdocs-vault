---
title: 'init(code:locale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/currency/init(code:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/currency/init(code:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/currency/init%28code%3Alocale%3A%29.json'
content_hash: 'sha256:798f1111c5f7dda5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [IntegerFormatStyle](../../integerformatstyle.md) · [Currency](../currency.md)

# init(code:locale:)

<sub>Initializer</sub>

Creates an integer currency format style that uses the given currency code and locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(code: String, locale: Locale = .autoupdatingCurrent)
```

## Parameters

- `code` — The currency code to use, such as `EUR` or `JPY`.

- `locale` — The locale to use when formatting or parsing integers. Defaults to [autoupdatingCurrent](../../locale/autoupdatingcurrent.md).
