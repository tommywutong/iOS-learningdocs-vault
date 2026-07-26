---
title: 'init(mutableBytes:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablespan/init(mutablebytes:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablespan/init(mutablebytes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablespan/init%28mutablebytes%3A%29.json'
content_hash: 'sha256:1bc645ad1b3d8b11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableSpan](../mutablespan.md)

# init(mutableBytes:)

<sub>Initializer</sub>

Convert a raw span to a typed span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(mutableBytes: consuming MutableRawSpan)
```

## Parameters

- `mutableBytes` — A raw span to reinterpret as typed elements.

## Discussion

The `byteCount` of `mutableBytes` must be a multiple of `Element`’s stride, and the starting address of `mutableBytes` must be well-aligned for the type of `Element`. If either of these requirements is not met, this initializer will trap at runtime.
