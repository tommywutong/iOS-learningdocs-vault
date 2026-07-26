---
title: url
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/parsestrategy/url
source_url: 'https://developer.apple.com/documentation/foundation/parsestrategy/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/parsestrategy/url.json'
content_hash: 'sha256:cfba7d2c44e4a6b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ParseStrategy](../parsestrategy.md)

# url

<sub>Type Property</sub>

A parse strategy for URLs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var url: URL.ParseStrategy { get }
```

## Discussion

Use the dot-notation form of this type property when the call point allows the use of [ParseStrategy](../url/parsestrategy.md). Typically, you use this with the URL initializer [init(_:strategy:)](<../url/init(__strategy_).md>).

## See Also

### Commonly-used parsers

- [fixed(format:timeZone:locale:)](<fixed(format_timezone_locale_).md>) — A fixed-format date parse strategy.
- [name](name.md) — A parse strategy for person name components.
