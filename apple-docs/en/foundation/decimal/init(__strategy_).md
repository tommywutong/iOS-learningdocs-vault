---
title: 'init(_:strategy:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/init(_:strategy:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/init(_:strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/init%28_%3Astrategy%3A%29.json'
content_hash: 'sha256:d7f7c7a0b8d82307'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Decimal](../decimal.md)

# init(_:strategy:)

<sub>Initializer</sub>

Creates and initializes a decimal by parsing an arbitrary type according to the provided parse strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ value: S.ParseInput, strategy: S) throws where S : ParseStrategy, S.ParseOutput == Decimal
```

## Parameters

- `value` — An instance of `strategy`’s input type.

- `strategy` — A parse strategy that describes how the parser converts the string to a decimal value.

## See Also

### Creating a decimal by parsing a string

- [init(_:format:lenient:)](<init(__format_lenient_)-6fk71.md>) — Creates and initializes a decimal by parsing a string according to the provided format style.
- [init(_:format:lenient:)](<init(__format_lenient_)-8t5o2.md>) — Creates and initializes a decimal by parsing a string according to the provided currency format style.
- [init(_:format:lenient:)](<init(__format_lenient_)-3u6o6.md>) — Creates and initializes a percentage decimal by parsing a string according to the provided format style.
- [init(string:locale:)](<init(string_locale_).md>) — Creates and initializes a decimal by parsing a string according to the provided locale’s conventions.
- [ParseStrategy](parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.
