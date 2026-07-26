---
title: nsImage
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/nsimage
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/nsimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/nsimage.json'
content_hash: 'sha256:ae89410682ecc449'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# nsImage

<sub>Instance Property</sub>

The current contents of the view, rasterized as an AppKit image.

<sub>macOS</sub>

```swift
@MainActor final var nsImage: NSImage? { get }
```

## Discussion

The renderer notifies its `objectWillChange` publisher when the contents of the image may have changed.

## See Also

### Rendering images

- [render(rasterizationScale:renderer:)](<render(rasterizationscale_renderer_).md>) — Draws the renderer’s current contents to an arbitrary Core Graphics context.
- [cgImage](cgimage.md) — The current contents of the view, rasterized as a Core Graphics image.
- [uiImage](uiimage.md) — The current contents of the view, rasterized as a UIKit image.
