---
title: 'background(_:in:fillStyle:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/background(_:in:fillstyle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/background(_:in:fillstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/background%28_%3Ain%3Afillstyle%3A%29.json'
content_hash: 'sha256:5b7144f3839718f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# background(_:in:fillStyle:)

<sub>Instance Method</sub>

Sets the view’s background to an insettable shape filled with a style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func background<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : InsettableShape

```

## Parameters

- `style` — A [ShapeStyle](../shapestyle.md) that SwiftUI uses to the fill the shape that you specify.

- `shape` — An instance of a type that conforms to [InsettableShape](../insettableshape.md) that SwiftUI draws behind the view.

- `fillStyle` — The [FillStyle](../fillstyle.md) to use when drawing the shape. The default style uses the nonzero winding number rule and antialiasing.

## Return Value

A view with the specified insettable shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the [InsettableShape](../insettableshape.md) protocol — like a [Rectangle](../rectangle.md), [Circle](../circle.md), or [Capsule](../capsule.md) — behind a view. Specify the [ShapeStyle](../shapestyle.md) that’s used to fill the shape. For example, you can place a [RoundedRectangle](../roundedrectangle.md) behind a [Label](../label.md):

```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .background(.teal, in: RoundedRectangle(cornerRadius: 8))
```

The [teal](../shapestyle/teal.md) color fills the shape:

![A screenshot of the flag icon and word on a teal rectangle with](../../../../attachments/25bb6e11e1fedd80e63abb5c9307ae98/View-background-8@2x.png)

This modifier is a convenience method for placing a single shape behind a view. To create a background with other [View](../view.md) types — or with a stack of views — use [background(alignment:content:)](<background(alignment_content_).md>) instead. To add a [ShapeStyle](../shapestyle.md) as a background, use [background(_:ignoresSafeAreaEdges:)](<background(__ignoressafeareaedges_).md>).

## See Also

### Layering views

- [Adding a background to your view](../adding-a-background-to-your-view.md) — Compose a background behind your view and extend it beyond the safe area insets.
- [ZStack](../zstack.md) — A view that overlays its subviews, aligning them in both axes.
- [zIndex(_:)](<zindex(__).md>) — Controls the display order of overlapping views.
- [background(alignment:content:)](<background(alignment_content_).md>) — Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](<background(__ignoressafeareaedges_).md>) — Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](<background(ignoressafeareaedges_).md>) — Sets the view’s background to the default background style.
- [background(in:fillStyle:)](<background(in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with the default background style.
- [overlay(alignment:content:)](<overlay(alignment_content_).md>) — Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](<overlay(__ignoressafeareaedges_).md>) — Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](<overlay(__in_fillstyle_).md>) — Layers a shape that you specify in front of this view.
- [backgroundMaterial](../environmentvalues/backgroundmaterial.md) — The material underneath the current view.
- [containerBackground(_:for:)](<containerbackground(__for_).md>) — Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](<containerbackground(for_alignment_content_).md>) — Sets the container background of the enclosing container using a view.
- [ContainerBackgroundPlacement](../containerbackgroundplacement.md) — The placement of a container background.
