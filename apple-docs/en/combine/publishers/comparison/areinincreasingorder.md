---
title: areInIncreasingOrder
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/comparison/areinincreasingorder
source_url: 'https://developer.apple.com/documentation/combine/publishers/comparison/areinincreasingorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/comparison/areinincreasingorder.json'
content_hash: 'sha256:279d0e6b0a56d5f2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Comparison](../comparison.md)

# areInIncreasingOrder

<sub>Instance Property</sub>

A closure that receives two elements and returns true if they are in increasing order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let areInIncreasingOrder: (Upstream.Output, Upstream.Output) -> Bool
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives its elements.
