---
title: 'init(upstream:size:prefetch:whenFull:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/buffer/init(upstream:size:prefetch:whenfull:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/buffer/init(upstream:size:prefetch:whenfull:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/buffer/init%28upstream%3Asize%3Aprefetch%3Awhenfull%3A%29.json'
content_hash: 'sha256:714b0777c7bb7d34'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Buffer](../buffer.md)

# init(upstream:size:prefetch:whenFull:)

<sub>Initializer</sub>

Creates a publisher that buffers elements received from an upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Publishers.Buffer<Upstream>.Failure>)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `size` — The maximum number of elements to store.

- `prefetch` — The strategy for initially populating the buffer.

- `whenFull` — The action to take when the buffer becomes full.
