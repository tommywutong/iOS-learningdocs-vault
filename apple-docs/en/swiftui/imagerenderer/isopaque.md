---
title: isOpaque
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/isopaque
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/isopaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/isopaque.json'
content_hash: 'sha256:d5170d63642feefb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# isOpaque

<sub>Instance Property</sub>

A Boolean value that indicates whether the alpha channel of the image is fully opaque.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor final var isOpaque: Bool { get set }
```

## Discussion

Setting this value to `true`, meaning the alpha channel is opaque, may improve performance. Don’t render non-opaque pixels to a renderer declared as opaque. This property defaults to `false`.

## See Also

### Accessing renderer properties

- [proposedSize](proposedsize.md) — The size proposed to the root view.
- [scale](scale.md) — The scale at which to render the image.
- [colorMode](colormode.md) — The working color space and storage format of the image.
- [allowedDynamicRange](alloweddynamicrange.md) — The allowed dynamic range of the image, or nil to mark that the dynamic range of the image should be unrestricted. This property defaults to `sdr`, i.e. HDR content will be tone mapped to SDR.
