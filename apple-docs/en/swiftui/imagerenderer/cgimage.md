---
title: cgImage
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/cgimage
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/cgimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/cgimage.json'
content_hash: 'sha256:f4700970ac6770eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# cgImage

<sub>Instance Property</sub>

The current contents of the view, rasterized as a Core Graphics image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor final var cgImage: CGImage? { get }
```

## Discussion

The renderer notifies its `objectWillChange` publisher when the contents of the image may have changed.

## See Also

### Rendering images

- [render(rasterizationScale:renderer:)](<render(rasterizationscale_renderer_).md>) — Draws the renderer’s current contents to an arbitrary Core Graphics context.
- [nsImage](nsimage.md) — The current contents of the view, rasterized as an AppKit image.
- [uiImage](uiimage.md) — The current contents of the view, rasterized as a UIKit image.
