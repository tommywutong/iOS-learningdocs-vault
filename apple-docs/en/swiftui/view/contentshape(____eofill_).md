---
title: 'contentShape(_:_:eoFill:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/contentshape(_:_:eofill:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/contentshape(_:_:eofill:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/contentshape%28_%3A_%3Aeofill%3A%29.json'
content_hash: 'sha256:9034c19c6d1b7fd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# contentShape(_:_:eoFill:)

<sub>Instance Method</sub>

Sets the content shape for this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func contentShape<S>(_ kind: ContentShapeKinds, _ shape: S, eoFill: Bool = false) -> some View where S : Shape

```

## Parameters

- `kind` — The kinds to apply to this content shape.

- `shape` — The shape to use.

- `eoFill` — A Boolean that indicates whether the shape is interpreted with the even-odd winding number rule.

## Return Value

A view that uses the given shape for the specified kind.

## Discussion

The content shape has a variety of uses. You can control the kind of the content shape by specifying one in `kind`. The following example sets the focus ring shape of the view, without affecting its shape for hit-testing:

```swift
MyFocusableView()
    .contentShape(.focusEffect, Circle())
```

You can apply multiple kinds of content shapes to the same view. For example, apply a [interaction](../contentshapekinds/interaction.md) shape and [focusEffect](../contentshapekinds/focuseffect.md) shape together to set both the hit-testing shape and focus ring shape on a view.

## Context Menu & Drag Previews

You can control the preview shown by the system for context menus or drags using the relevant content shape kind, like [dragPreview](../contentshapekinds/dragpreview.md) and [contextMenuPreview](../contentshapekinds/contextmenupreview.md).

The following example creates a [VStack](../vstack.md) of an [Image](../image.md) and [Text](../text.md) that has a context menu with a custom content shape:

```swift
VStack {
    Image("turtlerock")
        .contentShape(.contextMenuPreview,
                      RoundedRectangle(cornerRadius: 10))
    Text("Turtle Rock")
}
.contextMenu {
    Button {
        // Add this item to a list of favorites.
    } label: {
        Label("Add to Favorites", systemImage: "heart")
    }
}
```

When someone activates the context menu with an action like touch and hold in iOS or iPadOS, the system uses the [Image](../image.md) as the preview for the context menu, applying the requested corner radius.

The content shape also supports applying modifiers such as [inset(by:)](<../insettableshape/inset(by_).md>) to add padding.

> [!note] Note
> Similar to [focusEffect](../contentshapekinds/focuseffect.md), the [contextMenuPreview](../contentshapekinds/contextmenupreview.md) and [dragPreview](../contentshapekinds/dragpreview.md) content shapes do not impact the hit-testing shape. In this example, someone can touch and hold anywhere on the [VStack](../vstack.md) to activate the menu. If you only want the [Image](../image.md) to activate the menu, apply [contextMenu(menuItems:)](<contextmenu(menuitems_).md>) to the [Image](../image.md) instead.

## See Also

### Controlling hit testing

- [allowsTightening(_:)](<allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [contentShape(_:eoFill:)](<contentshape(__eofill_).md>) — Defines the content shape for hit testing.
- [ContentShapeKinds](../contentshapekinds.md) — A kind for the content shape of a view.
