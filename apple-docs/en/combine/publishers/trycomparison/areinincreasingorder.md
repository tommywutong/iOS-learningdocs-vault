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
doc_path: /documentation/combine/publishers/trycomparison/areinincreasingorder
source_url: 'https://developer.apple.com/documentation/combine/publishers/trycomparison/areinincreasingorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trycomparison/areinincreasingorder.json'
content_hash: 'sha256:fcfd59e9d0378224'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryComparison](../trycomparison.md)

# areInIncreasingOrder

<sub>Instance Property</sub>

A closure that receives two elements and returns true if they are in increasing order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let areInIncreasingOrder: (Upstream.Output, Upstream.Output) throws -> Bool
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives its elements.
