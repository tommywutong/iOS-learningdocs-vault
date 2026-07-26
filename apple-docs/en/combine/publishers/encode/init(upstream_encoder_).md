---
title: 'init(upstream:encoder:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/encode/init(upstream:encoder:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/encode/init(upstream:encoder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/encode/init%28upstream%3Aencoder%3A%29.json'
content_hash: 'sha256:9c3bf064e7f97115'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Encode](../encode.md)

# init(upstream:encoder:)

<sub>Initializer</sub>

Creates a publisher that decodes elements received from an upstream publisher, using a given decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, encoder: Coder)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `encoder` — The encoder that decodes elements received from the upstream publisher.
