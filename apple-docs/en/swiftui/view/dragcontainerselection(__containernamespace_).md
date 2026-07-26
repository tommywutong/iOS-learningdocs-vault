---
title: 'dragContainerSelection(_:containerNamespace:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 26.0+, visionOS 27.0+ beta]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dragcontainerselection(_:containernamespace:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dragcontainerselection(_:containernamespace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dragcontainerselection%28_%3Acontainernamespace%3A%29.json'
content_hash: 'sha256:2de58f0e5e140477'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dragContainerSelection(_:containerNamespace:)

<sub>Instance Method</sub>

Provides multiple item selection support for drag containers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func dragContainerSelection<ItemID>(_ selection: @autoclosure @escaping () -> Array<ItemID>, containerNamespace: Namespace.ID? = nil) -> some View where ItemID : Hashable, ItemID : Sendable

```

## Parameters

- `selection` — A closure that provides identifiers of selected items.

- `containerNamespace` — An optional namespace of the drag container.

## Discussion

A drag container finds the nearest enclosing `dragContainerSelection(_:containerNamespace:)` with the same item identifier type and same namespace, if specified. Drag container uses the provided selected item identifiers to determine what the drag payload should be.

If the dragged view is associated with a selected identifier, the payload should contain all the selected items. If the dragged view is not selected, the payload should not contain the whole selection, just the dragged item. With `dragContainerSelection(_:containerNamespace:)`, you get fine-grained control over what items are included in the drag payload.

```swift
 struct FruitContainer: View {
      @State private var fruits: [Fruit]
      @State private var selection: [Fruit.ID]

      var body: some View {
          VStack {
              ForEach(fruits) { fruit in
                  FruitView(fruit)
                      .draggable(containerItemID: fruit.id)
               }
           }
          .dragContainer(for: Fruit.self) { ids in
              fruits(with: ids)
          }
          .dragContainerSelection(selection)
      }

    func fruits(with ids: [Fruit.ID]) -> [Fruit] { ... }

    struct Fruit: Transferable, Identifiable {
        let id: String
        ...
    }

    struct FruitView: View {
        init(_ fruit: Fruit) { ... }
    }
}
```

## See Also

### Configuring drag-and-drop behavior

- [dragConfiguration(_:)](<dragconfiguration(__).md>) — Configures a drag session.
- [DragConfiguration](../dragconfiguration.md) — The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [dropConfiguration(_:)](<dropconfiguration(__).md>) — Configures a drop session.
- [DropConfiguration](../dropconfiguration.md) — Describes the behavior of the drop.
- [dragContainer(for:in:_:)](<dragcontainer(for_in___).md>) — A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainer(for:itemID:in:_:)](<dragcontainer(for_itemid_in___).md>) — A container with draggable views.
