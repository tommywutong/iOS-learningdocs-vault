---
title: 'init(_:_:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/zip/init(_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/zip/init(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/zip/init%28_%3A_%3A%29.json'
content_hash: 'sha256:91a90802c281f01d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Zip](../zip.md)

# init(_:_:)

<sub>Initializer</sub>

Creates a publisher that applies the zip function to two upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ a: A, _ b: B)
```

## Parameters

- `a` — A publisher to zip.

- `b` — Another publisher to zip.
