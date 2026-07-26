---
title: DropConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/dropconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropconfiguration.json'
content_hash: 'sha256:7e297dd44794a45e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DropConfiguration

<sub>Structure</sub>

Describes the behavior of the drop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DropConfiguration
```

## Topics

### Initializers

- [init(operation:)](<dropconfiguration/init(operation_).md>) — Creates a configuration value with the operation chosen by the drop destination.
- [init(operation:destination:)](<dropconfiguration/init(operation_destination_).md>) — Creates a drop configuration with the provided operation and reorder destination. _(beta)_

### Instance Properties

- [acceptedItemCount](dropconfiguration/accepteditemcount.md) — Specifies the number of items that the drop side wants to accept.
- [operation](dropconfiguration/operation.md) — The drop operation that the drop chooses to perform.

## See Also

### Configuring drag-and-drop behavior

- [dragConfiguration(_:)](<view/dragconfiguration(__).md>) — Configures a drag session.
- [DragConfiguration](dragconfiguration.md) — The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [dropConfiguration(_:)](<view/dropconfiguration(__).md>) — Configures a drop session.
- [dragContainer(for:in:_:)](<view/dragcontainer(for_in___).md>) — A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainer(for:itemID:in:_:)](<view/dragcontainer(for_itemid_in___).md>) — A container with draggable views.
- [dragContainerSelection(_:containerNamespace:)](<view/dragcontainerselection(__containernamespace_).md>) — Provides multiple item selection support for drag containers.
