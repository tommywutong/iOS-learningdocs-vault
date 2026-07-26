---
title: 'init(upstream:range:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/output/init(upstream:range:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/output/init(upstream:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/output/init%28upstream%3Arange%3A%29.json'
content_hash: 'sha256:f87e7731642dec3f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Output](../output.md)

# init(upstream:range:)

<sub>Initializer</sub>

Creates a publisher that publishes elements specified by a range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, range: CountableRange<Int>)
```

## Parameters

- `upstream` — The publisher from which this publisher receives its elements.

- `range` — The range of elements to publish.
