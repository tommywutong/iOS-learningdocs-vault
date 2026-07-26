---
title: predicate
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/firstwhere/predicate
source_url: 'https://developer.apple.com/documentation/combine/publishers/firstwhere/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/firstwhere/predicate.json'
content_hash: 'sha256:2f73f759d472d4c5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [FirstWhere](../firstwhere.md)

# predicate

<sub>Instance Property</sub>

The closure that determines whether to publish an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let predicate: (Publishers.FirstWhere<Upstream>.Output) -> Bool
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
