---
title: 'init(operation:destination:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/dropconfiguration/init(operation:destination:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dropconfiguration/init(operation:destination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropconfiguration/init%28operation%3Adestination%3A%29.json'
content_hash: 'sha256:07636641cf373941'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropConfiguration](../dropconfiguration.md)

# init(operation:destination:)

<sub>Initializer</sub>

Creates a drop configuration with the provided operation and reorder destination.

<sub>macOS</sub>

```swift
init<ItemID, CollectionID>(operation: DropOperation, destination: ReorderDifference<ItemID, CollectionID>.Destination) where ItemID : Hashable, ItemID : Sendable, CollectionID : Hashable, CollectionID : Sendable
```

## Discussion

Use this initializer when you want to decide where the destination value of the current reordering session should be. The value that you pass to this initializer will be the value used for this update.

If you don’t want to update the destination value, or your [dropDestination(for:isEnabled:action:)](<../view/dropdestination(for_isenabled_action_).md>) is not configured with a `View/reorderContainer(for:in:move:)`, use the initializer variant that takes only a `DropOperation`.

- operation: The drop operation that the drop destination chooses to perform on the drop.
- destination: The destination value for the reordering operation.
