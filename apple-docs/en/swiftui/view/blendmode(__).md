---
title: 'blendMode(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/blendmode(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/blendmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/blendmode%28_%3A%29.json'
content_hash: 'sha256:2f584d96914db72d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# blendMode(_:)

<sub>Instance Method</sub>

Sets the blend mode for compositing this view with overlapping views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func blendMode(_ blendMode: BlendMode) -> some View

```

## Parameters

- `blendMode` — The [BlendMode](../blendmode.md) for compositing this view.

## Return Value

A view that applies `blendMode` to this view.

## Discussion

Use `blendMode(_:)` to combine overlapping views and use a different visual effect to produce the result. The [BlendMode](../blendmode.md) enumeration defines many possible effects.

In the example below, the two overlapping rectangles have a [BlendMode.colorBurn](../blendmode/colorburn.md) effect applied, which effectively removes the non-overlapping portion of the second image:

```swift
HStack {
    Color.yellow.frame(width: 50, height: 50, alignment: .center)

    Color.red.frame(width: 50, height: 50, alignment: .center)
        .rotationEffect(.degrees(45))
        .padding(-20)
        .blendMode(.colorBurn)
}
```

![Two overlapping rectangles showing the effect of the blend mode view](../../../../attachments/c895f1b7ba32ddd9875ab5476003803e/SwiftUI-blendMode@2x.png)

## See Also

### Compositing views

- [compositingGroup()](<compositinggroup().md>) — Wraps this view in a compositing group.
- [drawingGroup(opaque:colorMode:)](<drawinggroup(opaque_colormode_).md>) — Composites this view’s contents into an offscreen image before final display.
- [BlendMode](../blendmode.md) — Modes for compositing a view with overlapping content.
- [ColorRenderingMode](../colorrenderingmode.md) — The set of possible working color spaces for color-compositing operations.
- [CompositorContent](../compositorcontent.md)
- [CompositorContentBuilder](../compositorcontentbuilder.md) — A result builder for composing a collection of [CompositorContent](../compositorcontent.md) elements.
- [AnyCompositorContent](../anycompositorcontent.md) — Type erased compositor content.
