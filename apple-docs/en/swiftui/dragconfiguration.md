---
title: DragConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dragconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/dragconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dragconfiguration.json'
content_hash: 'sha256:ed5025e4f0144f9b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DragConfiguration

<sub>Structure</sub>

The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DragConfiguration
```

## Overview

Pass a `DragConfiguration` to the [dragConfiguration(_:)](<view/dragconfiguration(__).md>) modifier to declare which operations — copy, move, or delete — a view supports when it is dragged.

### Opting in to move

By default, only copy is allowed. To support drag-to-move, where the source item is removed after a successful drop, initialize with `allowMove: true`:

```swift
.dragConfiguration(DragConfiguration(allowMove: true))
```

On macOS, users can override the proposed operation during a drag by holding modifier keys:

- **⌥ (Option)** proposes copy.
- **⌘ (Command)** proposes move.
- **⌥ + ⌘** proposes alias.

Modifier keys only take effect when the source supports the corresponding operation. For example, holding ⌘ has no effect unless `allowMove` is `true`.

### Responding to the performed operation

`DragConfiguration` communicates _suggested_ operations to drop destinations, but each destination chooses which operation to perform. To detect which operation was ultimately performed — for example, to remove the source item after a successful move — observe the drag session using [onDragSessionUpdated(_:)](<view/ondragsessionupdated(__).md>):

```swift
.dragConfiguration(DragConfiguration(allowMove: true))
.onDragSessionUpdated { session in
    if session.phase == .ended(.move) {
        removeItem()
    }
}
```

> [!info] See Also
> [dragConfiguration(_:)](<view/dragconfiguration(__).md>), [onDragSessionUpdated(_:)](<view/ondragsessionupdated(__).md>), [suggestedOperations](dropsession/suggestedoperations.md)

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Escapable](../swift/escapable.md)

## Topics

### Structures

- [OperationsOutsideApp](dragconfiguration/operationsoutsideapp-swift.struct.md) — Describes the suggested drag operations to other applications.
- [OperationsWithinApp](dragconfiguration/operationswithinapp-swift.struct.md) — Describes the drag operations suggested to destinations within the app.

### Initializers

- [init(allowMove:)](<dragconfiguration/init(allowmove_).md>) — Creates a drag configuration that can support drag-to-move in addition to drag-to-copy.
- [init(allowMove:allowDelete:)](<dragconfiguration/init(allowmove_allowdelete_).md>) — Creates a drag configuration that can support drag-to-move and drag-to-delete in addition to drag-to-copy.
- [init(operationsWithinApp:operationsOutsideApp:)](<dragconfiguration/init(operationswithinapp_operationsoutsideapp_).md>) — Creates a default drag configuration with operation `.copy` support for drags within the application and to other applications.

### Instance Properties

- [operationsOutsideApp](dragconfiguration/operationsoutsideapp-swift.property.md) — The operations suggested by the drag source for drags to other applications.
- [operationsWithinApp](dragconfiguration/operationswithinapp-swift.property.md) — The operations suggested by the drag source for drags within the application.

## See Also

### Configuring drag-and-drop behavior

- [dragConfiguration(_:)](<view/dragconfiguration(__).md>) — Configures a drag session.
- [dropConfiguration(_:)](<view/dropconfiguration(__).md>) — Configures a drop session.
- [DropConfiguration](dropconfiguration.md) — Describes the behavior of the drop.
- [dragContainer(for:in:_:)](<view/dragcontainer(for_in___).md>) — A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainer(for:itemID:in:_:)](<view/dragcontainer(for_itemid_in___).md>) — A container with draggable views.
- [dragContainerSelection(_:containerNamespace:)](<view/dragcontainerselection(__containernamespace_).md>) — Provides multiple item selection support for drag containers.
