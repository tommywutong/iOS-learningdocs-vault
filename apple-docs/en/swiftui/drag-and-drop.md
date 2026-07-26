---
title: Drag and drop
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/drag-and-drop
source_url: 'https://developer.apple.com/documentation/swiftui/drag-and-drop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/drag-and-drop.json'
content_hash: 'sha256:980093a79ceae346'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Drag and drop

<sub>API Collection</sub>

Enable people to move or duplicate items by dragging them from one location to another.

## Overview

Drag and drop offers people a convenient way to move content from one part of your app to another, from one app to another, or to reorder content using an intuitive dragging gesture. Support this feature in your app by adding view modifiers to potential source and destination views within your app’s interface.

![](../../../attachments/389cb904528e698574c83a1ccfbb85d9/drag-and-drop-hero@2x.png)

In your modifiers, provide or accept types that conform to the [Transferable](../coretransferable/transferable.md) protocol, or that conform to [NSItemProviderReading](../foundation/nsitemproviderreading.md) and/or [NSItemProviderWriting](../foundation/nsitemproviderwriting.md). In Swift, prefer using transferable items.

For design guidance, see [Drag and drop](../design/human-interface-guidelines/drag-and-drop.md) in the Human Interface Guidelines.

## Topics

### Essentials

- [Adopting drag and drop using SwiftUI](adopting-drag-and-drop-using-swiftui.md) — Enable drag-and-drop interactions in lists, tables and custom views.
- [Making a view into a drag source](making-a-view-into-a-drag-source.md) — Adopt draggable API to provide items for drag-and-drop operations.
- [Reordering items in lists, stacks, grids, and custom layouts](reordering-items-in-lists-stacks-grids-and-custom-layouts.md) — Add drag-to-reorder interactions to SwiftUI layouts using reordering modifiers.

### Configuring drag-and-drop behavior

- [dragConfiguration(_:)](<view/dragconfiguration(__).md>) — Configures a drag session.
- [DragConfiguration](dragconfiguration.md) — The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [dropConfiguration(_:)](<view/dropconfiguration(__).md>) — Configures a drop session.
- [DropConfiguration](dropconfiguration.md) — Describes the behavior of the drop.
- [dragContainer(for:in:_:)](<view/dragcontainer(for_in___).md>) — A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainer(for:itemID:in:_:)](<view/dragcontainer(for_itemid_in___).md>) — A container with draggable views.
- [dragContainerSelection(_:containerNamespace:)](<view/dragcontainerselection(__containernamespace_).md>) — Provides multiple item selection support for drag containers.

### Moving items

- [DragSession](dragsession.md) — Describes the ongoing dragging session.
- [DropSession](dropsession.md)

### Moving transferable items

- [draggable(_:)](<view/draggable(__).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:preview:)](<view/draggable(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:containerNamespace:_:)](<view/draggable(__containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:containerNamespace:_:)](<view/draggable(__id_containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:item:containerNamespace:)](<view/draggable(__id_item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:item:containerNamespace:)](<view/draggable(__item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(containerItemID:containerNamespace:)](<view/draggable(containeritemid_containernamespace_).md>) — Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.

### Moving items using item providers

- [itemProvider(_:)](<view/itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](<view/ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](<view/ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](dropdelegate.md) — An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](dropproposal.md) — The behavior of a drop.
- [DropOperation](dropoperation.md) — Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](dropinfo.md) — The current state of a drop.

### Reordering items

- [Making a card game with drag, drop, and reordering in SwiftUI](making-a-card-game-with-drag-drop-and-reordering-in-swiftui.md) — Move cards between positions in a card game using drag, drop, and reordering modifiers.
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

### Describing preview formations

- [dragPreviewsFormation(_:)](<view/dragpreviewsformation(__).md>) — Describes the way dragged previews are visually composed.
- [dropPreviewsFormation(_:)](<view/droppreviewsformation(__).md>) — Describes the way previews for a drop are composed.
- [DragDropPreviewsFormation](dragdroppreviewsformation.md) — On macOS, describes the way the dragged previews are visually composed. Both drag sources and drop destination can specify their desired preview formation.

### Configuring spring loading

- [springLoadingBehavior(_:)](<view/springloadingbehavior(__).md>) — Sets the spring loading behavior this view.
- [springLoadingBehavior](environmentvalues/springloadingbehavior.md) — The behavior of spring loaded interactions for the views associated with this environment.
- [SpringLoadingBehavior](springloadingbehavior.md) — The options for controlling the spring loading behavior of views.

## See Also

### Event handling

- [Gestures](gestures.md) — Define interactions from taps, clicks, and swipes to fine-grained gestures.
- [Input events](input-events.md) — Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Clipboard](clipboard.md) — Enable people to move or duplicate items by issuing Copy and Paste commands.
- [Focus](focus.md) — Identify and control which visible object responds to user interaction.
- [System events](system-events.md) — React to system events, like opening a URL.
