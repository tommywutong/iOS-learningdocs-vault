---
title: 'onDrop(of:isTargeted:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ondrop(of:istargeted:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ondrop(of:istargeted:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ondrop%28of%3Aistargeted%3Aperform%3A%29.json'
content_hash: 'sha256:56cdf29052d7dde5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onDrop(of:isTargeted:perform:)

<sub>Instance Method</sub>

Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func onDrop(of supportedContentTypes: [UTType], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider]) -> Bool) -> some View

```

## Parameters

- `supportedContentTypes` — The uniform type identifiers that describe the types of content this view can accept through drag and drop. If the drag-and-drop operation doesn’t contain any of the supported types, then this drop destination doesn’t activate and `isTargeted` doesn’t update.

- `isTargeted` — A binding that updates when a drag and drop operation enters or exits the drop target area. The binding’s value is `true` when the cursor is inside the area, and `false` when the cursor is outside.

- `action` — A closure that takes the dropped content and responds appropriately. The parameter to `action` contains the dropped items, with types specified by `supportedContentTypes`. Return `true` if the drop operation was successful; otherwise, return `false`.

## Return Value

A view that provides a drop destination for a drag operation of the specified types.

## Discussion

The drop destination is the same size and position as this view.

Make sure to start loading the contents of `NSItemProvider` instances within the scope of the `action` closure. Do not perform loading asynchronously on a different actor. Loading the contents may finish later, but it must start here. For security reasons, the drop receiver can access the dropped payload only before this closure returns.

To use `Transferable` types directly and access a richer feature set — including support for [DropSession](../dropsession.md) — use [dropDestination(for:isEnabled:action:)](<dropdestination(for_isenabled_action_).md>) instead.

## See Also

### Moving items using item providers

- [itemProvider(_:)](<itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](<ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](<ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:delegate:)](<ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](../dropdelegate.md) — An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](../dropproposal.md) — The behavior of a drop.
- [DropOperation](../dropoperation.md) — Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](../dropinfo.md) — The current state of a drop.
