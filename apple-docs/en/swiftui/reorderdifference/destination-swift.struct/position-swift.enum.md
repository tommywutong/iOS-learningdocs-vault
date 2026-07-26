---
title: ReorderDifference.Destination.Position
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/reorderdifference/destination-swift.struct/position-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/reorderdifference/destination-swift.struct/position-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/reorderdifference/destination-swift.struct/position-swift.enum.json'
content_hash: 'sha256:dee1dbca1cecad73'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [ReorderDifference](../../reorderdifference.md) · [Destination](../destination-swift.struct.md)

# ReorderDifference.Destination.Position

<sub>Enumeration</sub>

The position within the destination collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Position
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Destination positions

- [ReorderDifference.Destination.Position.before(_:)](<position-swift.enum/before(__).md>) — The position of the item with the associated identifier in its collection. Move source items to the index of this item. _(beta)_
- [ReorderDifference.Destination.Position.end](position-swift.enum/end.md) — The end of the collection. Append source items to the end of the collection. _(beta)_

## See Also

### Getting destination details

- [collectionID](collectionid.md) — The collection that contains the destination’s position. _(beta)_
- [position](position-swift.property.md) — The identifier position in the collection where the sources should be moved to. _(beta)_
