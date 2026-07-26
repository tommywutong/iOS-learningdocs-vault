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
doc_path: '/documentation/combine/publishers/autoconnect/init(upstream:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/autoconnect/init(upstream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/autoconnect/init%28upstream%3A%29.json'
content_hash: 'sha256:8846c51157757031'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Autoconnect](../autoconnect.md)

# init(upstream:)

<sub>Initializer</sub>

Creates a publisher that automatically connects to an upstream connectable publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.
