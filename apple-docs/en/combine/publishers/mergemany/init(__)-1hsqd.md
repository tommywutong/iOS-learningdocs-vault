---
title: 'init(_:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/mergemany/init(_:)-1hsqd'
source_url: 'https://developer.apple.com/documentation/combine/publishers/mergemany/init(_:)-1hsqd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/mergemany/init%28_%3A%29-1hsqd.json'
content_hash: 'sha256:e3aaa3c2e180de91'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [MergeMany](../mergemany.md)

# init(_:)

<sub>Initializer</sub>

Creates a publisher created by applying the merge function to an arbitrary number of upstream publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ upstream: Upstream...)
```

## Parameters

- `upstream` — A variadic parameter containing zero or more publishers to merge with this publisher.

## See Also

### Creating a merge many publisher

- [init(_:)](<init(__)-3hrmo.md>) — Creates a publisher created by applying the merge function to a sequence of upstream publishers.
