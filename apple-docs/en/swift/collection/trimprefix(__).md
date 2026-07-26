---
title: 'trimPrefix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collection/trimprefix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/collection/trimprefix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/trimprefix%28_%3A%29.json'
content_hash: 'sha256:5e45eaadb0fb12da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# trimPrefix(_:)

<sub>Instance Method</sub>

Removes `prefix` from the start of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func trimPrefix<Prefix>(_ prefix: Prefix) where Prefix : Sequence, Self.Element == Prefix.Element
```

## Parameters

- `prefix` — The collection to remove from this collection.
