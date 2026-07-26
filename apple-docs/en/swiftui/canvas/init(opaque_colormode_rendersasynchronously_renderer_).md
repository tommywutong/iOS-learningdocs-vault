---
title: 'init(opaque:colorMode:rendersAsynchronously:renderer:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/canvas/init(opaque:colormode:rendersasynchronously:renderer:)'
source_url: 'https://developer.apple.com/documentation/swiftui/canvas/init(opaque:colormode:rendersasynchronously:renderer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/canvas/init%28opaque%3Acolormode%3Arendersasynchronously%3Arenderer%3A%29.json'
content_hash: 'sha256:3e1da89286a318f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Canvas](../canvas.md)

# init(opaque:colorMode:rendersAsynchronously:renderer:)

<sub>Initializer</sub>

Creates and configures a canvas.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(opaque: Bool = false, colorMode: ColorRenderingMode = .nonLinear, rendersAsynchronously: Bool = false, renderer: @escaping (inout GraphicsContext, CGSize) -> Void)
```

## Parameters

- `opaque` — A Boolean that indicates whether the canvas is fully opaque. You might be able to improve performance by setting this value to `true`, but then drawing a non-opaque image into the context produces undefined results. The default is `false`.

- `colorMode` — A working color space and storage format of the canvas. The default is [ColorRenderingMode.nonLinear](../colorrenderingmode/nonlinear.md).

- `rendersAsynchronously` — A Boolean that indicates whether the canvas can present its contents to its parent view asynchronously. The default is `false`.

- `renderer` — A closure in which you conduct immediate mode drawing. The closure takes two inputs: a context that you use to issue drawing commands and a size — representing the current size of the canvas — that you can use to customize the content. The canvas calls the renderer any time it needs to redraw the content.

## Discussion

Use this initializer to create a new canvas that you can draw into. For example, you can draw a path:

```swift
Canvas { context, size in
    context.stroke(
        Path(ellipseIn: CGRect(origin: .zero, size: size)),
        with: .color(.green),
        lineWidth: 4)
}
.frame(width: 300, height: 200)
.border(Color.blue)
```

The example above draws the outline of an ellipse that exactly inscribes a canvas with a blue border:

![A screenshot of a canvas view that shows the green outline of an](../../../../attachments/da33312de456cfbf0dfa4f0f517083c8/Canvas-1@2x.png)

For information about using a context to draw into a canvas, see [GraphicsContext](../graphicscontext.md). If you want to provide SwiftUI views for the renderer to use as drawing elements, use [init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)](<init(opaque_colormode_rendersasynchronously_renderer_symbols_).md>) instead.

## See Also

### Creating a canvas

- [init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)](<init(opaque_colormode_rendersasynchronously_renderer_symbols_).md>) — Creates and configures a canvas that you supply with renderable child views.
