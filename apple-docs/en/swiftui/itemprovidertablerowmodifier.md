---
title: ItemProviderTableRowModifier
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/itemprovidertablerowmodifier
source_url: 'https://developer.apple.com/documentation/swiftui/itemprovidertablerowmodifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/itemprovidertablerowmodifier.json'
content_hash: 'sha256:8dc597fae2706339'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ItemProviderTableRowModifier

<sub>Structure</sub>

A table row modifier that associates an item provider with some base row content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct ItemProviderTableRowModifier
```

## Topics

### Instance Properties

- [body](itemprovidertablerowmodifier/body-swift.property.md)

### Type Aliases

- [Body](itemprovidertablerowmodifier/body-swift.typealias.md)

## See Also

### Managing interaction

- [draggable(_:)](<tablerowcontent/draggable(__).md>) — Activates this row as the source of a drag and drop operation.
- [dropDestination(for:action:)](<tablerowcontent/dropdestination(for_action_).md>) — Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [onHover(perform:)](<tablerowcontent/onhover(perform_).md>) — Adds an action to perform when the pointer moves onto or away from the entire row.
- [itemProvider(_:)](<tablerowcontent/itemprovider(__).md>) — Provides a closure that vends the drag representation for a particular data element.
