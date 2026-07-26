---
title: 'onHover(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowcontent/onhover(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowcontent/onhover(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowcontent/onhover%28perform%3A%29.json'
content_hash: 'sha256:449ac64e6061d0bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowContent](../tablerowcontent.md)

# onHover(perform:)

<sub>Instance Method</sub>

Adds an action to perform when the pointer moves onto or away from the entire row.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func onHover(perform action: @escaping (Bool) -> Void) -> some TableRowContent<Self.TableRowValue>

```

## See Also

### Managing interaction

- [draggable(_:)](<draggable(__).md>) — Activates this row as the source of a drag and drop operation.
- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [itemProvider(_:)](<itemprovider(__).md>) — Provides a closure that vends the drag representation for a particular data element.
- [ItemProviderTableRowModifier](../itemprovidertablerowmodifier.md) — A table row modifier that associates an item provider with some base row content.
