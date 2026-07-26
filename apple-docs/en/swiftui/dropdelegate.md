---
title: DropDelegate
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropdelegate
source_url: 'https://developer.apple.com/documentation/swiftui/dropdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropdelegate.json'
content_hash: 'sha256:4aec673270a44b87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DropDelegate

<sub>Protocol</sub>

An interface that you implement to interact with a drop operation in a view modified to accept drops.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol DropDelegate
```

## Overview

The [DropDelegate](dropdelegate.md) protocol provides a comprehensive and flexible way to interact with a drop operation. Specify a drop delegate when you modify a view to accept drops with the [onDrop(of:delegate:)](<view/ondrop(of_delegate_).md>) method.

Alternatively, for simple drop cases that don’t require the full functionality of a drop delegate, you can modify a view to accept drops using the [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) method. This method handles the drop using a closure you provide as part of the modifier.

## Topics

### Receiving drop information

- [dropEntered(info:)](<dropdelegate/dropentered(info_).md>) — Tells the delegate a validated drop has entered the modified view.
- [dropExited(info:)](<dropdelegate/dropexited(info_).md>) — Tells the delegate a validated drop operation has exited the modified view.
- [dropUpdated(info:)](<dropdelegate/dropupdated(info_).md>) — Tells the delegate that a validated drop moved inside the modified view.
- [validateDrop(info:)](<dropdelegate/validatedrop(info_).md>) — Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.
- [performDrop(info:)](<dropdelegate/performdrop(info_).md>) — Tells the delegate it can request the item provider data from the given information.

## See Also

### Moving items using item providers

- [itemProvider(_:)](<view/itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](<view/ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](<view/ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropProposal](dropproposal.md) — The behavior of a drop.
- [DropOperation](dropoperation.md) — Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](dropinfo.md) — The current state of a drop.
