---
title: 'init(_:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/asyncpublisher/init(_:)'
source_url: 'https://developer.apple.com/documentation/combine/asyncpublisher/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/asyncpublisher/init%28_%3A%29.json'
content_hash: 'sha256:5e162fdc0fdd904a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [AsyncPublisher](../asyncpublisher.md)

# init(_:)

<sub>Initializer</sub>

Creates a publisher that exposes elements received from an upstream publisher as an asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ publisher: P)
```

## Parameters

- `publisher` — An upstream publisher. The asynchronous publisher converts elements received from this publisher into an asynchronous sequence.
