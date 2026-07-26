---
title: 'init(mutating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/init(mutating:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/init(mutating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/init%28mutating%3A%29.json'
content_hash: 'sha256:c060aab92846726b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# init(mutating:)

<sub>Initializer</sub>

Mutate the elements of a typed span as bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Element>(mutating elements: inout MutableSpan<Element>) where Element : ConvertibleFromBytes, Element : ConvertibleToBytes
```

## Parameters

- `elements` — A typed span to reinterpret as raw bytes.

## Discussion

The stride of `Element` must equal its size, and the starting address of `elements` must be well-aligned for `Element`.
