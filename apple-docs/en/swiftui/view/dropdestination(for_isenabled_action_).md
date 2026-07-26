---
title: 'dropDestination(for:isEnabled:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dropdestination(for:isenabled:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dropdestination(for:isenabled:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dropdestination%28for%3Aisenabled%3Aaction%3A%29.json'
content_hash: 'sha256:e4dbf404c5c0df61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dropDestination(for:isEnabled:action:)

<sub>Instance Method</sub>

Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func dropDestination<T>(for type: T.Type = T.self, isEnabled: Bool = true, action: @escaping ([T], DropSession) -> Void) -> some View where T : Transferable

```

## Parameters

- `type` — The expected type of the dropped models.

- `isEnabled` — The Boolean value indicating if the view accepts drop interactions.

- `action` — A closure that takes the dropped content and responds appropriately. The first parameter to `action` contains the dropped items. The second parameter contains the drop session description.

## Return Value

A view that provides a drop destination for a drop operation of the specified type.

## Discussion

The dropped content can be provided as binary data, file URLs, or file promises.

The drop destination is the same size and position as this view.

```swift
@State private var isDropTargeted = false
@Binding var isDropEnabled: Bool

var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .dropDestination(
            for: String.self, isEnabled: isDropEnabled
        ) { receivedTitles, session in
            animateDrop(at: session.location)
            process(titles: receivedTitles)
        }
}

func process(titles: [String]) { ... }
func animateDrop(at: CGPoint) { ... }
```

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
- [dropPreviewsFormation(_:)](<droppreviewsformation(__).md>) — Describes the way previews for a drop are composed.
- [itemProvider(_:)](<itemprovider(__).md>) — Provides a closure that vends the drag representation to be used for a particular data element.
