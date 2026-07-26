---
title: 'init(_:format:lenient:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/init(_:format:lenient:)-6fk71'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/init(_:format:lenient:)-6fk71'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/init%28_%3Aformat%3Alenient%3A%29-6fk71.json'
content_hash: 'sha256:c324ecd48e92cf2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Decimal](../decimal.md)

# init(_:format:lenient:)

<sub>Initializer</sub>

Creates and initializes a decimal by parsing a string according to the provided format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: String, format: Decimal.FormatStyle, lenient: Bool = true) throws
```

## Parameters

- `value` — A string that contains a formatted decimal value.

- `format` — A format style that describes formatting conventions used by the string. The initializer uses this format’s [ParseStrategy](parsestrategy.md) to parse the string.

- `lenient` — A Boolean value that indicates whether the parse strategy should permit some discrepancies when parsing. Defaults to `true`.

## Discussion

This initializer throws an error if the format style fails to parse the string into a decimal value.

## See Also

### Creating a decimal by parsing a string

- [init(_:format:lenient:)](<init(__format_lenient_)-8t5o2.md>) — Creates and initializes a decimal by parsing a string according to the provided currency format style.
- [init(_:format:lenient:)](<init(__format_lenient_)-3u6o6.md>) — Creates and initializes a percentage decimal by parsing a string according to the provided format style.
- [init(string:locale:)](<init(string_locale_).md>) — Creates and initializes a decimal by parsing a string according to the provided locale’s conventions.
- [init(_:strategy:)](<init(__strategy_).md>) — Creates and initializes a decimal by parsing an arbitrary type according to the provided parse strategy.
- [ParseStrategy](parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.
