---
title: maxPublishers
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/flatmap/maxpublishers
source_url: 'https://developer.apple.com/documentation/combine/publishers/flatmap/maxpublishers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/flatmap/maxpublishers.json'
content_hash: 'sha256:649e85ecac72573e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [FlatMap](../flatmap.md)

# maxPublishers

<sub>Instance Property</sub>

The maximum number of concurrent publisher subscriptions

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let maxPublishers: Subscribers.Demand
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [transform](transform.md) — A closure that takes an element as a parameter and returns a publisher that produces elements of that type.
