---
title: Strategy
framework: Foundation
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/parseableformatstyle/strategy
source_url: 'https://developer.apple.com/documentation/foundation/parseableformatstyle/strategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/parseableformatstyle/strategy.json'
content_hash: 'sha256:4eadde56e29a6f30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ParseableFormatStyle](../parseableformatstyle.md)

# Strategy

<sub>Associated Type</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Strategy : ParseStrategy where Self.FormatInput == Self.Strategy.ParseOutput, Self.FormatOutput == Self.Strategy.ParseInput
```

## See Also

### Declaring Parse Strategy

- [parseStrategy](parsestrategy.md) — A `ParseStrategy` that can be used to parse this `FormatStyle`’s output
