---
title: 'onDragSessionUpdated(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 26.0+, visionOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ondragsessionupdated(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ondragsessionupdated(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ondragsessionupdated%28_%3A%29.json'
content_hash: 'sha256:e4310664532392b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onDragSessionUpdated(_:)

<sub>Instance Method</sub>

Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or anther drag modifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func onDragSessionUpdated(_ onUpdate: @escaping (DragSession) -> Void) -> some View

```

## Discussion

Below is an example of a view that displays a book and supports dragging to copy, move, and delete. If the session ends with moving or deleting the item, in the `onUpdate` closure, the view lets the model layer know that the book should be deleted from the source.

```swift
struct DraggableBookView: View {
    var id: UUID

    var body: some View {
        BookView()
            .draggable(Book(id: id))
            .dragConfiguration(
                DragConfiguration(
                    operationsWithinApp: .init(allowMove: true, allowDelete: true),
                    operationsOutsideApp: .init(allowMove: true, allowDelete: true)
                ))
            .onDragSessionUpdated { session in
                switch session.phase {
                case .ended(at: _, with: let operation):
                    if operation == .move || operation == .delete {
                        if let id = session.draggedItemIDs(type: UUID.self).first {
                            removeBook(id: id)
                        }
                    }
                default:
                    break
                }
            }
    }
}

func removeBook(id: UUID) { }
```

The `onUpdate` closure is called when the closest drag session in the child view hierarchy becomes active.

## See Also

### Drag and drop

- [dragConfiguration(_:)](<dragconfiguration(__).md>) — Configures a drag session.
- [dragContainer(for:in:_:)](<dragcontainer(for_in___).md>) — A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainer(for:itemID:in:_:)](<dragcontainer(for_itemid_in___).md>) — A container with draggable views.
- [dragContainerSelection(_:containerNamespace:)](<dragcontainerselection(__containernamespace_).md>) — Provides multiple item selection support for drag containers.
- [dragPreviewsFormation(_:)](<dragpreviewsformation(__).md>) — Describes the way dragged previews are visually composed.
- [draggable(_:)](<draggable(__).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:preview:)](<draggable(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:containerNamespace:_:)](<draggable(__containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:containerNamespace:_:)](<draggable(__id_containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:item:containerNamespace:)](<draggable(__id_item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:item:containerNamespace:)](<draggable(__item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(containerItemID:containerNamespace:)](<draggable(containeritemid_containernamespace_).md>) — Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
- [dropConfiguration(_:)](<dropconfiguration(__).md>) — Configures a drop session.
- [dropDestination(for:isEnabled:action:)](<dropdestination(for_isenabled_action_).md>) — Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [dropPreviewsFormation(_:)](<droppreviewsformation(__).md>) — Describes the way previews for a drop are composed.
