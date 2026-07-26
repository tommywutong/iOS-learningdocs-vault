---
title: 'init(upstream:other:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/prefixuntiloutput/init(upstream:other:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/prefixuntiloutput/init(upstream:other:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/prefixuntiloutput/init%28upstream%3Aother%3A%29.json'
content_hash: 'sha256:18956a337eea8ad2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [PrefixUntilOutput](../prefixuntiloutput.md)

# init(upstream:other:)

<sub>Initializer</sub>

Creates a publisher that republishes elements until another publisher emits an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, other: Other)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `other` — Another publisher, the first output from which causes this publisher to finish.
