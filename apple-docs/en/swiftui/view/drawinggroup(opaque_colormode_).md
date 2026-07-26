---
title: 'drawingGroup(opaque:colorMode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/drawinggroup(opaque:colormode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/drawinggroup(opaque:colormode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/drawinggroup%28opaque%3Acolormode%3A%29.json'
content_hash: 'sha256:cb59b4dd0b0ba6eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# drawingGroup(opaque:colorMode:)

<sub>Instance Method</sub>

Composites this view’s contents into an offscreen image before final display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func drawingGroup(opaque: Bool = false, colorMode: ColorRenderingMode = .nonLinear) -> some View

```

## Parameters

- `opaque` — A Boolean value that indicates whether the image is opaque. The default is `false`; if set to `true`, the alpha channel of the image must be `1`.

- `colorMode` — One of the working color space and storage formats defined in [ColorRenderingMode](../colorrenderingmode.md). The default is [ColorRenderingMode.nonLinear](../colorrenderingmode/nonlinear.md).

## Return Value

A view that composites this view’s contents into an offscreen image before display.

## Discussion

The `drawingGroup(opaque:colorMode:)` modifier flattens a subtree of views into a single view before rendering it.

In the example below, the contents of the view are composited to a single bitmap; the bitmap is then displayed in place of the view:

```swift
VStack {
    ZStack {
        Text("DrawingGroup")
            .foregroundColor(.black)
            .padding(20)
            .background(Color.red)
        Text("DrawingGroup")
            .blur(radius: 2)
    }
    .font(.largeTitle)
    .compositingGroup()
    .opacity(1.0)
}
.background(Color.white)
.drawingGroup()
```

> [!important] Important
> The visual result of a drawing group only includes views that SwiftUI rasterizes directly using its own drawing primitives, such as text, images, shapes, and composite views of these types. It will not include views whose contents are composited by Core Animation layers, such as more complex controls and containers, web views, media players, and most types of UIKit and AppKit views. In those cases, the output displays a placeholder image instead. Whether a particular view is rendered using SwiftUI’s own drawing primitives or composited by Core Animation may change in future releases. However, any view that is currently supported is guaranteed to remain supported.

![A screenshot showing the effects on several stacks configured as a](../../../../attachments/c81675b1f1b78f79e131cdabc7d7a89a/SwiftUI-View-drawingGroup@2x.png)

## See Also

### Compositing views

- [blendMode(_:)](<blendmode(__).md>) — Sets the blend mode for compositing this view with overlapping views.
- [compositingGroup()](<compositinggroup().md>) — Wraps this view in a compositing group.
- [BlendMode](../blendmode.md) — Modes for compositing a view with overlapping content.
- [ColorRenderingMode](../colorrenderingmode.md) — The set of possible working color spaces for color-compositing operations.
- [CompositorContent](../compositorcontent.md)
- [CompositorContentBuilder](../compositorcontentbuilder.md) — A result builder for composing a collection of [CompositorContent](../compositorcontent.md) elements.
- [AnyCompositorContent](../anycompositorcontent.md) — Type erased compositor content.
