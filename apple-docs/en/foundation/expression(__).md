---
title: 'Expression(_:)'
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/expression(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/expression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/expression%28_%3A%29.json'
content_hash: 'sha256:f66f1198ffed314b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Expression(_:)

<sub>Macro</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro Expression<each Input, Output>(_ body: (repeat each Input) -> Output) -> Expression<repeat each Input, Output>
```

## See Also

### Macros

- [Predicate(_:)](<predicate(__).md>)
