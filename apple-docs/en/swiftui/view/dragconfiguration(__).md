---
title: 'dragConfiguration(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dragconfiguration(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dragconfiguration(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dragconfiguration%28_%3A%29.json'
content_hash: 'sha256:9748be9de6fe8076'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dragConfiguration(_:)

<sub>Instance Method</sub>

Configures a drag session.

<sub>macOS</sub>

```swift
nonisolated func dragConfiguration(_ configuration: DragConfiguration) -> some View

```

## Parameters

- `configuration` — A value that describes the configuration of a drag session.

## Return Value

A view that configures a drag session in a way, described by the `configuration` parameter.

## Discussion

Below is a simplified example of a view that supports copy, move and delete operations for drag.

### Drag to delete into trash bin

If a view wants to support drag-to-delete into the trash bin or another location that has similar semantics, it should specify the support for this operation in a drag configuration:

```swift
    @State private var photos: [Photo] = []
    @State private var selectedPhotos: [Photo.ID] = []

    var body: some View {
        ScrollView {
            LazyVGrid(columns: gridColumns) {
                ForEach(photos) { photo in
                    PhotoView(photo: photo)
                        .draggable(containerItemID: photo.id)
                }
            }
        }
        .dragContainer(for: Photo.self) { draggedIDs in
            photos(ids: draggedIDs)
        }
        .dragContainerSelection(selectedPhotos)
        .dragConfiguration(DragConfiguration(allowMove: false, allowDelete: true))
        .onDragSessionUpdated { session in
            if session.phase == .ended(.delete) {
                let ids = session.draggedItemIDs(for: Photo.ID.self)
                removeAndTrash(ids)
            }
        }
        .dragPreviewsFormation(.stack)
    }

    func removeAndTrash(_ ids: [Photo.ID]) {
        ids.forEach { id
            if let idx = photos.firstIndex(where: { $0.id == id }) {
                let photo = photos[idx]
                photos.remove(at: idx)
                try? FileManager.default.trashItem(
                    at: photo.fileURL, resultingItemURL: nil
                )
            }
        }
    }
}
```

Note, that any drag supports copy operation by default. In the snippet above, the view supports both copy and delete operations.

## See Also

### Configuring drag-and-drop behavior

- [DragConfiguration](../dragconfiguration.md) — The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [dropConfiguration(_:)](<dropconfiguration(__).md>) — Configures a drop session.
- [DropConfiguration](../dropconfiguration.md) — Describes the behavior of the drop.
- [dragContainer(for:in:_:)](<dragcontainer(for_in___).md>) — A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainer(for:itemID:in:_:)](<dragcontainer(for_itemid_in___).md>) — A container with draggable views.
- [dragContainerSelection(_:containerNamespace:)](<dragcontainerselection(__containernamespace_).md>) — Provides multiple item selection support for drag containers.
