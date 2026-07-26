---
title: 'draggable(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/draggable(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/draggable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/draggable%28_%3A%29.json'
content_hash: 'sha256:33e6c3620c69078b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# draggable(_:)

<sub>Instance Method</sub>

Activates this view as the source of a drag and drop operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some View where T : Transferable

```

## Parameters

- `payload` — A closure that returns a single instance or a value conforming to [Transferable](../../coretransferable/transferable.md) that represents the draggable data from this view.

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a [contentShape(_:_:eoFill:)](<contentshape(____eofill_).md>) with a [dragPreview](../contentshapekinds/dragpreview.md) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

## See Also

### Moving transferable items

- [draggable(_:preview:)](<draggable(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:containerNamespace:_:)](<draggable(__containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:containerNamespace:_:)](<draggable(__id_containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:item:containerNamespace:)](<draggable(__id_item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:item:containerNamespace:)](<draggable(__item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(containerItemID:containerNamespace:)](<draggable(containeritemid_containernamespace_).md>) — Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
