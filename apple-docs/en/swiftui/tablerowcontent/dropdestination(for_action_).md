---
title: 'dropDestination(for:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowcontent/dropdestination(for:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowcontent/dropdestination(for:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowcontent/dropdestination%28for%3Aaction%3A%29.json'
content_hash: 'sha256:7ac6d06c20e4300b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowContent](../tablerowcontent.md)

# dropDestination(for:action:)

<sub>Instance Method</sub>

Defines the entire row as a destination of a drag and drop operation that handles the dropped content with a closure that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T]) -> Void) -> some TableRowContent<Self.TableRowValue> where T : Transferable

```

## Parameters

- `payloadType` — The expected type of the dropped models.

- `action` — A closure that takes the dropped content and responds with `true` if the drop operation was successful; otherwise, return `false`.

## Return Value

A row that provides a drop destination for a drag operation of the specified type.

## See Also

### Managing interaction

- [draggable(_:)](<draggable(__).md>) — Activates this row as the source of a drag and drop operation.
- [onHover(perform:)](<onhover(perform_).md>) — Adds an action to perform when the pointer moves onto or away from the entire row.
- [itemProvider(_:)](<itemprovider(__).md>) — Provides a closure that vends the drag representation for a particular data element.
- [ItemProviderTableRowModifier](../itemprovidertablerowmodifier.md) — A table row modifier that associates an item provider with some base row content.
