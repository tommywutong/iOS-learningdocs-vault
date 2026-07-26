---
title: 'scrollBounceBehavior(_:axes:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrollbouncebehavior(_:axes:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrollbouncebehavior(_:axes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrollbouncebehavior%28_%3Aaxes%3A%29.json'
content_hash: 'sha256:04793940cb054a90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollBounceBehavior(_:axes:)

<sub>Instance Method</sub>

Configures the bounce behavior of scrollable views along the specified axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scrollBounceBehavior(_ behavior: ScrollBounceBehavior, axes: Axis.Set = [.vertical]) -> some View

```

## Parameters

- `behavior` — The bounce behavior to apply to any scrollable views within the configured view. Use one of the [ScrollBounceBehavior](../scrollbouncebehavior.md) values.

- `axes` — The set of axes to apply `behavior` to. The default is [Axis.vertical](../axis/vertical.md).

## Return Value

A view that’s configured with the specified scroll bounce behavior.

## Discussion

Use this modifier to indicate whether scrollable views bounce when people scroll to the end of the view’s content, taking into account the relative sizes of the view and its content. For example, the following [ScrollView](../scrollview.md) only enables bounce behavior if its content is large enough to require scrolling:

```swift
ScrollView {
    Text("Small")
    Text("Content")
}
.scrollBounceBehavior(.basedOnSize)
```

The modifier passes the scroll bounce mode through the [Environment](../environment.md), which means that the mode affects any scrollable views in the modified view hierarchy. Provide an axis to the modifier to constrain the kinds of scrollable views that the mode affects. For example, all the scroll views in the following example can access the mode value, but only the two nested scroll views are affected, because only they use horizontal scrolling:

```swift
ScrollView { // Defaults to vertical scrolling.
    ScrollView(.horizontal) {
        ShelfContent()
    }
    ScrollView(.horizontal) {
        ShelfContent()
    }
}
.scrollBounceBehavior(.basedOnSize, axes: .horizontal)
```

You can use this modifier to configure any kind of scrollable view, including [ScrollView](../scrollview.md), [List](../list.md), [Table](../table.md), and [TextEditor](../texteditor.md):

```swift
List {
    Text("Hello")
    Text("World")
}
.scrollBounceBehavior(.basedOnSize)
```

## See Also

### Configuring scroll bounce behavior

- [horizontalScrollBounceBehavior](../environmentvalues/horizontalscrollbouncebehavior.md) — The scroll bounce mode for the horizontal axis of scrollable views.
- [verticalScrollBounceBehavior](../environmentvalues/verticalscrollbouncebehavior.md) — The scroll bounce mode for the vertical axis of scrollable views.
- [ScrollBounceBehavior](../scrollbouncebehavior.md) — The ways that a scrollable view can bounce when it reaches the end of its content.
