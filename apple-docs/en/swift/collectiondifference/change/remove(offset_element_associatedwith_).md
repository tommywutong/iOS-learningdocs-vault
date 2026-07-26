---
title: 'CollectionDifference.Change.remove(offset:element:associatedWith:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collectiondifference/change/remove(offset:element:associatedwith:)'
source_url: 'https://developer.apple.com/documentation/swift/collectiondifference/change/remove(offset:element:associatedwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectiondifference/change/remove%28offset%3Aelement%3Aassociatedwith%3A%29.json'
content_hash: 'sha256:2cbf8da3a51466c9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [CollectionDifference](../../collectiondifference.md) · [Change](../change.md)

# CollectionDifference.Change.remove(offset:element:associatedWith:)

<sub>Case</sub>

A removal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case remove(offset: Int, element: ChangeElement, associatedWith: Int?)
```

## Discussion

The `offset` value is the offset of the element to be removed in the original state of the collection. A non-`nil` `associatedWith` value is the offset of the complementary change.
