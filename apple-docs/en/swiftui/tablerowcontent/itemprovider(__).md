---
title: 'itemProvider(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowcontent/itemprovider(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowcontent/itemprovider(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowcontent/itemprovider%28_%3A%29.json'
content_hash: 'sha256:789ddd510752c80e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowContent](../tablerowcontent.md)

# itemProvider(_:)

<sub>Instance Method</sub>

Provides a closure that vends the drag representation for a particular data element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func itemProvider(_ action: (() -> NSItemProvider?)?) -> ModifiedContent<Self, ItemProviderTableRowModifier>
```

## See Also

### Managing interaction

- [draggable(_:)](<draggable(__).md>) — Activates this row as the source of a drag and drop operation.
- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [onHover(perform:)](<onhover(perform_).md>) — Adds an action to perform when the pointer moves onto or away from the entire row.
- [ItemProviderTableRowModifier](../itemprovidertablerowmodifier.md) — A table row modifier that associates an item provider with some base row content.
