---
title: compositingGroup()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/compositinggroup()
source_url: 'https://developer.apple.com/documentation/swiftui/view/compositinggroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/compositinggroup%28%29.json'
content_hash: 'sha256:0453471e7fe5b87e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# compositingGroup()

<sub>Instance Method</sub>

Wraps this view in a compositing group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func compositingGroup() -> some View

```

## Return Value

A view that wraps this view in a compositing group.

## Discussion

A compositing group makes compositing effects in this view’s ancestor views, such as opacity and the blend mode, take effect before this view is rendered.

Use `compositingGroup()` to apply effects to a parent view before applying effects to this view.

In the example below the `compositingGroup()` modifier separates the application of effects into stages. It applies the [opacity(_:)](<opacity(__).md>) effect to the VStack before the `blur(radius:)` effect is applied to the views inside the enclosed [ZStack](../zstack.md). This limits the scope of the opacity change to the outermost view.

```swift
VStack {
    ZStack {
        Text("CompositingGroup")
            .foregroundColor(.black)
            .padding(20)
            .background(Color.red)
        Text("CompositingGroup")
            .blur(radius: 2)
    }
    .font(.largeTitle)
    .compositingGroup()
    .opacity(0.9)
}
```

![A view showing the effect of the compositingGroup modifier in applying](../../../../attachments/102ab31bc2decb6b1f250dfb49c77c62/SwiftUI-View-compositingGroup@2x.png)

## See Also

### Compositing views

- [blendMode(_:)](<blendmode(__).md>) — Sets the blend mode for compositing this view with overlapping views.
- [drawingGroup(opaque:colorMode:)](<drawinggroup(opaque_colormode_).md>) — Composites this view’s contents into an offscreen image before final display.
- [BlendMode](../blendmode.md) — Modes for compositing a view with overlapping content.
- [ColorRenderingMode](../colorrenderingmode.md) — The set of possible working color spaces for color-compositing operations.
- [CompositorContent](../compositorcontent.md)
- [CompositorContentBuilder](../compositorcontentbuilder.md) — A result builder for composing a collection of [CompositorContent](../compositorcontent.md) elements.
- [AnyCompositorContent](../anycompositorcontent.md) — Type erased compositor content.
