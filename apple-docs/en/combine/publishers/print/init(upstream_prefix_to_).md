---
title: 'init(upstream:prefix:to:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/print/init(upstream:prefix:to:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/print/init(upstream:prefix:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/print/init%28upstream%3Aprefix%3Ato%3A%29.json'
content_hash: 'sha256:24a7163393309ee5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Print](../print.md)

# init(upstream:prefix:to:)

<sub>Initializer</sub>

Creates a publisher that prints log messages for all publishing events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, prefix: String, to stream: (any TextOutputStream)? = nil)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `prefix` — A string with which to prefix all log messages.
