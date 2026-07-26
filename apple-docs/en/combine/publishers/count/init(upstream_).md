---
title: 'init(upstream:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/count/init(upstream:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/count/init(upstream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/count/init%28upstream%3A%29.json'
content_hash: 'sha256:4b7182aee9ae951c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Count](../count.md)

# init(upstream:)

<sub>Initializer</sub>

Creates a publisher that publishes the number of elements received from the upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.
