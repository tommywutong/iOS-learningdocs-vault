---
title: 'init(upstream:maxPublishers:transform:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/flatmap/init(upstream:maxpublishers:transform:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/flatmap/init(upstream:maxpublishers:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/flatmap/init%28upstream%3Amaxpublishers%3Atransform%3A%29.json'
content_hash: 'sha256:a199e588928fc8d5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [FlatMap](../flatmap.md)

# init(upstream:maxPublishers:transform:)

<sub>Initializer</sub>

Creates a publisher that transforms elements from an upstream publisher into a new publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, maxPublishers: Subscribers.Demand, transform: @escaping (Upstream.Output) -> NewPublisher)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `maxPublishers` — The maximum number of concurrent publisher subscriptions.

- `transform` — A closure that takes an element as a parameter and returns a publisher that produces elements of that type.
