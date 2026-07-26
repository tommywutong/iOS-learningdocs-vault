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
doc_path: '/documentation/combine/publishers/dropuntiloutput/init(upstream:other:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/dropuntiloutput/init(upstream:other:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/dropuntiloutput/init%28upstream%3Aother%3A%29.json'
content_hash: 'sha256:95ab38a1d8cb5e96'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [DropUntilOutput](../dropuntiloutput.md)

# init(upstream:other:)

<sub>Initializer</sub>

Creates a publisher that ignores elements from the upstream publisher until it receives an element from another publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, other: Other)
```

## Parameters

- `upstream` — A publisher to drop elements from while waiting for another publisher to emit elements.

- `other` — A publisher to monitor for its first emitted element.
