---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collection/contains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/collection/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/contains%28_%3A%29.json'
content_hash: 'sha256:d0d4a5e481ad7c95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the collection contains the given sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains<C>(_ other: C) -> Bool where C : Collection, Self.Element == C.Element
```

## Parameters

- `other` — A sequence to search for within this collection.

## Return Value

`true` if the collection contains the specified sequence, otherwise `false`.
