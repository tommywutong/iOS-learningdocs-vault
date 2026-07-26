---
title: 'dropConfiguration(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dropconfiguration(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dropconfiguration(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dropconfiguration%28_%3A%29.json'
content_hash: 'sha256:fbf6533dc667fc97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dropConfiguration(_:)

<sub>Instance Method</sub>

Configures a drop session.

<sub>macOS</sub>

```swift
nonisolated func dropConfiguration(_ configuration: @escaping (DropSession) -> DropConfiguration) -> some View

```

## Parameters

- `configuration` — A value that describes the configuration of a drop session.

## Return Value

A view that configures a drop session in a way, described by the return value of the `configuration` parameter.

## Discussion

Below is an example of a view that accepts drop of `Image` type. The view prefers drop operation `move` in a case when the source supports it (the source will remove the images from its storage after the drop operation). If the source does not support moving images, the destination will make copies.

```swift
       ExampleView()
           .dropDestination(for: Image.self) { images, _ in
               process(images)
           }
           .dropConfiguration { dropSession in
               if dropSession.suggestedOperations.contains(.move) {
                   return DropConfiguration(operation: .move)
               }
               return DropConfiguration(operation: .copy)
           }
```

> [!note] Note
> The closure that provides the configuration is called frequently to allow specifying different operations for different drop locations in a view. Do not perform any expensive calculations in it.

## See Also

### Configuring drag-and-drop behavior

- [dragConfiguration(_:)](<dragconfiguration(__).md>) — Configures a drag session.
- [DragConfiguration](../dragconfiguration.md) — The behavior of the drag, proposed by the dragging source. A value that describes the drag operations a drag source supports.
- [DropConfiguration](../dropconfiguration.md) — Describes the behavior of the drop.
- [dragContainer(for:in:_:)](<dragcontainer(for_in___).md>) — A container with draggable views where the drag payload is based on multiple identifiers of dragged items.
- [dragContainer(for:itemID:in:_:)](<dragcontainer(for_itemid_in___).md>) — A container with draggable views.
- [dragContainerSelection(_:containerNamespace:)](<dragcontainerselection(__containernamespace_).md>) — Provides multiple item selection support for drag containers.
