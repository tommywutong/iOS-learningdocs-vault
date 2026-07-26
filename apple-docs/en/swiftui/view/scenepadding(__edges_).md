---
title: 'scenePadding(_:edges:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scenepadding(_:edges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scenepadding(_:edges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scenepadding%28_%3Aedges%3A%29.json'
content_hash: 'sha256:bad1b7e426635f48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scenePadding(_:edges:)

<sub>Instance Method</sub>

Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scenePadding(_ padding: ScenePadding, edges: Edge.Set = .all) -> some View

```

## Parameters

- `padding` — The kind of padding to add.

- `edges` — The set of edges along which to pad this view.

## Return Value

A view that’s padded on specified edges by a scene-appropriate amount.

## Discussion

Use this modifier to add a scene-appropriate amount of padding to a view. Specify either a single edge value from [Set](../edge/set.md), or an [OptionSet](../../swift/optionset.md) that describes the edges to pad.

In macOS, use scene padding to produce the recommended spacing around the root view of a window. In watchOS, use scene padding to align elements of your user interface with top level elements, like the title of a navigation view. For example, compare the effects of different kinds of padding on text views presented inside a [NavigationView](../navigationview.md) in watchOS:

```swift
VStack(alignment: .leading, spacing: 10) {
    Text("Minimum Scene padding")
        .scenePadding(.minimum, edges: .horizontal)
        .border(.red) // Border added for reference.
    Text("Navigation Bar Scene padding")
        .scenePadding(.navigationBar, edges: .horizontal)
        .border(.yellow)
    Text("Regular padding")
        .padding(.horizontal)
        .border(.green)
    Text("Text with no padding")
        .border(.blue)
    Button("Button") { }
}
.navigationTitle("Hello World")
```

The text with minimum scene padding uses the system minimum padding and the text with navigation bar scene padding automatically aligns with the navigation bar content. In contrast, the text that uses the default padding and the text without padding do not align with scene elements.

Scene padding in watchOS also ensures that your content avoids the curved edges of a device like Apple Watch Series 7. In other platforms, scene padding produces the same default padding that you get from the [padding(_:_:)](<padding(____).md>) modifier.

> [!important] Important
> Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even if you specify those edges as part of the input. For example, if you specify [vertical](../edge/set/vertical.md) instead of [horizontal](../edge/set/horizontal.md) in the example above, the modifier would have no effect in watchOS. It does, however, apply to all the edges that you specify in other platforms.

## See Also

### Adding padding around a view

- [padding(_:)](<padding(__).md>) — Adds a different padding amount to each edge of this view.
- [padding(_:_:)](<padding(____).md>) — Adds an equal padding amount to specific edges of this view.
- [padding3D(_:)](<padding3d(__).md>) — Pads this view using the edge insets you specify.
- [padding3D(_:_:)](<padding3d(____).md>) — Pads this view using the edge insets you specify.
- [scenePadding(_:)](<scenepadding(__).md>) — Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [ScenePadding](../scenepadding.md) — The padding used to space a view from its containing scene.
