---
title: 'onDrag(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ondrag(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ondrag(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ondrag%28_%3A%29.json'
content_hash: 'sha256:cac2eef0c3ff2b57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onDrag(_:)

<sub>Instance Method</sub>

Activates this view as the source of a drag and drop operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func onDrag(_ data: @escaping () -> NSItemProvider) -> some View

```

## Parameters

- `data` — A closure that returns a single [NSItemProvider](../../foundation/nsitemprovider.md) that represents the draggable data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

Applying the `onDrag(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a [contentShape(_:_:eoFill:)](<contentshape(____eofill_).md>) with a [dragPreview](../contentshapekinds/dragpreview.md) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

If you want to show a different preview, you can use [onDrag(_:preview:)](<ondrag(__preview_).md>).

To use `Transferable` types directly and access a richer feature set — including multi-item drag via [dragContainer(for:in:_:)](<dragcontainer(for_in___).md>) — use [draggable(_:)](<draggable(__).md>) instead.

## See Also

### Moving items using item providers

- [itemProvider(_:)](<itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:preview:)](<ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](<ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](<ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](../dropdelegate.md) — An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](../dropproposal.md) — The behavior of a drop.
- [DropOperation](../dropoperation.md) — Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](../dropinfo.md) — The current state of a drop.
