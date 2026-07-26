---
title: 'fixed(format:timeZone:locale:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/parsestrategy/fixed(format:timezone:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/parsestrategy/fixed(format:timezone:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/parsestrategy/fixed%28format%3Atimezone%3Alocale%3A%29.json'
content_hash: 'sha256:3eda46bb75ce244a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ParseStrategy](../parsestrategy.md)

# fixed(format:timeZone:locale:)

<sub>Type Method</sub>

A fixed-format date parse strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func fixed(format: Date.FormatString, timeZone: TimeZone, locale: Locale? = nil) -> Self where Self == Date.ParseStrategy
```

## Parameters

- `format` — The string describing the parsing format.

- `timeZone` — The [TimeZone](../timezone.md) used to create the string representation of the date.

- `locale` — The [Locale](../locale.md) used to create the string representation of the date.

## Return Value

A strategy for parsing a date.

## See Also

### Commonly-used parsers

- [url](url.md) — A parse strategy for URLs.
- [name](name.md) — A parse strategy for person name components.
