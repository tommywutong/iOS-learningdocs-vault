---
title: 'draggable(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowcontent/draggable(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowcontent/draggable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowcontent/draggable%28_%3A%29.json'
content_hash: 'sha256:b5a7e57a051143ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowContent](../tablerowcontent.md)

# draggable(_:)

<sub>Instance Method</sub>

Activates this row as the source of a drag and drop operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some TableRowContent<Self.TableRowValue> where T : Transferable

```

## Parameters

- `payload` — A closure that returns a single instance or a value conforming to [Transferable](../../coretransferable/transferable.md) that represents the draggable data from this view.

## Return Value

A row that activates this row as the source of a drag and drop operation.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this row.

## See Also

### Managing interaction

- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [onHover(perform:)](<onhover(perform_).md>) — Adds an action to perform when the pointer moves onto or away from the entire row.
- [itemProvider(_:)](<itemprovider(__).md>) — Provides a closure that vends the drag representation for a particular data element.
- [ItemProviderTableRowModifier](../itemprovidertablerowmodifier.md) — A table row modifier that associates an item provider with some base row content.
