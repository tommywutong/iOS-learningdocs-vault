---
title: ReorderableSingleCollectionIdentifier
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/reorderablesinglecollectionidentifier
source_url: 'https://developer.apple.com/documentation/swiftui/reorderablesinglecollectionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/reorderablesinglecollectionidentifier.json'
content_hash: 'sha256:54c69dfb639cc17e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ReorderableSingleCollectionIdentifier

<sub>Structure</sub>

An opaque, empty type used to identify reorderable containers and modifiers with only a single collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ReorderableSingleCollectionIdentifier
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Reordering items

- [Making a card game with drag, drop, and reordering in SwiftUI](making-a-card-game-with-drag-drop-and-reordering-in-swiftui.md) — Move cards between positions in a card game using drag, drop, and reordering modifiers.
- [reorderable()](<dynamicviewcontent/reorderable().md>) — Enables reordering of views from this content inside the scope of a reorderable container modifier. _(beta)_
- [reorderable(collectionID:)](<dynamicviewcontent/reorderable(collectionid_).md>) — Enables reordering views from this content within and between sections in the scope of a reorderable container modifier. _(beta)_
- [reorderContainer(for:isEnabled:move:)](<view/reordercontainer(for_isenabled_move_).md>) — Defines a container of reorderable views. _(beta)_
- [reorderContainer(for:in:isEnabled:move:)](<view/reordercontainer(for_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type you specify to identify sections. _(beta)_
- [reorderContainer(for:itemID:isEnabled:move:)](<view/reordercontainer(for_itemid_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you specify to identify items. _(beta)_
- [reorderContainer(for:itemID:in:isEnabled:move:)](<view/reordercontainer(for_itemid_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections. _(beta)_
- [reorderDestination(for:in:)](<dropsession/reorderdestination(for_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [reorderDestination(for:itemID:in:)](<dropsession/reorderdestination(for_itemid_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [ReorderDifference](reorderdifference.md) — The difference that a reordering operation produces. _(beta)_
