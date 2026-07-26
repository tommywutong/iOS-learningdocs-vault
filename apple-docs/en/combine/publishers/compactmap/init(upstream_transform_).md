---
title: 'init(upstream:transform:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/compactmap/init(upstream:transform:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/compactmap/init(upstream:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/compactmap/init%28upstream%3Atransform%3A%29.json'
content_hash: 'sha256:a85eba0e62cb531e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [CompactMap](../compactmap.md)

# init(upstream:transform:)

<sub>Initializer</sub>

Creates a publisher that republishes all non-`nil` results of calling a closure with each received element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, transform: @escaping (Upstream.Output) -> Output?)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `transform` — A closure that receives values from the upstream publisher and returns optional values.
