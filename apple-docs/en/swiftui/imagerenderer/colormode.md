---
title: colorMode
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/colormode
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/colormode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/colormode.json'
content_hash: 'sha256:03db27b048186cf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# colorMode

<sub>Instance Property</sub>

The working color space and storage format of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor final var colorMode: ColorRenderingMode { get set }
```

## See Also

### Accessing renderer properties

- [proposedSize](proposedsize.md) — The size proposed to the root view.
- [scale](scale.md) — The scale at which to render the image.
- [isOpaque](isopaque.md) — A Boolean value that indicates whether the alpha channel of the image is fully opaque.
- [allowedDynamicRange](alloweddynamicrange.md) — The allowed dynamic range of the image, or nil to mark that the dynamic range of the image should be unrestricted. This property defaults to `sdr`, i.e. HDR content will be tone mapped to SDR.
