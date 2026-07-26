---
title: 'trimmingPrefix(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collection/trimmingprefix(_:)'
source_url: 'https://developer.apple.com/documentation/swift/collection/trimmingprefix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/trimmingprefix%28_%3A%29.json'
content_hash: 'sha256:7e9e7e62386d0768'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# trimmingPrefix(_:)

<sub>Instance Method</sub>

Returns a new collection of the same type by removing `prefix` from the start of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func trimmingPrefix<Prefix>(_ prefix: Prefix) -> Self.SubSequence where Prefix : Sequence, Self.Element == Prefix.Element
```

## Parameters

- `prefix` — The collection to remove from this collection.

## Return Value

A collection containing the elements of the collection that are not removed by `prefix`.
