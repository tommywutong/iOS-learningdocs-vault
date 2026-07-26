---
title: 'init(format:lenient:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/parsestrategy/init(format:lenient:)-46ix2'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/parsestrategy/init(format:lenient:)-46ix2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/parsestrategy/init%28format%3Alenient%3A%29-46ix2.json'
content_hash: 'sha256:817292d695a645f5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Decimal](../../decimal.md) · [ParseStrategy](../parsestrategy.md)

# init(format:lenient:)

<sub>Initializer</sub>

Creates a parse strategy instance using the specified decimal format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(format: Format, lenient: Bool = true)
```

## Parameters

- `format` — A configured [FormatStyle](../formatstyle.md) that describes the string format to parse.

- `lenient` — A Boolean value that indicates whether the parse strategy should permit some discrepencies when parsing. Defaults to `true`.

## See Also

### Creating a decimal parse strategy

- [init(format:lenient:)](<init(format_lenient_)-22h06.md>) — Creates a parse strategy instance using the specified decimal currency format style.
- [init(format:lenient:)](<init(format_lenient_)-36ja3.md>) — Creates a parse strategy instance using the specified decimal percentage format style.
