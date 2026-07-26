---
title: 'init(upstream:count:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/collectbycount/init(upstream:count:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/collectbycount/init(upstream:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/collectbycount/init%28upstream%3Acount%3A%29.json'
content_hash: 'sha256:c14743742e63c63e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [CollectByCount](../collectbycount.md)

# init(upstream:count:)

<sub>Initializer</sub>

Creates a publisher that buffers a maximum number of items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, count: Int)
```

## Parameters

- `upstream` — The publisher that this publisher receives elements from.

- `count` — The maximum number of received elements to buffer before publishing.
