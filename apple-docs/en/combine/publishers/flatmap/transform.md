---
title: transform
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/flatmap/transform
source_url: 'https://developer.apple.com/documentation/combine/publishers/flatmap/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/flatmap/transform.json'
content_hash: 'sha256:585108956846fed2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [FlatMap](../flatmap.md)

# transform

<sub>Instance Property</sub>

A closure that takes an element as a parameter and returns a publisher that produces elements of that type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let transform: (Upstream.Output) -> NewPublisher
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [maxPublishers](maxpublishers.md) — The maximum number of concurrent publisher subscriptions
