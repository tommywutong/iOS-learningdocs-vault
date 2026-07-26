---
title: 'init(upstream:decoder:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/decode/init(upstream:decoder:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/decode/init(upstream:decoder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/decode/init%28upstream%3Adecoder%3A%29.json'
content_hash: 'sha256:94ce8d6bbeb2b17a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Decode](../decode.md)

# init(upstream:decoder:)

<sub>Initializer</sub>

Creates a publisher that decodes elements received from an upstream publisher, using a given decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, decoder: Coder)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `decoder` — The decoder that decodes elements received from the upstream publisher.
