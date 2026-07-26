---
title: startIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collectiondifference/startindex
source_url: 'https://developer.apple.com/documentation/swift/collectiondifference/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectiondifference/startindex.json'
content_hash: 'sha256:a416d996b66f4213'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionDifference](../collectiondifference.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a nonempty collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: CollectionDifference<ChangeElement>.Index { get }
```

## Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.
