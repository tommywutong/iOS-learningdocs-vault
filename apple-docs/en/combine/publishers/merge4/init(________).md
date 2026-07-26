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
doc_path: '/documentation/combine/publishers/merge4/init(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/merge4/init(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/merge4/init%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9132a4390dcce226'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Merge4](../merge4.md)

# init(_:_:_:_:)

<sub>Initializer</sub>

Creates a publisher created by applying the merge function to four upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ a: A, _ b: B, _ c: C, _ d: D)
```

## Parameters

- `a` — A publisher to merge

- `b` — A second publisher to merge.

- `c` — A third publisher to merge.

- `d` — A fourth publisher to merge.
