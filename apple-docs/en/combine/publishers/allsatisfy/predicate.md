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
doc_path: /documentation/combine/publishers/allsatisfy/predicate
source_url: 'https://developer.apple.com/documentation/combine/publishers/allsatisfy/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/allsatisfy/predicate.json'
content_hash: 'sha256:0f9d6dab50e01c46'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [AllSatisfy](../allsatisfy.md)

# predicate

<sub>Instance Property</sub>

A closure that evaluates each received element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let predicate: (Upstream.Output) -> Bool
```

## Discussion

Return `true` to continue, or `false` to cancel the upstream and finish.

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
