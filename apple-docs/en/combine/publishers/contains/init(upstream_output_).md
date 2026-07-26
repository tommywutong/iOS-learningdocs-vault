---
title: 'init(upstream:output:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/contains/init(upstream:output:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/contains/init(upstream:output:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/contains/init%28upstream%3Aoutput%3A%29.json'
content_hash: 'sha256:cf428eaa8e5b5f25'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Contains](../contains.md)

# init(upstream:output:)

<sub>Initializer</sub>

Creates a publisher that emits a Boolean value when it receives a specific element from its upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, output: Upstream.Output)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `output` — The element to match in the upstream publisher.
