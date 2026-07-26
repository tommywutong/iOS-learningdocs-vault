---
title: ReorderDifference.Destination
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/reorderdifference/destination-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftui/reorderdifference/destination-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/reorderdifference/destination-swift.struct.json'
content_hash: 'sha256:533369fd4bd73619'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReorderDifference](../reorderdifference.md)

# ReorderDifference.Destination

<sub>Structure</sub>

The destination value of a reordering operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Destination
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting destination details

- [collectionID](destination-swift.struct/collectionid.md) — The collection that contains the destination’s position. _(beta)_
- [position](destination-swift.struct/position-swift.property.md) — The identifier position in the collection where the sources should be moved to. _(beta)_
- [Position](destination-swift.struct/position-swift.enum.md) — The position within the destination collection. _(beta)_

### Initializers

- [init(position:)](<destination-swift.struct/init(position_).md>) — Initializes the destination value with the provided position and an instance of `ReorderableSingleCollectionIdentifier`. _(beta)_
- [init(position:collectionID:)](<destination-swift.struct/init(position_collectionid_).md>) — Initializes the destination value with the provided position and collectionID. _(beta)_

## See Also

### Getting changes

- [destination](destination-swift.property.md) — The end position of items to move during a reordering operation. _(beta)_
- [sources](sources.md) — The identifiers of items to move during a reordering operation. _(beta)_
