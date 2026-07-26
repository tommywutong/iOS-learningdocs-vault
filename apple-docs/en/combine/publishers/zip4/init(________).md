---
title: 'init(_:_:_:_:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/zip4/init(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/zip4/init(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/zip4/init%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:dd903c143ad00531'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Zip4](../zip4.md)

# init(_:_:_:_:)

<sub>Initializer</sub>

Creates a publisher created by applying the zip function to four upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ a: A, _ b: B, _ c: C, _ d: D)
```

## Parameters

- `a` — A publisher to zip.

- `b` — A second publisher to zip.

- `c` — A third publisher to zip.

- `d` — A fourth publisher to zip.
