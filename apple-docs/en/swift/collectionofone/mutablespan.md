---
title: mutableSpan
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collectionofone/mutablespan
source_url: 'https://developer.apple.com/documentation/swift/collectionofone/mutablespan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone/mutablespan.json'
content_hash: 'sha256:b5551f09bdbf0e36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionOfOne](../collectionofone.md)

# mutableSpan

<sub>Instance Property</sub>

A mutable span over the single element of this collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mutableSpan: MutableSpan<Element> { mutating get }
```

## Return Value

A `MutableSpan` over the element of this collection.

## Discussion

> [!abstract] Complexity
> O(1)
