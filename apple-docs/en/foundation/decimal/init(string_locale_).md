---
title: 'init(string:locale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/init(string:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/init(string:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/init%28string%3Alocale%3A%29.json'
content_hash: 'sha256:d06601e0df08be32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Decimal](../decimal.md)

# init(string:locale:)

<sub>Initializer</sub>

Creates and initializes a decimal by parsing a string according to the provided locale’s conventions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(string: String, locale: Locale? = nil)
```

## Parameters

- `string` — A string containing a formatted decimal value.

- `locale` — A locale that indicates the formatting conventions used by `string`.

## See Also

### Creating a decimal by parsing a string

- [init(_:format:lenient:)](<init(__format_lenient_)-6fk71.md>) — Creates and initializes a decimal by parsing a string according to the provided format style.
- [init(_:format:lenient:)](<init(__format_lenient_)-8t5o2.md>) — Creates and initializes a decimal by parsing a string according to the provided currency format style.
- [init(_:format:lenient:)](<init(__format_lenient_)-3u6o6.md>) — Creates and initializes a percentage decimal by parsing a string according to the provided format style.
- [init(_:strategy:)](<init(__strategy_).md>) — Creates and initializes a decimal by parsing an arbitrary type according to the provided parse strategy.
- [ParseStrategy](parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.
