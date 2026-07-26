---
title: DropOperation
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropoperation
source_url: 'https://developer.apple.com/documentation/swiftui/dropoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropoperation.json'
content_hash: 'sha256:ff0345eeb590ba3b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DropOperation

<sub>Enumeration</sub>

Operation types that determine how a drag and drop session resolves when the user drops a drag item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum DropOperation
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting operation types

- [DropOperation.cancel](dropoperation/cancel.md) — Cancel the drag operation and transfer no data.
- [DropOperation.copy](dropoperation/copy.md) — Copy the data to the modified view.
- [DropOperation.forbidden](dropoperation/forbidden.md) — The drop activity is not allowed at this time or location.
- [DropOperation.move](dropoperation/move.md) — Move the data represented by the drag items instead of copying it.

### Structures

- [Set](dropoperation/set.md) — A set of drop operations, corresponding to matching cases in `DropOperation`.

### Enumeration Cases

- [DropOperation.alias](dropoperation/alias.md)
- [DropOperation.delete](dropoperation/delete.md) — Delete the data. The item was dragged to Trash or to another destination that semantically represents deletion.

## See Also

### Moving items using item providers

- [itemProvider(_:)](<view/itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](<view/ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](<view/ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](dropdelegate.md) — An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](dropproposal.md) — The behavior of a drop.
- [DropInfo](dropinfo.md) — The current state of a drop.
