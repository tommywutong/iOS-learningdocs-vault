---
title: uiImage
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/uiimage
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/uiimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/uiimage.json'
content_hash: 'sha256:d22872b01764bdc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# uiImage

<sub>Instance Property</sub>

The current contents of the view, rasterized as a UIKit image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
@MainActor final var uiImage: UIImage? { get }
```

## Discussion

The renderer notifies its `objectWillChange` publisher when the contents of the image may have changed.

## See Also

### Rendering images

- [render(rasterizationScale:renderer:)](<render(rasterizationscale_renderer_).md>) — Draws the renderer’s current contents to an arbitrary Core Graphics context.
- [cgImage](cgimage.md) — The current contents of the view, rasterized as a Core Graphics image.
- [nsImage](nsimage.md) — The current contents of the view, rasterized as an AppKit image.
