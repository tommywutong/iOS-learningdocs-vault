---
title: DropProposal
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropproposal
source_url: 'https://developer.apple.com/documentation/swiftui/dropproposal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropproposal.json'
content_hash: 'sha256:35e8b55996349e35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DropProposal

<sub>Structure</sub>

The behavior of a drop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DropProposal
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a drop proposal

- [init(operation:)](<dropproposal/init(operation_).md>)
- [operation](dropproposal/operation.md) — The drop operation that the drop proposes to perform.

### Initializers

- [init(withinApplication:outsideApplication:)](<dropproposal/init(withinapplication_outsideapplication_).md>)

### Instance Properties

- [operationOutsideApplication](dropproposal/operationoutsideapplication.md) — The drop operation for drops outside the source application.

## See Also

### Moving items using item providers

- [itemProvider(_:)](<view/itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](<view/ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](<view/ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](dropdelegate.md) — An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropOperation](dropoperation.md) — Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](dropinfo.md) — The current state of a drop.
