---
title: 'draggable(_:item:containerNamespace:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 26.0+, visionOS 27.0+ beta]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/draggable(_:item:containernamespace:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/draggable(_:item:containernamespace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/draggable%28_%3Aitem%3Acontainernamespace%3A%29.json'
content_hash: 'sha256:cea982cc6f8ceecf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# draggable(_:item:containerNamespace:)

<sub>Instance Method</sub>

Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func draggable<Item>(_ itemType: Item.Type = Item.self, item: @autoclosure @escaping () -> Item?, containerNamespace: Namespace.ID? = nil) -> some View where Item : Transferable, Item : Identifiable, Item.ID : Sendable

```

## Parameters

- `itemType` — A type of the dragged item.

- `item` — A closure that returns a single instance or a value conforming to [Transferable](../../coretransferable/transferable.md) that represents the draggable data from this view.

- `containerNamespace` — A namespace of the associated drag container.

## Return Value

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

Applying the `draggable(_:_:containerNamespace:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

If the view is enclosed in a `dragContainer(for:in:_)`, the view becomes its draggable element, and the item’s identifier is used as drag payload identifier.

```swift
var fruits: [Fruit]
var selectedFruits: [Fruit.ID]

var body: some View {
    ScrollView {
        VStack {
            ForEach(fruits) { fruit in
                FruitView(fruit)
                    .draggable(fruit)
            }
        }
    }
    .dragContainer(for: Fruit.self) { identifiers in
        fruits(with: identifiers)
    }
}

func fruits(with: [Fruit.ID]) -> [Fruit] { ... }
struct Fruit: Identifiable, Transferable { ... }
```

## See Also

### Moving transferable items

- [draggable(_:)](<draggable(__).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:preview:)](<draggable(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [draggable(_:containerNamespace:_:)](<draggable(__containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional identifiable payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:containerNamespace:_:)](<draggable(__id_containernamespace___).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(_:id:item:containerNamespace:)](<draggable(__id_item_containernamespace_).md>) — Activates this view as the source of a drag and drop operation, allowing to provide optional payload and specify the namespace of the drag container this view belongs to.
- [draggable(containerItemID:containerNamespace:)](<draggable(containeritemid_containernamespace_).md>) — Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
