---
title: 'init(position:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/reorderdifference/destination-swift.struct/init(position:)'
source_url: 'https://developer.apple.com/documentation/swiftui/reorderdifference/destination-swift.struct/init(position:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/reorderdifference/destination-swift.struct/init%28position%3A%29.json'
content_hash: 'sha256:8cf0f04d477d708d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [ReorderDifference](../../reorderdifference.md) · [Destination](../destination-swift.struct.md)

# init(position:)

<sub>Initializer</sub>

Initializes the destination value with the provided position and an instance of `ReorderableSingleCollectionIdentifier`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(position: ReorderDifference<ItemID, CollectionID>.Destination.Position) where CollectionID == ReorderableSingleCollectionIdentifier
```

## Discussion

- position: The position within the collection.
