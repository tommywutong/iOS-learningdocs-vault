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
doc_path: '/documentation/swift/rangereplaceablecollection/trimprefix(_:)-3t4tj'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/trimprefix(_:)-3t4tj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/trimprefix%28_%3A%29-3t4tj.json'
content_hash: 'sha256:98cfec2fc275aade'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# trimPrefix(_:)

<sub>Instance Method</sub>

Removes `prefix` from the start of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func trimPrefix<Prefix>(_ prefix: Prefix) where Prefix : Sequence, Self.Element == Prefix.Element
```

## Parameters

- `prefix` — The collection to remove from this collection.
