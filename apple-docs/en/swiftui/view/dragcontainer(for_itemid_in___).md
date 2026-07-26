---
title: 'dragContainer(for:itemID:in:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 26.0+, visionOS 27.0+ beta]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dragcontainer(for:itemid:in:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dragcontainer(for:itemid:in:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dragcontainer%28for%3Aitemid%3Ain%3A_%3A%29.json'
content_hash: 'sha256:477b0aa0c2f436ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dragContainer(for:itemID:in:_:)

<sub>Instance Method</sub>

A container with draggable views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func dragContainer<ItemID, Item, Data>(for itemType: Item.Type = Item.self, itemID: KeyPath<Item, ItemID>, in namespace: Namespace.ID? = nil, _ payload: @escaping (Array<ItemID>) -> Data) -> some View where ItemID : Hashable, ItemID : Sendable, Item : Transferable, Item == Data.Element, Data : Collection

```

## Parameters

- `itemType` — A type of the dragged items.

- `itemID` — A closure that provides an item’s identifier.

- `namespace` — A namespace that identifies the drag container.

- `payload` — A closure which is called when a drag operation begins. As an argument, the closure receives either the identifiers of all the selected items, if the dragged item is a part of selection or only the identifier of the dragged item, if it is not part of the selection. Using the passed identifiers, put together the payload to drag, and return from the closure. Return an empty `Collection` to disable the drag.

## Return Value

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

## Discussion

In an example below, an app presents a view with `Fruit` values. `Fruit` does not conform to `Identifiable` but uses its name as its identifier.

```swift
@State private var fruits: [Fruit]
@State private var selection: [String]

var body: some View {
    VStack {
        ForEach(fruits) { fruit in
            FruitView(fruit)
                .draggable(containerItemID: fruit.name)
        }
    }
    .dragContainer(itemID: \Fruit.name) { ids in
       fruits(with: ids)
    }
}

func fruits(with ids: [String]) -> [Fruit] { ... }

struct Fruit: Transferable {
    var name: String
    ...
}
```

To enable multi-item drag, apply this modifier to a container view and mark each draggable child with [draggable(_:)](<draggable(__).md>) or [draggable(containerItemID:containerNamespace:)](<draggable(containeritemid_containernamespace_).md>).

## See Also

### Configuring drag-and-drop behavior

- [dragConfiguration(_:)](<dragconfiguration(__).md>) — Configures a drag session.
- [DragConfiguration](../dragconfiguration.md) — The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [dropConfiguration(_:)](<dropconfiguration(__).md>) — Configures a drop session.
- [DropConfiguration](../dropconfiguration.md) — Describes the behavior of the drop.
- [dragContainer(for:in:_:)](<dragcontainer(for_in___).md>) — A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainerSelection(_:containerNamespace:)](<dragcontainerselection(__containernamespace_).md>) — Provides multiple item selection support for drag containers.
