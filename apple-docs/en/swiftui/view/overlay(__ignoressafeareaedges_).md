---
title: 'overlay(_:ignoresSafeAreaEdges:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/overlay(_:ignoressafeareaedges:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/overlay(_:ignoressafeareaedges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/overlay%28_%3Aignoressafeareaedges%3A%29.json'
content_hash: 'sha256:63b3108c5ea49735'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# overlay(_:ignoresSafeAreaEdges:)

<sub>Instance Method</sub>

Layers the specified style in front of this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func overlay<S>(_ style: S, ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View where S : ShapeStyle

```

## Parameters

- `style` — An instance of a type that conforms to [ShapeStyle](../shapestyle.md) that SwiftUI layers in front of the modified view.

- `edges` — The set of edges for which to ignore safe area insets when adding the overlay. The default value is [all](../edge/set/all.md). Specify an empty set to respect safe area insets on all edges.

## Return Value

A view with the specified style drawn in front of it.

## Discussion

Use this modifier to layer a type that conforms to the [ShapeStyle](../shapestyle.md) protocol, like a [Color](../color.md), [Material](../material.md), or [HierarchicalShapeStyle](../hierarchicalshapestyle.md), in front of a view. For example, you can overlay the [ultraThinMaterial](../shapestyle/ultrathinmaterial.md) over a [Circle](../circle.md):

```swift
struct CoveredCircle: View {
    var body: some View {
        Circle()
            .frame(width: 300, height: 200)
            .overlay(.ultraThinMaterial)
    }
}
```

SwiftUI anchors the style to the view’s bounds. For the example above, the overlay fills the entirety of the circle’s frame (which happens to be wider than the circle is tall):

![A screenshot of a circle showing through a rectangle that imposes](../../../../attachments/ad8d81eac6822374f7b9a42224523ba6/View-overlay-5@2x.png)

SwiftUI also limits the style’s extent to the view’s container-relative shape. You can see this effect if you constrain the `CoveredCircle` view with a [containerShape(_:)](<containershape(__).md>) modifier:

```swift
CoveredCircle()
    .containerShape(RoundedRectangle(cornerRadius: 30))
```

The overlay takes on the specified container shape:

![A screenshot of a circle showing through a rounded rectangle that](../../../../attachments/79c6ec70d1f649f4c2eac46aa9cba166/View-overlay-6@2x.png)

By default, the overlay ignores safe area insets on all edges, but you can provide a specific set of edges to ignore, or an empty set to respect safe area insets on all edges:

```swift
Rectangle()
    .overlay(
        .secondary,
        ignoresSafeAreaEdges: []) // Ignore no safe area insets.
```

If you want to specify a [View](../view.md) or a stack of views as the overlay rather than a style, use [overlay(alignment:content:)](<overlay(alignment_content_).md>) instead. If you want to specify a [Shape](../shape.md), use [overlay(_:in:fillStyle:)](<overlay(__in_fillstyle_).md>).

## See Also

### Layering views

- [Adding a background to your view](../adding-a-background-to-your-view.md) — Compose a background behind your view and extend it beyond the safe area insets.
- [ZStack](../zstack.md) — A view that overlays its subviews, aligning them in both axes.
- [zIndex(_:)](<zindex(__).md>) — Controls the display order of overlapping views.
- [background(alignment:content:)](<background(alignment_content_).md>) — Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](<background(__ignoressafeareaedges_).md>) — Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](<background(ignoressafeareaedges_).md>) — Sets the view’s background to the default background style.
- [background(_:in:fillStyle:)](<background(__in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with a style.
- [background(in:fillStyle:)](<background(in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with the default background style.
- [overlay(alignment:content:)](<overlay(alignment_content_).md>) — Layers the views that you specify in front of this view.
- [overlay(_:in:fillStyle:)](<overlay(__in_fillstyle_).md>) — Layers a shape that you specify in front of this view.
- [backgroundMaterial](../environmentvalues/backgroundmaterial.md) — The material underneath the current view.
- [containerBackground(_:for:)](<containerbackground(__for_).md>) — Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](<containerbackground(for_alignment_content_).md>) — Sets the container background of the enclosing container using a view.
- [ContainerBackgroundPlacement](../containerbackgroundplacement.md) — The placement of a container background.
