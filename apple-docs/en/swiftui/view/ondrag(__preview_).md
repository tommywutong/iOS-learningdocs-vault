---
title: 'onDrag(_:preview:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ondrag(_:preview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ondrag(_:preview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ondrag%28_%3Apreview%3A%29.json'
content_hash: 'sha256:0705ced87a971542'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onDrag(_:preview:)

<sub>Instance Method</sub>

Activates this view as the source of a drag and drop operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func onDrag<V>(_ data: @escaping () -> NSItemProvider, @ContentBuilder preview: () -> V) -> some View where V : View

```

## Parameters

- `data` — A closure that returns a single [NSItemProvider](../../foundation/nsitemprovider.md) that represents the draggable data from this view.

- `preview` — A [View](../view.md) to use as the source for the dragging preview, once the drag operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag-and- drop operation, beginning with user gesture input.

## Discussion

Applying the `onDrag(_:preview:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of `preview` is generated and used as the preview image.

To customize the lift preview, shown while the system transitions to show your custom `preview`, apply a [contentShape(_:_:eoFill:)](<contentshape(____eofill_).md>) with a [dragPreview](../contentshapekinds/dragpreview.md) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

To use `Transferable` types directly and access a richer feature set — including multi-item drag via [dragContainer(for:in:_:)](<dragcontainer(for_in___).md>) — use [draggable(_:)](<draggable(__).md>) instead.

## See Also

### Moving items using item providers

- [itemProvider(_:)](<itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
- [onDrag(_:)](<ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](<ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](<ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](../dropdelegate.md) — An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](../dropproposal.md) — The behavior of a drop.
- [DropOperation](../dropoperation.md) — Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](../dropinfo.md) — The current state of a drop.
