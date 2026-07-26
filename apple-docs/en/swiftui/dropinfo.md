---
title: DropInfo
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropinfo
source_url: 'https://developer.apple.com/documentation/swiftui/dropinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropinfo.json'
content_hash: 'sha256:76127a3520c79cb3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DropInfo

<sub>Structure</sub>

The current state of a drop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DropInfo
```

## Topics

### Getting the drop location

- [location](dropinfo/location.md) — The location of the drag in the coordinate space of the drop view.

### Checking for items

- [hasItemsConforming(to:)](<dropinfo/hasitemsconforming(to_)-47irh.md>) — Indicates whether at least one item conforms to at least one of the specified uniform type identifiers.
- [itemProviders(for:)](<dropinfo/itemproviders(for_)-93409.md>) — Finds item providers that conform to at least one of the specified uniform type identifiers.

### Deprecated symbols

- [hasItemsConforming(to:)](<dropinfo/hasitemsconforming(to_)-4qeez.md>) — Returns whether at least one item conforms to at least one of the specified uniform type identifiers. _(deprecated)_
- [itemProviders(for:)](<dropinfo/itemproviders(for_)-b6fo.md>) — Returns an array of items that each conform to at least one of the specified uniform type identifiers. _(deprecated)_

### Instance Methods

- [hasItemsConforming(to:)](<dropinfo/hasitemsconforming(to_).md>) — Indicates whether at least one item conforms to at least one of the specified uniform type identifiers.
- [itemProviders(for:)](<dropinfo/itemproviders(for_).md>) — Finds item providers that conform to at least one of the specified uniform type identifiers.

## See Also

### Moving items using item providers

- [itemProvider(_:)](<view/itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](<view/ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](<view/ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](dropdelegate.md) — An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](dropproposal.md) — The behavior of a drop.
- [DropOperation](dropoperation.md) — Operation types that determine how a drag and drop session resolves when the user drops a drag item.
