---
title: 'render(rasterizationScale:renderer:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/imagerenderer/render(rasterizationscale:renderer:)'
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/render(rasterizationscale:renderer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/render%28rasterizationscale%3Arenderer%3A%29.json'
content_hash: 'sha256:a7cb9e0488c8c184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# render(rasterizationScale:renderer:)

<sub>Instance Method</sub>

Draws the renderer’s current contents to an arbitrary Core Graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor final func render(rasterizationScale: CGFloat = 1, renderer: (CGSize, (CGContext) -> Void) -> Void)
```

## Parameters

- `rasterizationScale` — The scale factor for converting user interface points to pixels when rasterizing parts of the view that can’t be represented as native Core Graphics drawing commands.

- `renderer` — The closure that sets up the Core Graphics context and renders the view. This closure receives two parameters: the size of the view and a function that you invoke in the closure to render the view at the reported size. This function takes a [CGContext](../../coregraphics/cgcontext.md) parameter, and assumes a bottom-left coordinate space origin.

## Discussion

Use this method to rasterize the renderer’s content to a [CGContext](../../coregraphics/cgcontext.md) you provide. The `renderer` closure receives two parameters: the current size of the view, and a function that renders the view to your `CGContext`. Implement the closure to provide a suitable `CGContext`, then invoke the function to render the content to that context.

## See Also

### Rendering images

- [cgImage](cgimage.md) — The current contents of the view, rasterized as a Core Graphics image.
- [nsImage](nsimage.md) — The current contents of the view, rasterized as an AppKit image.
- [uiImage](uiimage.md) — The current contents of the view, rasterized as a UIKit image.
