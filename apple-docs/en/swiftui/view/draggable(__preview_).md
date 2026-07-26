---
title: 'draggable(_:preview:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/draggable(_:preview:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/draggable(_:preview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/draggable%28_%3Apreview%3A%29.json'
content_hash: 'sha256:a51fd7514fd65e5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# draggable(_:preview:)

<sub>Instance Method</sub>

Activates this view as the source of a drag and drop operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func draggable<V, T>(_ payload: @autoclosure @escaping () -> T, @ContentBuilder preview: () -> V) -> some View where V : View, T : Transferable

```

## Parameters

- `payload` — A closure that returns a single class instance or a value conforming to `Transferable` that represents the draggable data from this view.

- `preview` — A [View](../view.md) to use as the source for the dragging preview, once the drag operation has begun. The preview is centered over the source view.

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

Applying the `draggable(_:preview:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of `preview` is generated and used as the preview image.

```swift
var title: String
var body: some View {
Color.pink
    .frame(width: 400, height: 400)
    .draggable(title) {
         Text("Drop me")
     }
}
```

To customize the lift preview, shown while the system transitions to show your custom `preview`, apply a [contentShape(_:_:eoFill:)](<contentshape(____eofill_).md>) with a [dragPreview](../contentshapekinds/dragpreview.md) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

## See Also

### Moving transferable items

- [draggable(_:)](<draggable(__).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:containerNamespace:_:)](<draggable(__containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:containerNamespace:_:)](<draggable(__id_containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:item:containerNamespace:)](<draggable(__id_item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:item:containerNamespace:)](<draggable(__item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(containerItemID:containerNamespace:)](<draggable(containeritemid_containernamespace_).md>) — Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
