---
title: 'onDrop(of:delegate:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ondrop(of:delegate:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ondrop(of:delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ondrop%28of%3Adelegate%3A%29.json'
content_hash: 'sha256:643452159c9f6607'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onDrop(of:delegate:)

<sub>Instance Method</sub>

Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func onDrop(of supportedContentTypes: [UTType], delegate: any DropDelegate) -> some View

```

## Parameters

- `supportedContentTypes` — The uniform type identifiers that describe the types of content this view can accept through drag and drop. If the drag and drop operation doesn’t contain any of the supported types, then this drop destination doesn’t activate and `isTargeted` doesn’t update.

- `delegate` — A type that conforms to the [DropDelegate](../dropdelegate.md) protocol. You have comprehensive control over drop behavior when you use a delegate.

## Return Value

A view that provides a drop destination for a drag operation of the specified types.

## Discussion

To use `Transferable` types directly and access a richer feature set — including support for [DropSession](../dropsession.md) — use [dropDestination(for:isEnabled:action:)](<dropdestination(for_isenabled_action_).md>) instead.

## See Also

### Moving items using item providers

- [itemProvider(_:)](<itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](<ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](<ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](<ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [DropDelegate](../dropdelegate.md) — An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](../dropproposal.md) — The behavior of a drop.
- [DropOperation](../dropoperation.md) — Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](../dropinfo.md) — The current state of a drop.
