---
title: 'init(_:comparator:order:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/keypathcomparator/init(_:comparator:order:)-749jk'
source_url: 'https://developer.apple.com/documentation/foundation/keypathcomparator/init(_:comparator:order:)-749jk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/keypathcomparator/init%28_%3Acomparator%3Aorder%3A%29-749jk.json'
content_hash: 'sha256:13eee46730d00a8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [KeyPathComparator](../keypathcomparator.md)

# init(_:comparator:order:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Value, Comparator>(_ keyPath: any KeyPath<Compared, Value> & Sendable, comparator: Comparator, order: SortOrder) where Value == Comparator.Compared, Comparator : SortComparator
```

## See Also

### Initializers

- [init(_:comparator:)](<init(__comparator_)-8b13q.md>)
- [init(_:comparator:)](<init(__comparator_)-284rt.md>)
- [init(_:comparator:order:)](<init(__comparator_order_)-3gjxd.md>)
- [init(_:order:)](<init(__order_)-6r8gw.md>)
- [init(_:order:)](<init(__order_)-4hyoi.md>)
