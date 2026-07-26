---
title: Making a card game with drag, drop, and reordering in SwiftUI
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 27.0+ beta, Xcode 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/making-a-card-game-with-drag-drop-and-reordering-in-swiftui
source_url: 'https://developer.apple.com/documentation/swiftui/making-a-card-game-with-drag-drop-and-reordering-in-swiftui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/making-a-card-game-with-drag-drop-and-reordering-in-swiftui.json'
content_hash: 'sha256:c47f59abc3669d4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Drag and drop](drag-and-drop.md)

# Making a card game with drag, drop, and reordering in SwiftUI

<sub>Sample Code</sub>

Move cards between positions in a card game using drag, drop, and reordering modifiers.

## Overview

> [!note] Note
> This sample code project is associated with WWDC26 session 271: [Code-along: Build powerful drag and drop in SwiftUI](http://developer.apple.com/videos/play/wwdc2026/271/).

## See Also

### Reordering items

- [reorderable()](<dynamicviewcontent/reorderable().md>) — Enables reordering of views from this content inside the scope of a reorderable container modifier. _(beta)_
- [reorderable(collectionID:)](<dynamicviewcontent/reorderable(collectionid_).md>) — Enables reordering views from this content within and between sections in the scope of a reorderable container modifier. _(beta)_
- [ReorderableSingleCollectionIdentifier](reorderablesinglecollectionidentifier.md) — An opaque, empty type used to identify reorderable containers and modifiers with only a single collection. _(beta)_
- [reorderContainer(for:isEnabled:move:)](<view/reordercontainer(for_isenabled_move_).md>) — Defines a container of reorderable views. _(beta)_
- [reorderContainer(for:in:isEnabled:move:)](<view/reordercontainer(for_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type you specify to identify sections. _(beta)_
- [reorderContainer(for:itemID:isEnabled:move:)](<view/reordercontainer(for_itemid_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you specify to identify items. _(beta)_
- [reorderContainer(for:itemID:in:isEnabled:move:)](<view/reordercontainer(for_itemid_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections. _(beta)_
- [reorderDestination(for:in:)](<dropsession/reorderdestination(for_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [reorderDestination(for:itemID:in:)](<dropsession/reorderdestination(for_itemid_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [ReorderDifference](reorderdifference.md) — The difference that a reordering operation produces. _(beta)_

## Download

- [MakingACardGameWithDragDropAndReorderingInSwiftUI.zip](https://docs-assets.developer.apple.com/published/97ac6f9aaef0/MakingACardGameWithDragDropAndReorderingInSwiftUI.zip)
