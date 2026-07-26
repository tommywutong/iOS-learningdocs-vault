---
title: Indices
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collection/indices-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swift/collection/indices-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/indices-swift.associatedtype.json'
content_hash: 'sha256:0dcf5f989fb29702'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# Indices

<sub>Associated Type</sub>

A type that represents the indices that are valid for subscripting the collection, in ascending order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Indices : Collection = DefaultIndices<Self> where Self.Indices == Self.Indices.SubSequence
```
